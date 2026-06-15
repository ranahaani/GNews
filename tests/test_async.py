import asyncio
import unittest
from unittest.mock import AsyncMock, patch, MagicMock

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


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


class TestAsyncGetNews(unittest.TestCase):
    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_async_get_news_returns_list(self, mock):
        g = GNews(max_results=2)
        result = run(g.get_news_async("AI"))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_async_get_news_title(self, mock):
        g = GNews(max_results=2)
        result = run(g.get_news_async("AI"))
        self.assertEqual(result[0]["title"], "AI Breakthrough")

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_async_get_news_passes_query(self, mock):
        g = GNews(max_results=2)
        run(g.get_news_async("Python"))
        mock.assert_called_once_with("Python", 1)

    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_async_get_news_passes_page(self, mock):
        g = GNews(max_results=2)
        run(g.get_news_async("Python", page=3))
        mock.assert_called_once_with("Python", 3)


class TestAsyncGetTopNews(unittest.TestCase):
    @patch("gnews.GNews.get_top_news", return_value=SAMPLE_ARTICLES)
    def test_async_get_top_news_returns_list(self, mock):
        g = GNews(max_results=2)
        result = run(g.get_top_news_async())
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

    @patch("gnews.GNews.get_top_news", return_value=SAMPLE_ARTICLES)
    def test_async_get_top_news_calls_sync(self, mock):
        g = GNews()
        run(g.get_top_news_async())
        mock.assert_called_once()


class TestAsyncGetNewsByTopic(unittest.TestCase):
    @patch("gnews.GNews.get_news_by_topic", return_value=SAMPLE_ARTICLES)
    def test_returns_list(self, mock):
        g = GNews()
        result = run(g.get_news_by_topic_async("TECHNOLOGY"))
        self.assertIsInstance(result, list)

    @patch("gnews.GNews.get_news_by_topic", return_value=SAMPLE_ARTICLES)
    def test_passes_topic(self, mock):
        g = GNews()
        run(g.get_news_by_topic_async("BUSINESS"))
        mock.assert_called_once_with("BUSINESS")


class TestAsyncGetNewsByLocation(unittest.TestCase):
    @patch("gnews.GNews.get_news_by_location", return_value=SAMPLE_ARTICLES)
    def test_returns_list(self, mock):
        g = GNews()
        result = run(g.get_news_by_location_async("Pakistan"))
        self.assertIsInstance(result, list)

    @patch("gnews.GNews.get_news_by_location", return_value=SAMPLE_ARTICLES)
    def test_passes_location(self, mock):
        g = GNews()
        run(g.get_news_by_location_async("India"))
        mock.assert_called_once_with("India")


class TestAsyncGetNewsBySite(unittest.TestCase):
    @patch("gnews.GNews.get_news_by_site", return_value=SAMPLE_ARTICLES)
    def test_returns_list(self, mock):
        g = GNews()
        result = run(g.get_news_by_site_async("bbc.com"))
        self.assertIsInstance(result, list)

    @patch("gnews.GNews.get_news_by_site", return_value=SAMPLE_ARTICLES)
    def test_passes_site(self, mock):
        g = GNews()
        run(g.get_news_by_site_async("cnn.com"))
        mock.assert_called_once_with("cnn.com")


class TestAsyncConcurrent(unittest.TestCase):
    @patch("gnews.GNews.get_news", return_value=SAMPLE_ARTICLES)
    def test_gather_multiple_queries(self, mock):
        g = GNews()
        results = run(asyncio.gather(
            g.get_news_async("AI"),
            g.get_news_async("Python"),
            g.get_news_async("Pakistan"),
        ))
        self.assertEqual(len(results), 3)
        for r in results:
            self.assertIsInstance(r, list)
