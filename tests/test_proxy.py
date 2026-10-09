import os
import unittest
from unittest.mock import patch, MagicMock

from gnews import GNews
from gnews.exceptions import InvalidConfigError, NetworkError

PROXY_URL = "http://user:pass@proxy.example.com:8080"


class TestProxyConfig(unittest.TestCase):
    def setUp(self):
        self._env = patch.dict(os.environ, {}, clear=False)
        self._env.start()
        os.environ.pop("GNEWS_PROXY_URL", None)

    def tearDown(self):
        self._env.stop()

    def test_no_proxy_by_default(self):
        self.assertIsNone(GNews().proxy)

    def test_dict_proxy_unchanged(self):
        d = {"https": PROXY_URL}
        self.assertEqual(GNews(proxy=d).proxy, d)

    def test_string_proxy_expanded(self):
        self.assertEqual(GNews(proxy=PROXY_URL).proxy, {"http": PROXY_URL, "https": PROXY_URL})

    def test_env_var_fallback(self):
        os.environ["GNEWS_PROXY_URL"] = PROXY_URL
        self.assertEqual(GNews().proxy, {"http": PROXY_URL, "https": PROXY_URL})

    def test_explicit_proxy_beats_env(self):
        os.environ["GNEWS_PROXY_URL"] = "http://other:1"
        self.assertEqual(GNews(proxy=PROXY_URL).proxy["https"], PROXY_URL)

    def test_empty_env_var_ignored(self):
        os.environ["GNEWS_PROXY_URL"] = ""
        self.assertIsNone(GNews().proxy)

    def test_string_without_scheme_rejected(self):
        with self.assertRaises(InvalidConfigError):
            GNews(proxy="proxy.example.com:8080")

    def test_bad_type_rejected(self):
        with self.assertRaises(InvalidConfigError):
            GNews(proxy=8080)

    def test_feed_fetch_uses_proxy_handler(self):
        g = GNews(proxy=PROXY_URL)
        with patch("gnews.gnews.feedparser.parse") as parse:
            g._fetch_feed("https://news.google.com/rss")
        handler = parse.call_args.kwargs["handlers"][0]
        self.assertEqual(handler.proxies["https"], PROXY_URL)


class TestFullArticleProxy(unittest.TestCase):
    def setUp(self):
        os.environ.pop("GNEWS_PROXY_URL", None)

    @patch("trafilatura.extract", return_value="body text")
    @patch("trafilatura.fetch_url")
    @patch("requests.get")
    def test_full_article_routed_through_proxy(self, req_get, fetch_url, extract):
        req_get.return_value = MagicMock(status_code=200, text="<html>x</html>")
        result = GNews(proxy=PROXY_URL).get_full_article("https://example.com/a")
        fetch_url.assert_not_called()
        self.assertEqual(req_get.call_args.kwargs["proxies"]["https"], PROXY_URL)
        self.assertEqual(result["text"], "body text")

    @patch("trafilatura.extract", return_value="body text")
    @patch("trafilatura.fetch_url", return_value="<html>x</html>")
    @patch("requests.get")
    def test_full_article_without_proxy_uses_trafilatura(self, req_get, fetch_url, extract):
        GNews().get_full_article("https://example.com/a")
        req_get.assert_not_called()
        fetch_url.assert_called_once()

    @patch("requests.get")
    def test_full_article_proxy_error_raises_network_error(self, req_get):
        import requests
        req_get.side_effect = requests.ConnectionError("boom")
        with self.assertRaises(NetworkError):
            GNews(proxy=PROXY_URL).get_full_article("https://example.com/a")


if __name__ == "__main__":
    unittest.main()
