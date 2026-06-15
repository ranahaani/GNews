import csv
import json
import os
import tempfile
import unittest

from gnews import GNews


SAMPLE_ARTICLES = [
    {
        "title": "AI Breakthrough",
        "description": "New model released.",
        "published date": "Mon, 10 Jun 2026 10:00:00 GMT",
        "url": "https://example.com/ai",
        "publisher": "TechNews",
    },
    {
        "title": "Stock Market Up",
        "description": "Markets rally.",
        "published date": "Mon, 10 Jun 2026 11:00:00 GMT",
        "url": "https://example.com/stocks",
        "publisher": "FinanceDaily",
    },
]


class TestExportToJSON(unittest.TestCase):
    def setUp(self):
        self.gnews = GNews()
        self.tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        self.tmp.close()

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.unlink(self.tmp.name)

    def test_saves_valid_json(self):
        self.gnews.save_to_json(SAMPLE_ARTICLES, self.tmp.name)
        with open(self.tmp.name) as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "AI Breakthrough")

    def test_json_contains_all_fields(self):
        self.gnews.save_to_json(SAMPLE_ARTICLES, self.tmp.name)
        with open(self.tmp.name) as f:
            data = json.load(f)
        for field in ("title", "description", "published date", "url", "publisher"):
            self.assertIn(field, data[0])

    def test_json_empty_list(self):
        self.gnews.save_to_json([], self.tmp.name)
        with open(self.tmp.name) as f:
            data = json.load(f)
        self.assertEqual(data, [])

    def test_json_returns_path(self):
        result = self.gnews.save_to_json(SAMPLE_ARTICLES, self.tmp.name)
        self.assertEqual(result, self.tmp.name)

    def test_json_invalid_path_raises(self):
        with self.assertRaises(Exception):
            self.gnews.save_to_json(SAMPLE_ARTICLES, "/nonexistent/dir/out.json")

    def test_json_pretty_printed(self):
        self.gnews.save_to_json(SAMPLE_ARTICLES, self.tmp.name)
        with open(self.tmp.name) as f:
            raw = f.read()
        self.assertIn("\n", raw)


class TestExportToCSV(unittest.TestCase):
    def setUp(self):
        self.gnews = GNews()
        self.tmp = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
        self.tmp.close()

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.unlink(self.tmp.name)

    def test_saves_valid_csv(self):
        self.gnews.save_to_csv(SAMPLE_ARTICLES, self.tmp.name)
        with open(self.tmp.name, newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["title"], "AI Breakthrough")

    def test_csv_header_matches_fields(self):
        self.gnews.save_to_csv(SAMPLE_ARTICLES, self.tmp.name)
        with open(self.tmp.name, newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
        for field in ("title", "description", "published date", "url", "publisher"):
            self.assertIn(field, header)

    def test_csv_empty_list(self):
        self.gnews.save_to_csv([], self.tmp.name)
        with open(self.tmp.name, newline="") as f:
            content = f.read()
        self.assertEqual(content.strip(), "")

    def test_csv_returns_path(self):
        result = self.gnews.save_to_csv(SAMPLE_ARTICLES, self.tmp.name)
        self.assertEqual(result, self.tmp.name)

    def test_csv_invalid_path_raises(self):
        with self.assertRaises(Exception):
            self.gnews.save_to_csv(SAMPLE_ARTICLES, "/nonexistent/dir/out.csv")

    def test_csv_second_row_correct(self):
        self.gnews.save_to_csv(SAMPLE_ARTICLES, self.tmp.name)
        with open(self.tmp.name, newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(rows[1]["publisher"], "FinanceDaily")
