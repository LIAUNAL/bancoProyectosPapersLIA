"""Tests for tools/bank_db.py, the SQLite FTS5 index behind the Banco LIA MCP server.

Run: python3 -m unittest discover -s tests
"""
import json
import os
import sqlite3
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import bank_db  # noqa: E402

BANK = {
    "topics": {"T01": {"name": "Interfaces cerebro-computador", "scope": "EEG, BCI"},
               "T02": {"name": "Visión por computador", "scope": "imágenes, video"}},
    "clusters": [{"id": "C01", "name": "Decodificación EEG", "top_terms": ["eeg"], "topics": {"T01": 2}, "members": ["A001", "P001"]},
                 {"id": "C02", "name": "Visión con drones", "top_terms": ["uav"], "topics": {"T02": 1}, "members": ["A002"]}],
    "links": [{"from": "P001", "to": "A001", "rel": "yields", "sim": 0.5}],
    "items": [
        {"id": "A001", "kind": "articulo", "slug": "A001-2024-eeg", "title": "Decodificación de imaginación motora con EEG",
         "year": "2024", "journal": "Sensors", "doi": "10.1/a1", "temas": ["T01"], "cluster": "C01",
         "palabras_clave": ["imaginación motora", "EEG"], "metodos": ["redes convolucionales"],
         "aplicacion": "Interfaces cerebro-computador", "problema": "Baja precisión entre sujetos",
         "propuesta": "Red con atención", "resultados": "Precisión de 85 %", "conclusiones": "Mejora la transferencia",
         "idea_futura": "Probar en pacientes", "top5": [{"id": "A002", "sim": 0.2}]},
        {"id": "A002", "kind": "articulo", "slug": "A002-2021-uav", "title": "Detección de objetos desde vehículos aéreos",
         "year": "2021", "journal": "Drones", "doi": "10.1/a2", "temas": ["T02"], "cluster": "C02",
         "palabras_clave": ["UAV", "detección"], "metodos": ["YOLO"], "aplicacion": "Vigilancia urbana",
         "problema": "Objetos pequeños", "propuesta": "Detector ligero", "resultados": "mAP 0.7",
         "conclusiones": "Viable en tiempo real", "idea_futura": "Seguimiento multiobjeto", "top5": []},
        {"id": "P001", "kind": "proyecto", "slug": "P001-2023-bci", "title": "Sistema BCI para rehabilitación",
         "year": "2023", "start": "2023", "end": "2025", "temas": ["T01"], "cluster": "C01",
         "palabras_clave": ["rehabilitación"], "aplicacion": "Rehabilitación motora", "problema": "Terapias costosas",
         "propuesta": "Neurorretroalimentación", "resultados": "Prototipo validado", "conclusiones": "",
         "idea_futura": "", "productos_tecnologicos": ["Prototipo BCI portable"], "aliados": ["Hospital de Caldas"],
         "financiador": "Minciencias", "hermes": {"codigo": "57661"}, "top5": [{"id": "A001", "sim": 0.6}]},
    ],
}


class BankDbTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.bank = self.tmp / "data" / "bank.json"
        self.bank.parent.mkdir()
        self.bank.write_text(json.dumps(BANK), encoding="utf-8")
        (self.tmp / "articulos").mkdir()
        (self.tmp / "proyectos").mkdir()
        (self.tmp / "articulos" / "A001-2024-eeg.md").write_text("# A001 ficha\n", encoding="utf-8")
        (self.tmp / "proyectos" / "P001-2023-bci.md").write_text("# P001 ficha\n", encoding="utf-8")
        self.db = self.tmp / "data" / "bank.db"
        self.bank_db = bank_db.Bank(self.bank, self.db)

    def test_build_creates_fts5_index_with_every_item(self):
        self.bank_db.search("EEG")
        con = sqlite3.connect(self.db)
        self.assertEqual(con.execute("select count(*) from items").fetchone()[0], 3)
        self.assertEqual(con.execute("select count(*) from items_fts").fetchone()[0], 3)

    def test_search_ranks_by_relevance_and_ignores_accents(self):
        hits = self.bank_db.search("imaginacion motora")
        self.assertEqual(hits[0]["id"], "A001")
        self.assertIn("snippet", hits[0])

    def test_search_tolerates_fts_syntax_characters(self):
        self.assertEqual(self.bank_db.search('"UAV" AND (drones* -'), self.bank_db.search("UAV drones"))
        self.assertEqual(self.bank_db.search("UAV drones")[0]["id"], "A002")

    def test_search_ignores_stopwords(self):
        # "de" appears in A001's title; only the content words should decide the match.
        self.assertEqual([h["id"] for h in self.bank_db.search("detección de objetos")], ["A002"])
        self.assertEqual(self.bank_db.search("de la por"), [])

    def test_search_filters_kind_cluster_topic_and_year(self):
        self.assertEqual([h["id"] for h in self.bank_db.search("rehabilitación EEG", kind="proyecto")], ["P001"])
        self.assertEqual({h["id"] for h in self.bank_db.search("EEG rehabilitación", cluster="C01")}, {"A001", "P001"})
        self.assertEqual([h["id"] for h in self.bank_db.search("detección EEG", topic="T02")], ["A002"])
        self.assertEqual({h["id"] for h in self.bank_db.search("EEG rehabilitación detección", year_from=2023)}, {"A001", "P001"})

    def test_search_without_query_lists_filtered_items(self):
        self.assertEqual({h["id"] for h in self.bank_db.search("", cluster="C01")}, {"A001", "P001"})

    def test_get_item_returns_record_and_markdown(self):
        item = self.bank_db.get_item("a001")
        self.assertEqual(item["doi"], "10.1/a1")
        self.assertEqual(item["markdown"], "# A001 ficha\n")
        self.assertEqual(item["topic_names"], ["Interfaces cerebro-computador"])
        self.assertIsNone(self.bank_db.get_item("X999"))

    def test_related_items_merges_links_similarity_and_cluster(self):
        rel = self.bank_db.related_items("P001")
        self.assertEqual(rel["links"], [{"id": "A001", "rel": "yields", "direction": "out", "title": rel["links"][0]["title"]}])
        self.assertEqual(rel["similar"][0]["id"], "A001")
        self.assertEqual([c["id"] for c in rel["same_cluster"]], ["A001"])
        self.assertEqual(self.bank_db.related_items("A001")["links"][0]["direction"], "in")

    def test_lab_capabilities_aggregates_allies_funders_products_and_methods(self):
        cap = self.bank_db.lab_capabilities("rehabilitación EEG", match="any")
        self.assertEqual(cap["items"], 2)
        self.assertEqual(cap["aliados"], [{"value": "Hospital de Caldas", "items": ["P001"]}])
        self.assertEqual(cap["financiadores"], [{"value": "Minciencias", "items": ["P001"]}])
        self.assertEqual(cap["productos_tecnologicos"][0]["value"], "Prototipo BCI portable")
        self.assertEqual(cap["metodos"][0]["value"], "redes convolucionales")
        self.assertEqual(cap["years"], [2023, 2024])

    def test_search_match_all_requires_every_word(self):
        self.assertEqual({h["id"] for h in self.bank_db.search("EEG rehabilitación")}, {"A001", "P001"})
        self.assertEqual(self.bank_db.search("EEG rehabilitación", match="all"), [])
        self.assertEqual([h["id"] for h in self.bank_db.search("imaginación EEG", match="all")], ["A001"])

    def test_lab_capabilities_requires_every_word_by_default(self):
        self.assertEqual(self.bank_db.lab_capabilities("rehabilitación EEG")["items"], 0)
        self.assertEqual(self.bank_db.lab_capabilities("prototipo BCI")["aliados"][0]["items"], ["P001"])

    def test_taxonomy_lists_topics_and_clusters_with_counts(self):
        tax = self.bank_db.taxonomy()
        self.assertEqual(tax["topics"][0], {"id": "T01", "name": "Interfaces cerebro-computador", "scope": "EEG, BCI", "items": 2})
        self.assertEqual(tax["clusters"][1]["items"], 1)

    def test_export_copies_markdown_into_existing_directory(self):
        dest = self.tmp / "insumos" / "background"
        dest.mkdir(parents=True)
        out = self.bank_db.export(["A001", "P001", "A002", "Z9"], str(dest))
        self.assertEqual(sorted(Path(p).name for p in out["written"]),
                         ["banco-lia-A001-2024-eeg.md", "banco-lia-P001-2023-bci.md"])
        self.assertEqual(out["missing"], ["A002", "Z9"])
        self.assertEqual((dest / "banco-lia-A001-2024-eeg.md").read_text(encoding="utf-8"), "# A001 ficha\n")
        with self.assertRaises(ValueError):
            self.bank_db.export(["A001"], str(self.tmp / "no-such-dir"))

    def test_default_paths_use_the_checkout_data_when_present(self):
        tools = self.tmp / "tools"
        tools.mkdir()
        self.assertEqual(bank_db.default_paths(tools), (self.bank, self.db))

    def test_default_paths_in_an_installed_wheel_read_packaged_data_and_cache_the_index(self):
        pkg = self.tmp / "site-packages" / "banco_lia"
        (pkg / "data").mkdir(parents=True)
        (pkg / "data" / "bank.json").write_text("{}", encoding="utf-8")
        cache = self.tmp / "cache"
        os.environ["XDG_CACHE_HOME"] = str(cache)
        try:
            self.assertEqual(bank_db.default_paths(pkg), (pkg / "data" / "bank.json", cache / "banco-lia" / "bank.db"))
        finally:
            del os.environ["XDG_CACHE_HOME"]

    def test_index_rebuilds_when_bank_json_changes(self):
        self.assertEqual(len(self.bank_db.search("", kind="articulo")), 2)
        changed = dict(BANK, items=BANK["items"][:1])
        self.bank.write_text(json.dumps(changed), encoding="utf-8")
        later = time.time() + 5
        os.utime(self.bank, (later, later))
        self.assertEqual(len(bank_db.Bank(self.bank, self.db).search("", kind="articulo")), 1)


if __name__ == "__main__":
    unittest.main()
