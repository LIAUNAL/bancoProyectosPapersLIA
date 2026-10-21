"""Build the LIA knowledge bank: one .md per article/project, clusters, links and the constellation.

Run: uv run --with scikit-learn --with numpy python tools/build_bank.py
Inputs: data/raw/sources.json, data/summaries/*.jsonl, data/taxonomy.md, data/hermes.json (optional),
        data/cluster_names.json (optional, overrides automatic cluster labels).
Outputs: articulos/, proyectos/, data/bank.json, dashboard/constelacion.html.
"""
from __future__ import annotations

import glob
import importlib.util
import json
import re
import unicodedata
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "docs"  # static site, served locally by bin/bancoLIA ui or tools/serve.sh
N_CLUSTERS = 12
MIN_YEAR = 2018  # articles published, or projects active (start or end), from this year on
SEED = 7

TOPICS = {}
for line in (ROOT / "data/taxonomy.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"(T\d\d) (.+?) \((.+)\)$", line.strip())
    if m:
        TOPICS[m.group(1)] = {"name": m.group(2), "scope": m.group(3)}

STOP = """de la el en y a los las del se por con para un una que su al lo como mas o es son sus este esta
these this that with from into based using use used the of and in for on to an by at as is are be we our
approach method methods proposed propose results data analysis system sistema propuesta resultados
mediante partir basado basada uso través""".split()


def slugify(text, n=60):
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:n].rstrip("-")


