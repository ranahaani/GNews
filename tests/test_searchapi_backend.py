import unittest
from unittest.mock import patch, MagicMock
from gnews.backends.searchapi import SearchApiBackend
from gnews.exceptions import InvalidConfigError, NetworkError


MOCK_RESPONSE = {
    "organic_results": [
        {
            "position": 1,
            "title": "Test Article One",
            "link": "https://example.com/article-1",
            "source": "Example News",
            "date": "2 hours ago",
            "iso_date": "2026-06-11T10:00:00Z",
            "snippet": "This is a test article snippet.",
            "favicon": "data:image/png;base64,abc123",
            "thumbnail": "data:image/jpeg;base64,xyz456",
        },
        {
            "position": 2,
            "title": "Test Article Two",
            "link": "https://example.com/article-2",
            "source": "Another Source",
            "date": "5 hours ago",
            "iso_date": "2026-06-11T07:00:00Z",
            "snippet": "Second article snippet.",
            "favicon": "",
            "thumbnail": "",
        },
    ]
}

MOCK_EMPTY_RESPONSE = {"organic_results": []}


class TestSearchApiBackendInit(unittest.TestCase):
    def test_raises_on_empty_key(self):
        with self.assertRaises(InvalidConfigError):
            SearchApiBackend("")

    def test_raises_on_none_key(self):
        with self.assertRaises(InvalidConfigError):
            SearchApiBackend(None)

    def test_valid_key(self):
        backend = SearchApiBackend("test-key-123")
        self.assertIsNotNone(backend)


class TestSearchApiMapArticle(unittest.TestCase):
    def setUp(self):
        self.backend = SearchApiBackend("test-key")
        self.raw = MOCK_RESPONSE["organic_results"][0]

    def test_maps_title(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["title"], "Test Article One")

    def test_maps_url(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["url"], "https://example.com/article-1")

    def test_maps_publisher(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["publisher"], "Example News")

    def test_maps_description_from_snippet(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["description"], "This is a test article snippet.")

    def test_maps_published_date(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["published date"], "2 hours ago")

    def test_maps_iso_date(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["iso_date"], "2026-06-11T10:00:00Z")

    def test_maps_thumbnail(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["thumbnail"], "data:image/jpeg;base64,xyz456")

    def test_maps_favicon(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["favicon"], "data:image/png;base64,abc123")

    def test_maps_rank(self):
        article = self.backend._map_article(self.raw)
        self.assertEqual(article["rank"], 1)

    def test_missing_optional_fields_default_to_empty(self):
        raw = {"position": 1, "title": "T", "link": "https://x.com", "source": "S",
               "date": "now", "iso_date": "2026-01-01T00:00:00Z"}
        article = self.backend._map_article(raw)
        self.assertEqual(article["description"], "")
        self.assertEqual(article["thumbnail"], "")
        self.assertEqual(article["favicon"], "")


class TestSearchApiGetNews(unittest.TestCase):
    def setUp(self):
        self.backend = SearchApiBackend("test-key")

    @patch("gnews.backends.searchapi.requests.get")
    def test_returns_list_of_articles(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_RESPONSE
        )
        results = self.backend.get_news("test query")
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    @patch("gnews.backends.searchapi.requests.get")
    def test_articles_have_required_keys(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_RESPONSE
        )
        results = self.backend.get_news("test query")
        required = {"title", "url", "publisher", "description", "published date",
                    "iso_date", "thumbnail", "favicon", "rank"}
        for article in results:
            for key in required:
                self.assertIn(key, article, f"Missing key: {key}")

    @patch("gnews.backends.searchapi.requests.get")
    def test_empty_results(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_EMPTY_RESPONSE
        )
        results = self.backend.get_news("noresults")
        self.assertEqual(results, [])

    @patch("gnews.backends.searchapi.requests.get")
    def test_raises_network_error_on_non_200(self, mock_get):
        mock_get.return_value = MagicMock(status_code=401, text="Unauthorized")
        with self.assertRaises(NetworkError):
            self.backend.get_news("test")

    @patch("gnews.backends.searchapi.requests.get")
    def test_raises_network_error_on_exception(self, mock_get):
        mock_get.side_effect = Exception("connection refused")
        with self.assertRaises(NetworkError):
            self.backend.get_news("test")

    @patch("gnews.backends.searchapi.requests.get")
    def test_respects_max_results(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_RESPONSE
        )
        results = self.backend.get_news("test", max_results=1)
        self.assertLessEqual(len(results), 1)

    @patch("gnews.backends.searchapi.requests.get")
    def test_sends_correct_params(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_EMPTY_RESPONSE
        )
        self.backend.get_news("AI news", language="fr", country="FR", page=2)
        call_params = mock_get.call_args[1]["params"]
        self.assertEqual(call_params["q"], "AI news")
        self.assertEqual(call_params["hl"], "fr")
        self.assertEqual(call_params["gl"], "FR")
        self.assertEqual(call_params["page"], 2)
        self.assertEqual(call_params["engine"], "google_news")

    @patch("gnews.backends.searchapi.requests.get")
    def test_request_has_timeout(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_EMPTY_RESPONSE
        )
        self.backend.get_news("test")
        _, kwargs = mock_get.call_args
        self.assertEqual(kwargs.get("timeout"), 10)

    @patch("gnews.backends.searchapi.requests.get")
    def test_sends_date_range_when_provided(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: MOCK_EMPTY_RESPONSE
        )
        self.backend.get_news("test", start_date="2026-01-01", end_date="2026-06-01")
        call_params = mock_get.call_args[1]["params"]
        self.assertIn("tbs", call_params)


if __name__ == "__main__":
    unittest.main()
