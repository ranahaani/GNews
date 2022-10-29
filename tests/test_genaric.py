import unittest

from gnews import GNews


class TestGNews(unittest.TestCase):
    def test_GNews(self):
        google_news = GNews()

        # News by keyword
        result = google_news.get_news("Cryptocurrency")
        self.assertNotEqual(0, len(result))

        # News by TOPICS
        result = google_news.get_news_by_topic("WORLD")
        self.assertNotEqual(0, len(result))

        # News by Location
        result = google_news.get_news_by_location("Pakistan")
        self.assertNotEqual(0, len(result))

        # Top News
        result = google_news.get_top_news()
        self.assertNotEqual(0, len(result))
