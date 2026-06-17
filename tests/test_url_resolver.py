import unittest
from unittest.mock import patch, MagicMock, call

GOOGLE_NEWS_URL = "https://news.google.com/rss/articles/CBMirwFBVV95cUxQ"
REAL_URL = "https://www.washingtonpost.com/politics/2026/06/15/article"
PROXY = {"https": "http://myproxy.example.com:8080", "http": "http://myproxy.example.com:8080"}


class TestResolveUrl(unittest.TestCase):
    def test_non_google_url_returned_unchanged(self):
        from gnews.utils.utils import resolve_url
        url = "https://bbc.com/news/article-123"
        self.assertEqual(resolve_url(url), url)

    def test_returns_original_when_playwright_missing(self):
        from gnews.utils.utils import resolve_url
        import sys
        backup = sys.modules.get("playwright")
        sys.modules["playwright"] = None
        try:
            result = resolve_url(GOOGLE_NEWS_URL)
            self.assertEqual(result, GOOGLE_NEWS_URL)
        finally:
            if backup is not None:
                sys.modules["playwright"] = backup
            else:
                del sys.modules["playwright"]

    @patch("gnews.utils.utils._resolve_with_playwright", return_value=REAL_URL)
    def test_google_url_resolved_via_playwright(self, mock_resolve):
        from gnews.utils.utils import resolve_url
        result = resolve_url(GOOGLE_NEWS_URL)
        self.assertEqual(result, REAL_URL)
        mock_resolve.assert_called_once_with(GOOGLE_NEWS_URL, proxies=None)

    @patch("gnews.utils.utils._resolve_with_playwright", return_value=REAL_URL)
    def test_proxy_forwarded_to_playwright(self, mock_resolve):
        from gnews.utils.utils import resolve_url
        result = resolve_url(GOOGLE_NEWS_URL, proxies=PROXY)
        self.assertEqual(result, REAL_URL)
        mock_resolve.assert_called_once_with(GOOGLE_NEWS_URL, proxies=PROXY)

    @patch("gnews.utils.utils._resolve_with_playwright", return_value=None)
    def test_falls_back_to_original_on_failure(self, mock_resolve):
        from gnews.utils.utils import resolve_url
        result = resolve_url(GOOGLE_NEWS_URL)
        self.assertEqual(result, GOOGLE_NEWS_URL)

    @patch("gnews.utils.utils._resolve_with_playwright", return_value=GOOGLE_NEWS_URL)
    def test_falls_back_if_still_google_url(self, mock_resolve):
        from gnews.utils.utils import resolve_url
        result = resolve_url(GOOGLE_NEWS_URL)
        self.assertEqual(result, GOOGLE_NEWS_URL)


class TestResolveWithPlaywright(unittest.TestCase):
    def test_returns_none_on_timeout(self):
        from gnews.utils.utils import _resolve_with_playwright

        mock_pw = MagicMock()
        mock_pw.return_value.__enter__.return_value.chromium.launch.side_effect = Exception("Timeout")

        with patch("playwright.sync_api.sync_playwright", mock_pw):
            result = _resolve_with_playwright(GOOGLE_NEWS_URL)
            self.assertIsNone(result)

    def test_returns_real_url_on_success(self):
        from gnews.utils.utils import _resolve_with_playwright

        mock_page = MagicMock()
        mock_page.url = REAL_URL
        mock_context = MagicMock()
        mock_context.new_page.return_value = mock_page
        mock_browser = MagicMock()
        mock_browser.new_context.return_value = mock_context

        with patch("playwright.sync_api.sync_playwright") as mock_pw:
            mock_instance = MagicMock()
            mock_instance.chromium.launch.return_value = mock_browser
            mock_pw.return_value.__enter__.return_value = mock_instance
            result = _resolve_with_playwright(GOOGLE_NEWS_URL)
            self.assertEqual(result, REAL_URL)

    def test_proxy_passed_to_playwright_context(self):
        from gnews.utils.utils import _resolve_with_playwright

        mock_page = MagicMock()
        mock_page.url = REAL_URL
        mock_context = MagicMock()
        mock_context.new_page.return_value = mock_page
        mock_browser = MagicMock()
        mock_browser.new_context.return_value = mock_context

        with patch("playwright.sync_api.sync_playwright") as mock_pw:
            mock_instance = MagicMock()
            mock_instance.chromium.launch.return_value = mock_browser
            mock_pw.return_value.__enter__.return_value = mock_instance

            _resolve_with_playwright(GOOGLE_NEWS_URL, proxies=PROXY)

            mock_browser.new_context.assert_called_once()
            kwargs = mock_browser.new_context.call_args.kwargs
            self.assertEqual(kwargs["proxy"], {"server": "http://myproxy.example.com:8080"})

    def test_no_proxy_passes_none_to_context(self):
        from gnews.utils.utils import _resolve_with_playwright

        mock_page = MagicMock()
        mock_page.url = REAL_URL
        mock_context = MagicMock()
        mock_context.new_page.return_value = mock_page
        mock_browser = MagicMock()
        mock_browser.new_context.return_value = mock_context

        with patch("playwright.sync_api.sync_playwright") as mock_pw:
            mock_instance = MagicMock()
            mock_instance.chromium.launch.return_value = mock_browser
            mock_pw.return_value.__enter__.return_value = mock_instance

            _resolve_with_playwright(GOOGLE_NEWS_URL)

            kwargs = mock_browser.new_context.call_args.kwargs
            self.assertIsNone(kwargs["proxy"])

    def test_http_only_proxy_used_as_fallback(self):
        from gnews.utils.utils import _resolve_with_playwright

        mock_page = MagicMock()
        mock_page.url = REAL_URL
        mock_context = MagicMock()
        mock_context.new_page.return_value = mock_page
        mock_browser = MagicMock()
        mock_browser.new_context.return_value = mock_context

        with patch("playwright.sync_api.sync_playwright") as mock_pw:
            mock_instance = MagicMock()
            mock_instance.chromium.launch.return_value = mock_browser
            mock_pw.return_value.__enter__.return_value = mock_instance

            _resolve_with_playwright(GOOGLE_NEWS_URL, proxies={"http": "http://proxy:3128"})

            kwargs = mock_browser.new_context.call_args.kwargs
            self.assertEqual(kwargs["proxy"], {"server": "http://proxy:3128"})
