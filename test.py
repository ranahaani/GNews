# from gnews import GNews

# google_news = GNews()
# pakistan_news = google_news.get_news('World')
# print(pakistan_news[0])

from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('World')
article = google_news.get_full_article(
    json_resp[0]['url'])  
#print(json_resp)
print(article.text)