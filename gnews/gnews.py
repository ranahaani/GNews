import logging
import os
import urllib.request

import feedparser
from bs4 import BeautifulSoup as Soup
from dotenv import load_dotenv

from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, TOPICS, BASE_URL, USER_AGENT
from gnews.utils.utils import connect_database, post_database, import_or_install, process_url

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


class GNews:
    """
    GNews initialization
    """

    def __init__(self, language="en", country="US", max_results=100, period=None, exclude_websites=None, proxy=None):
        self.countries = tuple(AVAILABLE_COUNTRIES),
        self.languages = tuple(AVAILABLE_LANGUAGES),
        self._max_results = max_results
        self._language = language
        self._country = country
        self._period = period
        self._exclude_websites = exclude_websites if exclude_websites and isinstance(exclude_websites, list) else []
        self._proxy = {'http': proxy, 'https': proxy} if proxy else None

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
        self._language = AVAILABLE_LANGUAGES.get(language, language)

    @property
    def exclude_websites(self):
        return self._exclude_websites

    @exclude_websites.setter
    def exclude_websites(self, exclude_websites):
        self._exclude_websites = exclude_websites

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
        self._country = AVAILABLE_COUNTRIES.get(country, country)

    def get_full_article(self, url):
        try:
            import_or_install('newspaper3k')
            from newspaper import Article
            article = Article(url="%s" % url, language=self._language)
            article.download()
            article.parse()
        except Exception as error:
            logger.error(error.args[0])
            return None
        return article

    def _clean(self, html):
        soup = Soup(html, features="html.parser")
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def _process(self, item):
        url = process_url(item, self._exclude_websites)
        if url:
            title = item.get("title", "")
            item = {
                'title': title,
                'description': self._clean(item.get("description", "")),
                'published date': item.get("published", ""),
                'url': url,
                'publisher': item.get("source", " ")
            }
            return item

    def get_news(self, key):
        """
         :return: JSON response as nested Python dictionary.
        """
        if key:
            key = "%20".join(key.split(" "))
            url = BASE_URL + '/search?q={}'.format(key) + self._ceid()
            return self._get_news(url)

    def get_top_news(self):
        """
         :return: Top News JSON response.
        """
        url = BASE_URL + "?" + self._ceid()
        return self._get_news(url)

    def get_news_by_topic(self, topic: str):
        f"""
        :params: TOPIC names i.e {TOPICS}
         :return: JSON response as nested Python dictionary.
        """
        topic = topic.upper()
        if topic in TOPICS:
            url = BASE_URL + '/headlines/section/topic/' + topic + '?' + self._ceid()
            return self._get_news(url)

        logger.info(f"Invalid topic. \nAvailable topics are: {', '.join(TOPICS)}.")
        return []

    def get_news_by_location(self, location: str):
        """
        :params: city/state/country
         :return: JSON response as nested Python dictionary.
        """
        if location:
            url = BASE_URL + '/headlines/section/geo/' + location + '?' + self._ceid()
            return self._get_news(url)
        logger.warning("Enter a valid location.")
        return []

    def _get_news(self, url):
        try:
            if self._proxy:
                proxy_handler = urllib.request.ProxyHandler(self._proxy)
                feed_data = feedparser.parse(url, agent=USER_AGENT, handlers=[proxy_handler])
            else:
                feed_data = feedparser.parse(url, agent=USER_AGENT)

            return [item for item in
                    map(self._process, feed_data.entries[:self._max_results]) if item]
        except Exception as err:
            logger.error(err.args[0])
            return []

    def store_in_mongodb(self, news):
        """MongoDB cluster needs to be created first - https://www.mongodb.com/cloud/atlas/register"""
        load_dotenv()

        db_user = os.getenv("DB_USER")
        db_pw = os.getenv("DB_PW")
        db_name = os.getenv("DB_NAME")
        collection_name = os.getenv("COLLECTION_NAME")

        collection = connect_database(db_user, db_pw, db_name, collection_name)
        post_database(collection, news)
