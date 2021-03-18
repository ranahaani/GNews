import feedparser
from bs4 import BeautifulSoup as Soup

from gnews.utils.constants import countries, languages
from gnews.utils.utils import lang_mapping, country_mapping


class GNews:
    """
    GNews initialization
    """

    def __init__(self, language="english", country="United States", max_results=5, period=None):
        self.countries = *countries,
        self.languages = *languages,
        self._max_results = max_results
        self._language = lang_mapping(language)
        self._country = country_mapping(country)

        self._period = period
        self.BASE_URL = 'https://news.google.com/rss'

    def _ceid(self):
        if self._period:
            return 'when%3A{}&ceid={}:{}&hl={}&gl={}'.format(self._period,
                                                             self._country,
                                                             self._language,
                                                             self._language,
                                                             self._country)
        return '&ceid={}:{}&hl={}&gl={}'.format(self._country,
                                                self._language,
                                                self._language,
                                                self._country)

    def set_language(self, language):
        self._language = language

    def set_max_results(self, size):
        self._max_results = size

    def set_period(self, period):
        self._period = period

    def set_country(self, country):
        self._country = country

    def get_full_article(self, url):
        try:
            from newspaper import Article
            article = Article(url="%s" % url, language=self._language)
            article.download()
            article.parse()
        except Exception as error:
            print(error.args[0])
            return None
        return article

    def _clean(self, html):
        soup = Soup(html, features="lxml")
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def _process(self, item):
        item = {
            'title': item.get("title", ""),
            'description': self._clean(item.get("description", "")),
            'published date': item.get("published", ""),
            'url': item.get("link", ""),
            'publisher': item.get("source", " ").get("title", " ")
        }
        return item

    def get_news(self, key):
        if key != '':
            key = "%20".join(key.split(" "))
            url = self.BASE_URL + '/search?q={}'.format(key) + self._ceid()
            return list(map(self._process, feedparser.parse(url).entries[:self._max_results]))