def load():
    src = json.loads((ROOT / "data/raw/sources.json").read_text(encoding="utf-8"))
    summ = {}
    for f in sorted(glob.glob(str(ROOT / "data/summaries/*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            if line.strip():
                rec = json.loads(line)
                summ[rec["id"]] = rec
    hermes_path = ROOT / "data/hermes.json"
    hermes = json.loads(hermes_path.read_text(encoding="utf-8")) if hermes_path.exists() else {}
    items = []
    for a in src["articles"]:
        items.append({**a, **summ.get(a["id"], {}), "kind": "articulo"})
    for p in src["projects"]:
        items.append({**p, **summ.get(p["id"], {}), "kind": "proyecto", "title": p["name"], "year": p["start"],
                      "hermes": hermes.get(p["id"], {})})
    extra_path = ROOT / "data/raw/hermes_extra.json"
    for p in json.loads(extra_path.read_text(encoding="utf-8")) if extra_path.exists() else []:
        items.append({**p, **summ.get(p["id"], {}), "kind": "proyecto", "title": p["name"], "year": p["start"],
                      "slug": f"{p['id']}-{p['start']}-{slugify(p['name'])}"})

    def in_window(i):
        years = [i.get("year"), i.get("end")] if i["kind"] == "proyecto" else [i.get("year")]
        return any(y and int(y) >= MIN_YEAR for y in years)
    items = [i for i in items if in_window(i)]
    missing = [i["id"] for i in items if i["id"] not in summ]
    if missing:
        raise SystemExit(f"missing summaries: {missing}")
    return items


def text_of(it):
    parts = [it["title"], it.get("aplicacion", ""), it.get("problema", ""), it.get("propuesta", ""),
             " ".join(it.get("palabras_clave", [])), " ".join(it.get("metodos", [])),
             " ".join(TOPICS[t]["name"] for t in it.get("temas", []) if t in TOPICS)]
    return " ".join(parts)


def cluster(items):
    vec = TfidfVectorizer(stop_words=STOP, min_df=2, max_df=0.5, ngram_range=(1, 2), sublinear_tf=True,
                          strip_accents="unicode")
    X = vec.fit_transform([text_of(i) for i in items])
    Z = normalize(TruncatedSVD(n_components=80, random_state=SEED).fit_transform(X))
    labels = KMeans(n_clusters=N_CLUSTERS, n_init=20, random_state=SEED).fit_predict(Z)
    terms = np.array(vec.get_feature_names_out())
    names_path = ROOT / "data/cluster_names.json"
    names = json.loads(names_path.read_text(encoding="utf-8")) if names_path.exists() else {}
    clusters = []
    for c in range(N_CLUSTERS):
        idx = np.where(labels == c)[0]
        top = terms[np.asarray(X[idx].mean(axis=0)).ravel().argsort()[::-1][:8]].tolist()
        topic_counts = {}
        for i in idx:
            for t in items[i].get("temas", [])[:1]:
                topic_counts[t] = topic_counts.get(t, 0) + 1
        cid = f"C{c + 1:02d}"
        clusters.append({"id": cid, "name": names.get(cid, " · ".join(top[:3])), "top_terms": top,
                         "topics": dict(sorted(topic_counts.items(), key=lambda kv: -kv[1])),
                         "members": [items[i]["id"] for i in idx]})
        for i in idx:
            items[i]["cluster"] = cid
    return Z, clusters


def relate(items, Z):
    """Project -> article links (shared content, publication within the project window) and
    each article's nearest earlier article (a candidate lineage)."""
    S = Z @ Z.T
    idx = {it["id"]: k for k, it in enumerate(items)}
    links = []
    for k, it in enumerate(items):
        it["relacionados"] = []
        order = [j for j in np.argsort(-S[k]) if j != k][:5]
        it["top5"] = [{"id": items[j]["id"], "sim": round(float(S[k, j]), 3)} for j in order]
    for k, it in enumerate(items):
        if it["kind"] != "proyecto":
            continue
        y0 = int(it.get("start") or 0)
        y1 = int(it.get("end") or y0 or 0)
        cands = []
        for j, other in enumerate(items):
            if other["kind"] != "articulo" or not other.get("year"):
                continue
            y = int(other["year"])
            if y0 and not (y0 <= y <= y1 + 3):
                continue
            cands.append((S[k, j], j))
        for sim, j in sorted(cands, reverse=True)[:4]:
            if sim >= 0.45:
                links.append({"from": it["id"], "to": items[j]["id"], "rel": "yields", "sim": round(float(sim), 3)})
    for k, it in enumerate(items):
        if it["kind"] != "articulo" or not it.get("year"):
            continue
        best = None
        for j, other in enumerate(items):
            if j == k or other["kind"] != "articulo" or not other.get("year"):
                continue
            if int(other["year"]) < int(it["year"]) and S[k, j] >= 0.75 and (best is None or S[k, j] > best[0]):
                best = (S[k, j], j)
        if best:
            links.append({"from": it["id"], "to": items[best[1]]["id"], "rel": "extends", "sim": round(float(best[0]), 3)})
    for l in links:
        items[idx[l["from"]]]["relacionados"].append((l["rel"], l["to"]))
        items[idx[l["to"]]]["relacionados"].append(({"yields": "derivado_de", "extends": "extendido_por"}[l["rel"]], l["from"]))
    return links


ESTADOS = {"Activo": "Activo", "Finalizado": "Finalizado", "porFinalizar": "Por finalizar", "Propuesto": "Propuesto",
           "Elegible": "Elegible (en evaluación)", "BancoFinanc": "En banco de financiables", "Ingresando": "Ingresando",
           "En_Legalizacion": "En legalización", "No_financiado": "No financiado",
           "No_cumplio_requisitos": "No cumplió requisitos"}

REL_ES = {"yields": "produjo", "extends": "extiende", "derivado_de": "derivado del proyecto",
          "extendido_por": "extendido por"}


def esc(s):
    return str(s or "").replace('"', "'")


def bullet(xs, empty="No reportado"):
    return "\n".join(f"- {x}" for x in xs) if xs else f"- {empty}"


def write_md(items, clusters):
    by_id = {i["id"]: i for i in items}
    cname = {c["id"]: c["name"] for c in clusters}
    for folder in ("articulos", "proyectos"):
        d = ROOT / folder
        d.mkdir(exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
    for it in items:
        temas = [f"{t} {TOPICS[t]['name']}" for t in it.get("temas", []) if t in TOPICS]
        rel = [f"- {REL_ES[r]}: [[{by_id[o]['slug']}]] — {by_id[o]['title']}" for r, o in it["relacionados"]]
        fm = [f"id: {it['id']}", f'titulo: "{esc(it["title"])}"', f"tipo: {it['kind']}",
              f"temas: [{', '.join(it.get('temas', []))}]", f'cluster: "{it["cluster"]} {esc(cname[it["cluster"]])}"',
              f"palabras_clave: [{', '.join(esc(k) for k in it.get('palabras_clave', []))}]",
              f"fuente_resumen: {it.get('fuente', '')}"]
        if it["kind"] == "articulo":
            fm += [f"anio: {it.get('year', '')}", f'revista: "{esc(it.get("journal_oa") or it.get("journal"))}"',
                   f"doi: {it.get('doi', '')}", f"citas_openalex: {it.get('cited_by', '')}",
                   f"fuentes: [{', '.join(sorted({it['src'], *it.get('also_in', [])}))}]"]
            authors = it.get("all_authors") or it.get("authors") or []
            body = [f"# {it['title']}", "",
                    f"**Autores:** {', '.join(authors)}  ",
                    f"**Revista:** {it.get('journal_oa') or it.get('journal')} ({it.get('year')})  ",
                    f"**DOI:** {('https://doi.org/' + it['doi']) if it.get('doi') else 'No disponible'}  ",
                    f"**Temas:** {'; '.join(temas)}  ", f"**Clúster:** {it['cluster']} {cname[it['cluster']]}", ""]
        else:
            h = it.get("hermes") or {}
            fm += [f"inicio: {it.get('start', '')}", f"fin: {it.get('end', '')}",
                   f"codigo_hermes: {h.get('codigo', '')}", f"quipu: {h.get('quipu', '')}",
                   f"estado_hermes: {h.get('estado', '')}", f"origen: {'Hermes' if it['id'].startswith('H') else 'CvLAC'}", f"tipo_proyecto: {it.get('type', '')}"]
            body = [f"# {it['title']}", "",
                    f"**Periodo:** {it.get('start') or '?'}–{it.get('end') or '?'}  ",
                    f"**Código Hermes:** {h.get('codigo') or 'Sin registro en Hermes (anterior al sistema o externo)'}"
                    + (f" · QUIPU {h['quipu']}" if h.get('quipu') else "") + "  ",
                    *([f"**Convocatoria (Hermes):** {h['convocatoria']}  "] if h.get('convocatoria') else []),
                    *([f"**Estado en Hermes:** {ESTADOS.get(h['estado'], h['estado'])}  "] if h.get('estado') else []),
                    *([f"**Nota Hermes:** {h['nota']}  "] if h.get('nota') else []),
                    f"**Financiador:** {it.get('financiador') or 'No reportado en CvLAC'}  ",
                    f"**Temas:** {'; '.join(temas)}  ", f"**Clúster:** {it['cluster']} {cname[it['cluster']]}", ""]
        body += ["## Aplicación", it.get("aplicacion", ""), "", "## Problema de investigación", it.get("problema", ""), "",
                 "## Propuesta o novedad", it.get("propuesta", ""), "", "## Resultados", it.get("resultados", ""), "",
                 "## Conclusiones principales", it.get("conclusiones", ""), ""]
        if it["kind"] == "proyecto":
            body += ["## Productos tecnológicos principales", bullet(it.get("productos_tecnologicos", [])), "",
                     "## Estrategia de apropiación social", it.get("apropiacion_social") or "No reportada en CvLAC", "",
                     "## Aliados", bullet(it.get("aliados", []) + (it.get("hermes") or {}).get("aliados", []),
                                          "No reportados en CvLAC (verificar en Hermes)"), ""]
        else:
            body += ["## Métodos", bullet(it.get("metodos", [])), ""]
        body += ["## Idea para trabajo futuro", it.get("idea_futura", ""), "",
                 "## Relacionados (similitud semántica)", "\n".join(rel) or "- Ninguno sobre el umbral", ""]
        if it["kind"] == "proyecto" and it.get("summary"):
            body += ["<details><summary>Resumen original (CvLAC)</summary>", "", it["summary"], "", "</details>", ""]
        if it["kind"] == "articulo" and it.get("abstract"):
            body += ["<details><summary>Abstract</summary>", "", it["abstract"], "", "</details>", ""]
        folder = "articulos" if it["kind"] == "articulo" else "proyectos"
        (ROOT / folder / f"{it['slug']}.md").write_text("---\n" + "\n".join(fm) + "\n---\n\n" + "\n".join(body),
                                                         encoding="utf-8")


def short(text, n):
    text = " ".join(str(text or "").split())
    return text if len(text) <= n else text[:n - 1].rsplit(" ", 1)[0] + "…"


def atlas(items, clusters, links):
    cname = {c["id"]: c["name"] for c in clusters}
    by_id = {it["id"]: it for it in items}

    def planet(pid, slot, orbit, label, detail, it, tip=None):
        return {"id": pid, "slot": slot, "orbit": orbit, "label": label[:90], "detail": detail,
                "tip": tip or short(f"{label}: {detail}", 90),
                "provenance": "CvLAC/OpenAlex" if it["kind"] == "articulo" else "CvLAC",
                "evidence": {"quote": (it.get("abstract") or it.get("summary") or "")[:420],
                             "origin": f"https://doi.org/{it['doi']}" if it.get("doi") else it["id"],
                             "retrieved": "2026-10-20"}}

    systems = []
    for it in items:
        is_p = it["kind"] == "proyecto"
        head = f"{it['id']} · {it.get('titulo_corto') or it['title']}"
        kind = "Proyecto" if is_p else "Artículo"
        ps = [planet("sun", "branch" if is_p else "sun", 0, head,
                     f"{kind} ({it.get('year') or '?'}). {it['title']}", it,
                     tip=short(f"{it['id']} · {kind} {it.get('year') or ''} · {it.get('titulo_corto') or it['title']}", 90)),
              planet("app", "application", 1, "Aplicación", it.get("aplicacion", ""), it),
              planet("prob", "problem", 1, "Problema", it.get("problema", ""), it),
              planet("nov", "novelty", 2, "Propuesta / novedad", it.get("propuesta", ""), it),
              planet("fam", "family", 2, f"{it['cluster']} {cname[it['cluster']]}", f"Clúster {it['cluster']}", it,
                     tip=f"Clúster {it['cluster']} · {cname[it['cluster']]}")]
        for t in it.get("temas", [])[:2]:
            if t in TOPICS:
                ps.append(planet(f"topic{t}", "topic_ai", 2, f"{t} {TOPICS[t]['name']}", TOPICS[t]["scope"], it,
                                 tip=f"Tema {t} · {TOPICS[t]['name']}"))
        ps += [planet("res", "result", 3, "Resultados", it.get("resultados", ""), it),
               planet("conc", "conclusion", 3, "Conclusiones", it.get("conclusiones", ""), it)]
        if is_p:
            prods = it.get("productos_tecnologicos") or []
            if prods:
                ps.append(planet("prod", "contribution", 3, "Productos tecnológicos", "; ".join(prods), it))
        label = f"{it['id']} · {(it.get('titulo_corto') or it['title'])[:28]}" if is_p else it["id"]
        h = it.get("hermes") or {}
        meta = {"kind": it["kind"], "title": it["title"],
                "years": f"{it.get('start') or '?'}–{it.get('end') or '?'}" if is_p else str(it.get("year") or ""),
                "venue": it.get("journal") or h.get("convocatoria") or "",
                "cluster": f"{it['cluster']} {cname[it['cluster']]}",
                "temas": [f"{t} {TOPICS[t]['name']}" for t in it.get("temas", []) if t in TOPICS],
                "estado": ESTADOS.get(h.get("estado"), h.get("estado") or ""), "hermes": h.get("codigo") or "",
                "aplicacion": it.get("aplicacion", ""), "problema": it.get("problema", ""),
                "propuesta": it.get("propuesta", ""), "resultados": it.get("resultados", ""),
                "conclusiones": it.get("conclusiones", ""),
                "productos": "; ".join(it.get("productos_tecnologicos") or []) if is_p else "",
                "aliados": "; ".join(it.get("aliados") or []) if is_p else "",
                "top5": [{"id": r["id"], "sim": r["sim"], "kind": by_id[r["id"]]["kind"],
                          "title": short(by_id[r["id"]].get("titulo_corto") or by_id[r["id"]]["title"], 110)}
                         for r in it.get("top5", [])]}
        systems.append({"id": it["id"], "title": label, "planets": ps, "meta": meta})
    alinks = [{"from_system": l["from"], "from": "nov", "to_system": l["to"], "to": "nov", "rel": l["rel"]}
              for l in links]
    # Sun -> planet spokes, so a lit system shows its own connections.
    alinks += [{"from_system": s["id"], "from": "sun", "to_system": s["id"], "to": p["id"], "rel": "about"}
               for s in systems for p in s["planets"] if p["id"] != "sun"]
    return {"systems": systems, "links": alinks}


# Build-time additions to the vendored viewer (vendor/papersmith stays byte-identical
# to upstream): no permanent labels, centred framing, a node's own short tooltip and camera controls.
VIEWER_PATCHES = [
    # No permanent system or cluster labels: names appear only in the hover tooltip and the side panel.
    ("let U=Yh(String(at.title||nt).slice(0,64),r_);U.position.copy(xt),Mt.add(U)", ""),
    ("yt.forEach(A=>{A.visible=dt===\"groups\"})", "yt.forEach(A=>{A.visible=!1})"),
    # Render at least one canvas pixel per CSS pixel, so a zoomed-out browser (devicePixelRatio < 1)
    # does not shrink points and lines to a faint quarter size.
    ("n.setPixelRatio(Math.min(window.devicePixelRatio||1,2))",
     "n.setPixelRatio(Math.min(Math.max(window.devicePixelRatio||1,1),2))"),
    # Fit the framing to the narrower field of view, so a tall container does not crop the sides.
    ("let at=$/Math.sin(H/2*Math.PI/180)*.8;",
     "let at=$/Math.sin(H/2*Math.PI/180)*.8/Math.min(1,(i.clientWidth||800)/(i.clientHeight||600));"),
    # Frame the initial view on the centroid of the nodes (the bounding-box centre sat off the mass).
    ("let J=k(m,_),X=J;",
     "let J=k(u.reduce((a,b)=>a.add(b),new L).multiplyScalar(1/Math.max(1,u.length)),_*.7),X=J;"),
    ("s.textContent=`${A.planet.label} [${A.planet.slot}]`",
     "s.textContent=A.planet.tip||`${A.planet.label} [${A.planet.slot}]`"),
    ("layout(){return dt}}}",
     "layout(){return dt},"
     "rotating(){return Q.autoRotate},"
     "rotate(o){Q.autoRotate=o===void 0?!Q.autoRotate:!!o;return Q.autoRotate},"
     "spin(a){Q.autoRotate=!1;let d=P.position.clone().sub(Q.target).applyAxisAngle(new L(0,0,1),a);"
     "P.position.copy(Q.target).add(d)},"
     "tilt(a){Q.autoRotate=!1;let d=P.position.clone().sub(Q.target),"
     "x=new L().crossVectors(d,new L(0,0,1)).normalize();d.applyAxisAngle(x,a);"
     "P.position.copy(Q.target).add(d)}}}"),
]


def viewer_bundle():
    bundle = (ROOT / "vendor/papersmith/atlas3d.bundle.js").read_text(encoding="utf-8")
    for old, new in VIEWER_PATCHES:
        if bundle.count(old) != 1:
            raise SystemExit(f"viewer patch no longer applies: {old[:40]}")
        bundle = bundle.replace(old, new)
    return bundle


def render(atlas_doc):
    spec = importlib.util.spec_from_file_location("render_atlas", ROOT / "vendor/papersmith/render_atlas.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.PAGE = (ROOT / "tools/constellation_template.html").read_text(encoding="utf-8")
    page = mod.render(atlas_doc, viewer=viewer_bundle(), title="Constelación LIA",
                      heading="Constelación LIA — artículos (soles dorados) y proyectos (soles verdes)")
    SITE.mkdir(exist_ok=True)
    (SITE / "constelacion.html").write_text(page, encoding="utf-8")


def main():
    items = load()
    Z, clusters = cluster(items)
    links = relate(items, Z)
    write_md(items, clusters)
    doc = atlas(items, clusters, links)
    render(doc)
    keep = ("id", "kind", "slug", "title", "titulo_corto", "year", "start", "end", "journal", "journal_oa", "doi",
            "cited_by", "temas", "cluster", "palabras_clave", "metodos", "aplicacion", "problema", "propuesta",
            "resultados", "conclusiones", "idea_futura", "productos_tecnologicos", "apropiacion_social", "aliados",
            "financiador", "hermes", "fuente", "relacionados", "top5", "objetivo_general")
    bank = {"topics": TOPICS, "clusters": clusters, "links": links,
            "items": [{k: it.get(k) for k in keep if k in it} for it in items]}
    (ROOT / "data/bank.json").write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding="utf-8")
    template = (ROOT / "tools/dashboard_template.html").read_text(encoding="utf-8")
    page = template.replace("@@BANK@@", json.dumps(bank, ensure_ascii=False).replace("<", "\\u003c"))
    (SITE / "index.html").write_text(
        '<!doctype html>\n<html lang="es">\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + page,
        encoding="utf-8")
    (SITE / "data").mkdir(exist_ok=True)
    (SITE / "data/bank.json").write_text(json.dumps(bank, ensure_ascii=False), encoding="utf-8")
    notice = (ROOT / "vendor/papersmith/THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    (SITE / "THIRD_PARTY_NOTICES.md").write_text(
        notice + "\n\nModified for Banco LIA: constelacion.html uses its own page template "
        "(tools/constellation_template.html) and adds node tooltips and camera controls to "
        "atlas3d.bundle.js at build time (VIEWER_PATCHES in tools/build_bank.py).\n", encoding="utf-8")
    (ROOT / "data/atlas.json").write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    print(f"items={len(items)} clusters={len(clusters)} links={len(links)}")
    for c in clusters:
        print(c["id"], len(c["members"]), c["name"], "|", ", ".join(c["top_terms"]), "|", c["topics"])


if __name__ == "__main__":
    main()
