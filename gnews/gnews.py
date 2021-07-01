import feedparser
from bs4 import BeautifulSoup as Soup

from gnews.utils.constants import countries, languages
from gnews.utils.utils import lang_mapping, country_mapping, import_or_install


class GNews:
    """
    GNews initialization
    """

    def __init__(self, language="en", country="US", max_results=100, period=None):
        self.countries = tuple(countries),
        self.languages = tuple(languages),
        self._max_results = max_results
        self._language = language
        self._country = country

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
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        self._language = languages.get(language, language)

    @property
    def max_results(self):
        return self._max_results

    @max_results.setter
    def max_results(self, size):
        self._max_results = size

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = countries.get(country, country)

    def get_full_article(self, url):
        try:
            import_or_install('newspaper')
            from newspaper import Article
            article = Article(url="%s" % url, language=self._language)
            article.download()
            article.parse()
        except Exception as error:
            print(error.args[0])
            return None
        return article

    def _clean(self, html):
        soup = Soup(html, features="html.parser")
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def _process(self, item):
        item = {
            'title': item.get("title", ""),
            'description': self._clean(item.get("description", "")),
            'published date': item.get("published", ""),
            'url': item.get("link", ""),
            'publisher': item.get("source", " ")
        }
        return item

    def get_news(self, key):
        if key != '':
            key = "%20".join(key.split(" "))
            url = self.BASE_URL + '/search?q={}'.format(key) + self._ceid()
            return list(map(self._process, feedparser.parse(url).entries[:self._max_results]))
