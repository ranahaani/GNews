import logging
import os
import sys
import urllib.request
import datetime
import inspect
import warnings

import feedparser
from bs4 import BeautifulSoup as Soup
from dotenv import load_dotenv

try:
    import newspaper  # Optional - required by GNews.get_full_article()
except ImportError:
    pass

from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, TOPICS, BASE_URL, USER_AGENT
from gnews.utils.utils import connect_database, post_database, process_url

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


class GNews:
    def __init__(self, language="en", country="US", max_results=100, period=None, start_date=None, end_date=None,
                 exclude_websites=None, proxy=None):
        """
        (optional parameters)
        :param language: The language in which to return results, defaults to en (optional)
        :param country: The country code of the country you want to get headlines for, defaults to US
        :param max_results: The maximum number of results to return. The default is 100, defaults to 100
        :param period: The period of time from which you want the news
        :param start_date: Date after which results must have been published
        :param end_date: Date before which results must have been published
        :param exclude_websites: A list of strings that indicate websites to exclude from results
        :param proxy: The proxy parameter is a dictionary with a single key-value pair. The key is the
        protocol name and the value is the proxy address
        """
        self.countries = tuple(AVAILABLE_COUNTRIES),
        self.languages = tuple(AVAILABLE_LANGUAGES),
        self._max_results = max_results
        self._language = language
        self._country = country
        self._period = period
        self._end_date = None
        self._start_date = None
        self.end_date = self.end_date = end_date
        self._start_date = self.start_date = start_date
        self._exclude_websites = exclude_websites if exclude_websites and isinstance(exclude_websites, list) else []
        self._proxy = {'http': proxy, 'https': proxy} if proxy else None

    def _ceid(self):
        time_query = ''
        if self._start_date or self._end_date:
            if inspect.stack()[2][3] != 'get_news':
                warnings.warn(message=("Only searches using the function get_news support date ranges. Review the "
                                       f"documentation for {inspect.stack()[2][3]} for a partial workaround. \nStart "
                                       "date and end date will be ignored"), category=UserWarning, stacklevel=4)
                if self._period:
                    time_query += 'when%3A'.format(self._period)
            if self._period:
                warnings.warn(message=f'\nPeriod ({self.period}) will be ignored in favour of the start and end dates',
                              category=UserWarning, stacklevel=4)
            if self.end_date is not None:
                time_query += '%20before%3A{}'.format(self.end_date)
            if self.start_date is not None:
                time_query += '%20after%3A{}'.format(self.start_date)
        elif self._period:
            time_query += '%20when%3A{}'.format(self._period)

        return time_query + '&hl={}&gl={}&ceid={}:{}'.format(self._language,
                                                             self._country,
                                                             self._country,
                                                             self._language,)

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        """
        :param language: The language code for the language you want to use
        """
        self._language = AVAILABLE_LANGUAGES.get(language, language)

    @property
    def exclude_websites(self):
        return self._exclude_websites

    @exclude_websites.setter
    def exclude_websites(self, exclude_websites):
        """
        The function takes in a list of websites that you want to exclude
        :param exclude_websites: A list of strings that will be used to filter out websites
        """
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
    def start_date(self):
        """
        :return: string of start_date in form YYYY-MM-DD, or None if start_date is not set
        …NOTE this will reset period to None if start_date is not none
        """
        if self._start_date is None:
            return None
        self.period = None
        return self._start_date.strftime("%Y-%m-%d")

    @start_date.setter
    def start_date(self, start_date):
        """
        The function sets the start of the date range you want to search
        :param start_date: either a tuple in the form (YYYY, MM, DD) or a datetime
        """
        if type(start_date) is tuple:
            start_date = datetime.datetime(start_date[0], start_date[1], start_date[2])
        if self._end_date:
            if start_date - self._end_date == datetime.timedelta(days=0):
                warnings.warn("The start and end dates should be at least 1 day apart, or GNews will return no results")
            elif self._end_date < start_date:
                warnings.warn("End date should be after start date, or GNews will return no results")
        self._start_date = start_date

    @property
    def end_date(self):
        """
        :return: string of end_date in form YYYY-MM-DD, or None if end_date is not set
        …NOTE this will reset period to None if end date is not None
        """
        if self._end_date is None:
            return None
        self.period = None
        return self._end_date.strftime("%Y-%m-%d")

    @end_date.setter
    def end_date(self, end_date):
        """
        The function sets the end of the date range you want to search
        :param end_date: either a tuple in the form (YYYY, MM, DD) or a datetime
        …NOTE this will reset period to None
        """
        if type(end_date) is tuple:
            end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])
        if self._start_date:
            if end_date - self._start_date == datetime.timedelta(days=0):
                warnings.warn("The start and end dates should be at least 1 day apart, or GNews will return no results")
            elif end_date < self._start_date:
                warnings.warn("End date should be after start date, or GNews will return no results")
        self._end_date = end_date

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = AVAILABLE_COUNTRIES.get(country, country)

    def get_full_article(self, url):
        """
        Download an article from the specified URL, parse it, and return an article object.
         :param url: The URL of the article you wish to summarize.
         :return: An `Article` object returned by the `newspaper` library.
        """
        # Check if the `newspaper` library is available
        if 'newspaper' not in (sys.modules.keys() & globals()):  # Top import failed since it's not installed
            print("\nget_full_article() requires the `newspaper` library.")
            print("You can install it by running `python3 -m pip install newspaper3k` in your shell.\n")
            return None
        try:
            article = newspaper.Article(url="%s" % url, language=self._language)
            article.download()
            article.parse()
        except Exception as error:
            logger.error(error.args[0])
            return None
        return article

    @staticmethod
    def _clean(html):
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

    def docstring_parameter(*sub):
        def dec(obj):
            obj.__doc__ = obj.__doc__.format(*sub)
            return obj

        return dec

    indent = '\n\t\t\t'
    indent2 = indent + '\t'
    standard_output = (indent + "{'title': Article Title," + indent + "'description': Google News summary of the "
                       "article," + indent + "'url': link to the news article," + indent + "'publisher':" + indent2 +
                       "{'href': link to publisher's website," + indent2 + "'title': name of the publisher}}")

    @docstring_parameter(standard_output)
    def get_news(self, key):
        """
        The function takes in a key and returns a list of news articles
        :param key: The query you want to search for. For example, if you want to search for news about
        the "Yahoo", you would get results from Google News according to your key i.e "yahoo"
        :return: A list of dictionaries with structure: {0}.
        """
        if key:
            key = "%20".join(key.split(" "))
            query = '/search?q={}'.format(key)
            return self._get_news(query)

    @docstring_parameter(standard_output)
    def get_top_news(self):
        """
        This function returns top news stories for the current time
        :return: A list of dictionaries with structure: {0}.
        ..To implement date range try get_news('?')
        """
        query = "?"
        return self._get_news(query)

    @docstring_parameter(standard_output, ', '.join(TOPICS))
    def get_news_by_topic(self, topic: str):
        """
        Function to get news from one of Google's key topics
        :param topic: TOPIC names i.e {1}
        :return: A list of dictionaries with structure: {0}.
        ..To implement date range try get_news('topic')
        """
        topic = topic.upper()
        if topic in TOPICS:
            query = '/headlines/section/topic/' + topic + '?'
            return self._get_news(query)

        logger.info(f"Invalid topic. \nAvailable topics are: {', '.join(TOPICS)}.")
        return []

    @docstring_parameter(standard_output)
    def get_news_by_location(self, location: str):
        """
        This function is used to get news from a specific location (city, state, and country)
        :param location: (type: str) The location for which you want to get headlines
        :return: A list of dictionaries with structure: {0}.
        ..To implement date range try get_news('location')
        """
        if location:
            query = '/headlines/section/geo/' + location + '?'
            return self._get_news(query)
        logger.warning("Enter a valid location.")
        return []

    def _get_news(self, query):
        url = BASE_URL + query + self._ceid()
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
        """
        - MongoDB cluster needs to be created first - https://www.mongodb.com/cloud/atlas/register
        - Connect to the MongoDB cluster
        - Create a new collection
        - Insert the news into the collection
         :param news: the news object that we created in the previous function
        """

        load_dotenv()

        db_user = os.getenv("DB_USER")
        db_pw = os.getenv("DB_PW")
        db_name = os.getenv("DB_NAME")
        collection_name = os.getenv("COLLECTION_NAME")

        collection = connect_database(db_user, db_pw, db_name, collection_name)
        post_database(collection, news)
