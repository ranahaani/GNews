import json
import sys
import unittest
from io import StringIO
from unittest.mock import patch

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


def run_cli(*args):
    from gnews.cli import main
    with patch("sys.argv", ["gnews", *args]):
        buf = StringIO()
        with patch("sys.stdout", buf):
            try:
                main()
            except SystemExit:
                pass
        return buf.getvalue()


class TestCLISearch(unittest.TestCase):
    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_search_outputs_titles(self, mock):
        out = run_cli("search", "AI")
        self.assertIn("AI Breakthrough", out)

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_search_json_flag_outputs_valid_json(self, mock):
        out = run_cli("search", "AI", "--json")
        data = json.loads(out)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "AI Breakthrough")

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_search_max_results_flag(self, mock):
        run_cli("search", "AI", "--max", "5")
        mock.assert_called_once()

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_search_lang_flag(self, mock):
        run_cli("search", "AI", "--lang", "fr")
        self.assertEqual(mock.call_args[0][0], "AI")

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_search_country_flag(self, mock):
        run_cli("search", "AI", "--country", "GB")
        self.assertIn("AI Breakthrough", run_cli("search", "AI"))


class TestCLITop(unittest.TestCase):
    @patch("gnews.GNews.get_top_news", return_value=SAMPLE_ARTICLES)
    def test_top_outputs_titles(self, mock):
        out = run_cli("top")
        self.assertIn("AI Breakthrough", out)

    @patch("gnews.GNews.get_top_news", return_value=SAMPLE_ARTICLES)
    def test_top_json_flag(self, mock):
        out = run_cli("top", "--json")
        data = json.loads(out)
        self.assertEqual(data[0]["title"], "AI Breakthrough")


class TestCLITopic(unittest.TestCase):
    @patch("gnews.GNews.get_news_by_topic", return_value=SAMPLE_ARTICLES)
    def test_topic_outputs_titles(self, mock):
        out = run_cli("topic", "BUSINESS")
        self.assertIn("AI Breakthrough", out)

    @patch("gnews.GNews.get_news_by_topic", return_value=SAMPLE_ARTICLES)
    def test_topic_json_flag(self, mock):
        out = run_cli("topic", "TECHNOLOGY", "--json")
        data = json.loads(out)
        self.assertEqual(len(data), 2)


class TestCLISite(unittest.TestCase):
    @patch("gnews.GNews.get_news_by_site", return_value=SAMPLE_ARTICLES)
    def test_site_outputs_titles(self, mock):
        out = run_cli("site", "cnn.com")
        self.assertIn("AI Breakthrough", out)

    @patch("gnews.GNews.get_news_by_site", return_value=SAMPLE_ARTICLES)
    def test_site_json_flag(self, mock):
        out = run_cli("site", "bbc.com", "--json")
        data = json.loads(out)
        self.assertEqual(data[1]["publisher"], "FinanceDaily")


class TestCLILocation(unittest.TestCase):
    @patch("gnews.GNews.get_news_by_location", return_value=SAMPLE_ARTICLES)
    def test_location_outputs_titles(self, mock):
        out = run_cli("location", "India")
        self.assertIn("AI Breakthrough", out)

    @patch("gnews.GNews.get_news_by_location", return_value=SAMPLE_ARTICLES)
    def test_location_json_flag(self, mock):
        out = run_cli("location", "Pakistan", "--json")
        data = json.loads(out)
        self.assertEqual(len(data), 2)
