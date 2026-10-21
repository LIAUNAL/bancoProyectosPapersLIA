"""SQLite FTS5 index over data/bank.json, the query layer of the Banco LIA MCP server.

The index (data/bank.db) is derived data: it is rebuilt automatically whenever the
content of bank.json changes, so `bancoLIA build` never has to remember it.

    python3 tools/bank_db.py build            # force a rebuild
    python3 tools/bank_db.py search "EEG"     # quick check from the shell
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "1"
# Weighted for bm25(): title and keywords count more than the long narrative fields.
FTS_COLUMNS = [("title", 5.0), ("palabras_clave", 3.0), ("metodos", 2.0), ("temas", 2.0), ("aplicacion", 1.0),
               ("problema", 1.0), ("propuesta", 1.0), ("resultados", 1.0), ("conclusiones", 1.0),
               ("idea_futura", 1.0), ("productos", 1.0), ("aliados", 1.0)]
KIND_DIRS = {"articulo": "articulos", "proyecto": "proyectos"}


def as_list(value):
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value.strip().startswith("["):
        try:
            parsed = ast.literal_eval(value)
            return parsed if isinstance(parsed, list) else [parsed]
        except (ValueError, SyntaxError):
            pass
    return [value] if value else []


def as_year(value):
    try:
        return int(str(value)[:4])
    except (TypeError, ValueError):
        return None


# Any word may match (OR), so function words would match nearly every item.
STOPWORDS = set("""a al con como de del e el en entre es la las lo los o para por que se sin su sus un una uno y
an and as at by for from in is of on or the to with""".split())


def match_query(text, match="any"):
    """Free text to a safe FTS5 query: every word is quoted, so FTS operators are inert.
    match="any" joins the words with OR, match="all" with AND."""
    words = [w for w in re.findall(r"\w+", text or "") if w.lower() not in STOPWORDS]
    return (" AND " if match == "all" else " OR ").join('"%s"' % w for w in words)


class Bank:
    def __init__(self, bank_path=ROOT / "data/bank.json", db_path=ROOT / "data/bank.db"):
        self.bank_path = Path(bank_path)
        self.db_path = Path(db_path)
        self.root = self.bank_path.parent.parent
        self._con = None

    # -- index ---------------------------------------------------------------
    def _fingerprint(self):
        return SCHEMA_VERSION + ":" + hashlib.sha256(self.bank_path.read_bytes()).hexdigest()

    def _stored_fingerprint(self):
        if not self.db_path.exists():
            return None
        try:
            con = sqlite3.connect(self.db_path)
            try:
                row = con.execute("select value from meta where key='fingerprint'").fetchone()
            finally:
                con.close()
            return row[0] if row else None
        except sqlite3.DatabaseError:
            return None

    def build(self):
        """Write the index to a temporary file and swap it in, so readers never see a half-built db."""
        bank = json.loads(self.bank_path.read_text(encoding="utf-8"))
        topics = bank.get("topics", {})
        tmp = self.db_path.with_suffix(".db.tmp")
        if tmp.exists():
            tmp.unlink()
        con = sqlite3.connect(tmp)
        con.executescript(
            """
            create table meta(key text primary key, value text);
            create table items(id text primary key, kind text, year integer, cluster text, title text,
                               slug text, doc text);
            create table item_topics(item_id text, topic text);
            create table links(src text, dst text, rel text, sim real);
            create table topics(id text primary key, name text, scope text);
            create table clusters(id text primary key, name text, doc text);
            """
        )
        cols = ", ".join(c for c, _ in FTS_COLUMNS)
        con.execute(f"create virtual table items_fts using fts5(id unindexed, {cols}, "
                    "tokenize='unicode61 remove_diacritics 2')")
        for tid, t in topics.items():
            con.execute("insert into topics values(?,?,?)", (tid, t.get("name", ""), t.get("scope", "")))
        for c in bank.get("clusters", []):
            con.execute("insert into clusters values(?,?,?)", (c["id"], c.get("name", ""), json.dumps(c, ensure_ascii=False)))
        for link in bank.get("links", []):
            con.execute("insert into links values(?,?,?,?)", (link["from"], link["to"], link.get("rel", ""), link.get("sim")))
        for it in bank.get("items", []):
            temas = [str(t) for t in as_list(it.get("temas"))]
            con.execute("insert into items values(?,?,?,?,?,?,?)",
                        (it["id"], it.get("kind", ""), as_year(it.get("year")), it.get("cluster", ""),
                         it.get("title", ""), it.get("slug", ""), json.dumps(it, ensure_ascii=False)))
            con.executemany("insert into item_topics values(?,?)", [(it["id"], t) for t in temas])
            for t in as_list(it.get("top5")):
                if isinstance(t, dict) and t.get("id"):
                    con.execute("insert into links values(?,?,?,?)", (it["id"], t["id"], "similar", t.get("sim")))
            text = {
                "title": " ".join(filter(None, [it.get("title"), it.get("titulo_corto")])),
                "palabras_clave": " · ".join(map(str, as_list(it.get("palabras_clave")))),
                "metodos": " · ".join(map(str, as_list(it.get("metodos")))),
                "temas": " · ".join(topics.get(t, {}).get("name", t) for t in temas),
                "productos": " · ".join(map(str, as_list(it.get("productos_tecnologicos")))),
                "aliados": " · ".join(map(str, as_list(it.get("aliados")) + as_list(it.get("financiador")))),
            }
            row = [it["id"]] + [text.get(c, it.get(c) or "") for c, _ in FTS_COLUMNS]
            con.execute(f"insert into items_fts values({', '.join('?' * len(row))})", [str(v) for v in row])
        con.execute("insert into meta values('fingerprint', ?)", (self._fingerprint(),))
        con.commit()
        con.close()
        os.replace(tmp, self.db_path)

    def con(self):
        if self._con is None or self._stored_fingerprint() != self._fingerprint():
            if self._con is not None:
                self._con.close()
            if self._stored_fingerprint() != self._fingerprint():
                self.build()
            self._con = sqlite3.connect(self.db_path, check_same_thread=False)
            self._con.row_factory = sqlite3.Row
        return self._con

    # -- queries -------------------------------------------------------------
    def _doc(self, row):
        return json.loads(row["doc"])

    def _summary(self, row, **extra):
        doc = self._doc(row)
        out = {"id": row["id"], "kind": row["kind"], "title": row["title"], "year": row["year"], "cluster": row["cluster"]}
        if doc.get("doi"):
            out["doi"] = doc["doi"]
        out.update(extra)
        return out

    def search(self, query="", kind=None, cluster=None, topic=None, year_from=None, limit=10, match="any"):
        """Items ranked by BM25 relevance; with no query, the filtered items newest first."""
        con = self.con()
        where, args = [], []
        if kind:
            where.append("i.kind = ?"); args.append(kind)
        if cluster:
            where.append("i.cluster = ?"); args.append(cluster.upper())
        if topic:
            where.append("i.id in (select item_id from item_topics where topic = ?)"); args.append(topic.upper())
        if year_from:
            where.append("i.year >= ?"); args.append(int(year_from))
        limit = max(1, min(int(limit or 10), 100))
        q = match_query(query, match)
        if (query or "").strip() and not q:
            return []
        if q:
            weights = ", ".join(str(w) for _, w in FTS_COLUMNS)
            sql = (f"select i.*, bm25(items_fts, 0, {weights}) as score, "
                   "snippet(items_fts, -1, '[', ']', '…', 14) as snip "
                   "from items_fts join items i on i.id = items_fts.id where items_fts match ? "
                   + "".join(" and " + w for w in where) + " order by score, i.id limit ?")
            rows = con.execute(sql, [q] + args + [limit]).fetchall()
            return [self._summary(r, snippet=r["snip"], score=round(-r["score"], 3)) for r in rows]
        sql = "select i.* from items i" + (" where " + " and ".join(where) if where else "") + \
              " order by i.year desc, i.id limit ?"
        return [self._summary(r) for r in con.execute(sql, args + [limit]).fetchall()]

    def _row(self, item_id):
        return self.con().execute("select * from items where id = ?", ((item_id or "").upper(),)).fetchone()

    def get_item(self, item_id):
        row = self._row(item_id)
        if row is None:
            return None
        doc = self._doc(row)
        topics = dict(self.con().execute("select id, name from topics").fetchall())
        doc["topic_names"] = [topics.get(str(t), str(t)) for t in as_list(doc.get("temas"))]
        md = self._markdown_path(row)
        doc["markdown_path"] = str(md) if md.exists() else None
        doc["markdown"] = md.read_text(encoding="utf-8") if md.exists() else None
        return doc

    def _markdown_path(self, row):
        return self.root / KIND_DIRS.get(row["kind"], row["kind"]) / f"{row['slug']}.md"

    def _title(self, item_id):
        row = self._row(item_id)
        return row["title"] if row else None

    def related_items(self, item_id):
        row = self._row(item_id)
        if row is None:
            return None
        con, iid = self.con(), row["id"]
        links = []
        for r in con.execute("select src, dst, rel from links where rel != 'similar' and (src = ? or dst = ?) "
                             "order by rel, src, dst", (iid, iid)):
            other, direction = (r["dst"], "out") if r["src"] == iid else (r["src"], "in")
            links.append({"id": other, "rel": r["rel"], "direction": direction, "title": self._title(other)})
        similar = [{"id": r["dst"], "sim": r["sim"], "title": self._title(r["dst"])}
                   for r in con.execute("select dst, sim from links where rel = 'similar' and src = ? "
                                        "order by sim desc", (iid,))]
        same = [self._summary(r) for r in con.execute(
            "select * from items where cluster = ? and id != ? order by year desc, id", (row["cluster"], iid))]
        return {"id": iid, "title": row["title"], "links": links, "similar": similar, "same_cluster": same}

    def lab_capabilities(self, query="", kind=None, limit=50, match="all"):
        """What the lab can bring to a topic: allies, funders, products, methods, with the items behind each."""
        items = [self._row(h["id"]) for h in self.search(query, kind=kind, limit=limit, match=match)] if (query or "").strip() else \
            self.con().execute("select * from items" + (" where kind = ?" if kind else ""), (kind,) if kind else ()).fetchall()
        fields = {"aliados": "aliados", "financiadores": "financiador",
                  "productos_tecnologicos": "productos_tecnologicos", "metodos": "metodos"}
        agg = {name: defaultdict(list) for name in fields}
        clusters, years = defaultdict(int), set()
        for row in items:
            doc = self._doc(row)
            for name, field in fields.items():
                for value in as_list(doc.get(field)):
                    value = str(value).strip()
                    if value and row["id"] not in agg[name][value]:
                        agg[name][value].append(row["id"])
            clusters[row["cluster"]] += 1
            if row["year"]:
                years.add(row["year"])
        out = {"query": query, "items": len(items), "years": sorted(years),
               "clusters": [{"id": c, "items": n} for c, n in sorted(clusters.items(), key=lambda x: (-x[1], x[0]))]}
        for name, values in agg.items():
            out[name] = [{"value": v, "items": ids} for v, ids in sorted(values.items(), key=lambda x: (-len(x[1]), x[0]))]
        return out

    def taxonomy(self):
        con = self.con()
        topics = [{"id": r["id"], "name": r["name"], "scope": r["scope"],
                   "items": con.execute("select count(distinct item_id) from item_topics where topic = ?", (r["id"],)).fetchone()[0]}
                  for r in con.execute("select * from topics order by id")]
        clusters = []
        for r in con.execute("select * from clusters order by id"):
            doc = json.loads(r["doc"])
            clusters.append({"id": r["id"], "name": r["name"], "top_terms": doc.get("top_terms", []),
                             "items": con.execute("select count(*) from items where cluster = ?", (r["id"],)).fetchone()[0]})
        return {"topics": topics, "clusters": clusters}

    def export(self, ids, dest_dir):
        """Copy the items' Markdown files into an existing folder (e.g. a proposal's insumos/background)."""
        dest = Path(dest_dir).expanduser()
        if not dest.is_dir():
            raise ValueError(f"destination folder does not exist: {dest}")
        written, missing = [], []
        for item_id in ids:
            row = self._row(item_id)
            md = self._markdown_path(row) if row else None
            if md is None or not md.exists():
                missing.append(item_id)
                continue
            target = dest / f"banco-lia-{row['slug']}.md"
            target.write_text(md.read_text(encoding="utf-8"), encoding="utf-8")
            written.append(str(target))
        return {"written": written, "missing": missing}


def main(argv):
    bank = Bank()
    if argv[:1] == ["build"]:
        bank.build()
        print(f"index written to {bank.db_path}")
    elif argv[:1] == ["search"] and len(argv) > 1:
        for hit in bank.search(" ".join(argv[1:])):
            print(f"{hit['id']:8} {hit['score']:6} {hit['title'][:90]}")
    else:
        print("usage: bank_db.py build | search <text>", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
