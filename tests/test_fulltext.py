import unittest
from unittest.mock import patch, MagicMock

from gnews import GNews


MOCK_HTML = b"""
<html><body>
<article>
<h1>AI Transforms Healthcare</h1>
<p>Artificial intelligence is revolutionizing how doctors diagnose diseases.</p>
<p>New research shows that AI models outperform radiologists in detecting cancer.</p>
<p>The study was conducted across 50 hospitals with 10,000 patients.</p>
</article>
</body></html>
"""


class TestGetFullArticle(unittest.TestCase):
    def setUp(self):
        self.gnews = GNews()
        self.url = "https://example.com/ai-healthcare"

    @patch("trafilatura.fetch_url", return_value=MOCK_HTML)
    @patch("trafilatura.extract", return_value="AI Transforms Healthcare\nArtificial intelligence is revolutionizing...")
    def test_returns_dict(self, mock_extract, mock_fetch):
        result = self.gnews.get_full_article(self.url)
        self.assertIsInstance(result, dict)

    @patch("trafilatura.fetch_url", return_value=MOCK_HTML)
    @patch("trafilatura.extract", return_value="AI Transforms Healthcare\nArtificial intelligence is revolutionizing...")
    def test_result_has_required_keys(self, mock_extract, mock_fetch):
        result = self.gnews.get_full_article(self.url)
        for key in ("text", "url"):
            self.assertIn(key, result)

    @patch("trafilatura.fetch_url", return_value=MOCK_HTML)
    @patch("trafilatura.extract", return_value="AI Transforms Healthcare\nArtificial intelligence is revolutionizing...")
    def test_result_url_matches_input(self, mock_extract, mock_fetch):
        result = self.gnews.get_full_article(self.url)
        self.assertEqual(result["url"], self.url)

    @patch("trafilatura.fetch_url", return_value=MOCK_HTML)
    @patch("trafilatura.extract", return_value="AI Transforms Healthcare")
    def test_result_text_not_empty(self, mock_extract, mock_fetch):
        result = self.gnews.get_full_article(self.url)
        self.assertTrue(len(result["text"]) > 0)

    @patch("trafilatura.fetch_url", return_value=None)
    def test_raises_network_error_when_download_fails(self, mock_fetch):
        from gnews.exceptions import NetworkError
        with self.assertRaises(NetworkError):
            self.gnews.get_full_article(self.url)

    @patch("trafilatura.fetch_url", return_value=MOCK_HTML)
    @patch("trafilatura.extract", return_value=None)
    def test_raises_network_error_when_extraction_fails(self, mock_extract, mock_fetch):
        from gnews.exceptions import NetworkError
        with self.assertRaises(NetworkError):
            self.gnews.get_full_article(self.url)

    def test_raises_import_error_when_trafilatura_missing(self):
        import sys
        trafilatura_backup = sys.modules.get("trafilatura")
        sys.modules["trafilatura"] = None
        try:
            with self.assertRaises(ImportError) as ctx:
                self.gnews.get_full_article(self.url)
            self.assertIn("pip install gnews[fulltext]", str(ctx.exception))
        finally:
            if trafilatura_backup is not None:
                sys.modules["trafilatura"] = trafilatura_backup
            else:
                del sys.modules["trafilatura"]

    @patch("trafilatura.fetch_url", return_value=MOCK_HTML)
    @patch("trafilatura.extract", return_value="Some article text")
    def test_fetch_called_with_correct_url(self, mock_extract, mock_fetch):
        self.gnews.get_full_article(self.url)
        mock_fetch.call_args[0][0] == self.url
