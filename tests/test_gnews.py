import unittest
from gnews import GNews

class TestGNews(unittest.TestCase):
    def setUp(self):
        # Create a GNews instance with default parameters for testing
        self.gnews = GNews()

    def test_get_news(self):
        # Test that get_news returns a non-empty list of news articles
        key = "Google"
        news_articles = self.gnews.get_news(key)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_top_news(self):
        # Test that get_top_news returns a non-empty list of news articles
        top_news_articles = self.gnews.get_top_news()
        self.assertTrue(isinstance(top_news_articles, list))
        self.assertTrue(len(top_news_articles) > 0)

    def test_get_news_by_topic(self):
        # Test that get_news_by_topic returns a non-empty list of news articles for a valid topic
        topic = "business"
        news_articles = self.gnews.get_news_by_topic(topic)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_news_by_location(self):
        # Test that get_news_by_location returns a non-empty list of news articles for a valid location
        location = "India"
        news_articles = self.gnews.get_news_by_location(location)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_full_article(self):
        pass
        # Test that get_full_article returns a valid article object for a valid URL
        # url = "https://www.bbc.com/news/live/world-us-canada-66248859"
        # article = self.gnews.get_full_article(url)
        # self.assertIsNotNone(article)
        # self.assertTrue(hasattr(article, 'title'))
        # self.assertTrue(hasattr(article, 'text'))

if __name__ == '__main__':
    unittest.main()
