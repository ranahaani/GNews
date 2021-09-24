from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('Pakistan')
print(json_resp[0])

google_news.store_in_mongodb(json_resp[0])