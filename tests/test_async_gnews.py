import unittest

from gnews import GNewsAsync


class TestGNewsAsync(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.gnews_context = GNewsAsync()
        self.gnews = await self.gnews_context.__aenter__()
        self.addAsyncCleanup(self.gnews_context.__aexit__, None, None, None)

    async def test_get_news(self):
        key = "Google"
        news_articles = await self.gnews.get_news(key)
        self.assertIsInstance(news_articles, list)
        self.assertGreater(len(news_articles), 0)

    async def test_get_top_news(self):
        top_news_articles = await self.gnews.get_top_news()
        self.assertIsInstance(top_news_articles, list)
        self.assertGreater(len(top_news_articles), 0)

    async def test_get_news_by_topic(self):
        topic = "business"
        news_articles = await self.gnews.get_news_by_topic(topic)
        self.assertIsInstance(news_articles, list)
        self.assertGreater(len(news_articles), 0)

    async def test_get_news_by_location(self):
        location = "India"
        news_articles = await self.gnews.get_news_by_location(location)
        self.assertIsInstance(news_articles, list)
        if news_articles:
            self.assertIn("title", news_articles[0])
            self.assertIn("url", news_articles[0])

    async def test_get_news_by_site_valid(self):
        site = "cnn.com"
        news_articles = await self.gnews.get_news_by_site(site)
        self.assertIsInstance(news_articles, list)
        self.assertGreater(len(news_articles), 0)

    async def test_get_news_by_site_invalid(self):
        site = "invalidsite123.com"
        news_articles = await self.gnews.get_news_by_site(site)
        self.assertEqual(news_articles, [])


if __name__ == "__main__":
    unittest.main()

