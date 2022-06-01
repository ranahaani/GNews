from gnews import GNews

google_news = GNews()

google_news.start_date = (2021, 1, 1)
google_news.end_date = (2021, 2, 1)
google_news.max_results = 2

google_news.get_news_by_topic("WORLD")
result = google_news.get_news('"WORLD"')
print(result)
