import feedparser
from bs4 import BeautifulSoup as Soup


class GNews:
    def __init__(self, language="en", country="US", size=5, period=None):
        self.__size = size
        self.__language = language.lower()
        self.__country = country.upper()
        self.__period = period
        self.BASE_URL = 'https://news.google.com/rss'

    def __ceid(self):
        if self.__period:
            return 'when%3A{}&ceid={}:{}&hl={}&gl={}'.format(self.__period, self.__country, self.__language,
                                                             self.__language, self.__country)
        return '&ceid={}:{}&hl={}&gl={}'.format(self.__country, self.__language, self.__language, self.__country)

    def set_language(self, language):
        self.__language = language

    def set_period(self, period):
        self.__period = period

    def set_country(self, country):
        self.__country = country

    def get_full_article(self, url):
        try:
            from newspaper import Article
            article = Article(url="%s" % url, language=self.__language)
            article.download()
            article.parse()
        except Exception as error:
            print(error.args[0])
            return None
        return article

    def __clean(self, html):
        soup = Soup(html, features="lxml")
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def __process(self, item):
        item = {
            'title': item.get("title", ""),
            'description': self.__clean(item.get("description", "")),
            'published date': item.get("published", ""),
            'url': item.get("link", ""),
            'publisher': item.get("source", " ").get("title", " ")
        }
        return item

    def get_news(self, key):
        if key != '':
            key = "%20".join(key.split(" "))
            url = self.BASE_URL + '/search?q={}'.format(key) + self.__ceid()
            return list(map(self.__process, feedparser.parse(url).entries[:self.__size]))
