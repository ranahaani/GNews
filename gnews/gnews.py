from __future__ import annotations

import asyncio
import csv
import functools
import json
import logging
import urllib.request
import datetime
import inspect
import warnings

import feedparser
from bs4 import BeautifulSoup as Soup

from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, SECTIONS, TOPICS, BASE_URL, USER_AGENT
from gnews.utils.utils import process_url
from gnews.exceptions import (
    GNewsException,
    RateLimitError,
    InvalidConfigError,
    NetworkError,
)
from gnews.backends.searchapi import SearchApiBackend

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class GNews:
    def __init__(
        self,
        language: str = "en",
        country: str = "US",
        max_results: int = 100,
        period: str | None = None,
        start_date: tuple | datetime.datetime | None = None,
        end_date: tuple | datetime.datetime | None = None,
        exclude_websites: list[str] | None = None,
        proxy: dict | None = None,
        searchapi_key: str | None = None,
    ) -> None:
        """
        Initialize the GNews client with configuration options.

        :param language: The language in which to return results, defaults to 'en'
        :param country: The country code for which to get headlines, defaults to 'US'
        :param max_results: Maximum number of results to return
        :param period: Time period for filtering news
        :param start_date: Date after which results must have been published
        :param end_date: Date before which results must have been published
        :param exclude_websites: List of websites to exclude from results
        :param proxy: Proxy settings as a dict {protocol: address}
        """
        self.countries = tuple(AVAILABLE_COUNTRIES),
        self.languages = tuple(AVAILABLE_LANGUAGES),

        if max_results <= 0:
            raise InvalidConfigError("max_results must be a positive integer.")

        self._max_results = max_results
        self._language = language
        self._country = country
        self._period = period
        self._end_date = None
        self._start_date = None
        self.end_date = end_date
        self.start_date = start_date
        self._exclude_websites = exclude_websites if exclude_websites and isinstance(exclude_websites, list) else []
        self._proxy = proxy if proxy else None
        self._searchapi = SearchApiBackend(searchapi_key) if searchapi_key else None

    def _ceid(self) -> str:
        time_query = ''
        if self._start_date or self._end_date:
            if inspect.stack()[2][3] != 'get_news':
                warnings.warn(message=("Only searches using get_news support date ranges. "
                                       "Start and end dates will be ignored."), category=UserWarning, stacklevel=4)
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
        self._language = AVAILABLE_LANGUAGES.get(language, language)

    @property
    def exclude_websites(self):
        return self._exclude_websites

    @exclude_websites.setter
    def exclude_websites(self, exclude_websites):
        if not isinstance(exclude_websites, list):
            raise InvalidConfigError("exclude_websites must be a list.")
        self._exclude_websites = exclude_websites

    @property
    def max_results(self):
        return self._max_results

    @max_results.setter
    def max_results(self, size):
        if size <= 0:
            raise InvalidConfigError("max_results must be greater than 0.")
        self._max_results = size

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period

    @property
    def start_date(self):
        if self._start_date is None:
            return None
        self.period = None
        return self._start_date.strftime("%Y-%m-%d")

    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) is tuple:
            start_date = datetime.datetime(start_date[0], start_date[1], start_date[2])
        if self._end_date:
            if start_date - self._end_date == datetime.timedelta(days=0):
                warnings.warn("The start and end dates should be at least 1 day apart.")
            elif self._end_date < start_date:
                warnings.warn("End date should be after start date.")
        self._start_date = start_date

    @property
    def end_date(self):
        if self._end_date is None:
            return None
        self.period = None
        return self._end_date.strftime("%Y-%m-%d")

    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) is tuple:
            end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])
        if self._start_date:
            if end_date - self._start_date == datetime.timedelta(days=0):
                warnings.warn("The start and end dates should be at least 1 day apart.")
            elif end_date < self._start_date:
                warnings.warn("End date should be after start date.")
        self._end_date = end_date

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = AVAILABLE_COUNTRIES.get(country, country)

    def get_full_article(self, url: str) -> dict:
        try:
            import trafilatura
        except ImportError as e:
            raise ImportError(
                "get_full_article() requires trafilatura. "
                "Install it with: pip install gnews[fulltext]"
            ) from e

        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            raise NetworkError(f"Could not download article from {url}")

        text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
        if not text:
            raise NetworkError(f"Could not extract article text from {url}")

        return {"text": text, "url": url}

    @staticmethod
    def _clean(html: str) -> str:
        soup = Soup(html, features="html.parser")
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def _process(self, item: dict) -> dict | None:
        url = process_url(item, self._exclude_websites, self._proxy)
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
            if obj.__doc__:
                obj.__doc__ = obj.__doc__.format(*sub)
            return obj
        return dec


    indent = '\n\t\t\t'
    indent2 = indent + '\t'
    standard_output = (indent + "{'title': Article Title," + indent + "'description': Google News summary of the "
                       "article," + indent + "'url': link to the news article," + indent + "'publisher':" + indent2 +
                       "{'href': link to publisher's website," + indent2 + "'title': name of the publisher}}")

    @docstring_parameter(standard_output)
    def get_news(self, key: str, page: int = 1) -> list[dict]:
        if key:
            if self._searchapi:
                return self._searchapi.get_news(
                    query=key,
                    language=self._language,
                    country=self._country,
                    start_date=self.start_date,
                    end_date=self.end_date,
                    max_results=self._max_results,
                    page=page,
                )
            if self._max_results > 100:
                return self._get_news_more_than_100(key)
            key = "%20".join(key.split(" "))
            query = '/search?q={}'.format(key)
            return self._get_news(query)
        raise InvalidConfigError("Search key cannot be empty.")

    def _get_news_more_than_100(self, key: str) -> list[dict]:
        articles = []
        seen_urls = set()
        earliest_date = None

        if self._start_date or self._end_date or self._period:
            warnings.warn("Searches for over 100 articles ignore date ranges.", category=UserWarning)

        self._start_date = None
        self._end_date = None

        while len(articles) < self._max_results:
            fetched_articles = self._get_news(f'/search?q={key}')
            if not fetched_articles:
                break

            for article in fetched_articles:
                if article['url'] not in seen_urls:
                    articles.append(article)
                    seen_urls.add(article['url'])
                    published_date = article.get("published date")
                    try:
                        published_date = datetime.datetime.strptime(published_date, '%a, %d %b %Y %H:%M:%S GMT')
                    except Exception as e:
                        logger.warning(f"Failed to parse published date: {e}")
                        continue

                    if earliest_date is None or published_date < earliest_date:
                        earliest_date = published_date

                if len(articles) >= self._max_results:
                    return articles

            if len(fetched_articles) < 100:
                break

            self._end_date = earliest_date
            self._start_date = earliest_date - datetime.timedelta(days=7)

        return articles

    @docstring_parameter(standard_output)
    def get_top_news(self) -> list[dict]:
        query = "?"
        return self._get_news(query)

    @docstring_parameter(standard_output, ', '.join(TOPICS), ', '.join(SECTIONS.keys()))
    def get_news_by_topic(self, topic: str) -> list[dict]:
        topic = topic.upper()
        if topic in TOPICS:
            query = '/headlines/section/topic/' + topic + '?'
            return self._get_news(query)
        elif topic in SECTIONS.keys():
            query = '/topics/' + SECTIONS[topic] + '?'
            return self._get_news(query)
        raise InvalidConfigError(f"Invalid topic '{topic}'. Must be one of {list(TOPICS) + list(SECTIONS.keys())}.")

    @docstring_parameter(standard_output)
    def get_news_by_location(self, location: str) -> list[dict]:
        if location:
            query = '/headlines/section/geo/' + location + '?'
            return self._get_news(query)
        raise InvalidConfigError("Location cannot be empty.")

    @docstring_parameter(standard_output)
    def get_news_by_site(self, site: str) -> list[dict]:
        if site:
            key = "site:{}".format(site)
            return self.get_news(key)
        raise InvalidConfigError("Site domain cannot be empty.")

    async def _run_in_executor(self, func, *args):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, functools.partial(func, *args))

    async def get_news_async(self, key: str, page: int = 1) -> list[dict]:
        return await self._run_in_executor(self.get_news, key, page)

    async def get_top_news_async(self) -> list[dict]:
        return await self._run_in_executor(self.get_top_news)

    async def get_news_by_topic_async(self, topic: str) -> list[dict]:
        return await self._run_in_executor(self.get_news_by_topic, topic)

    async def get_news_by_location_async(self, location: str) -> list[dict]:
        return await self._run_in_executor(self.get_news_by_location, location)

    async def get_news_by_site_async(self, site: str) -> list[dict]:
        return await self._run_in_executor(self.get_news_by_site, site)

    def save_to_json(self, articles: list[dict], path: str) -> str:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        return path

    def save_to_csv(self, articles: list[dict], path: str) -> str:
        if not articles:
            open(path, "w").close()
            return path
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=articles[0].keys())
            writer.writeheader()
            writer.writerows(articles)
        return path

    def _get_news(self, query: str) -> list[dict]:
        url = BASE_URL + query + self._ceid()
        try:
            if self._proxy:
                proxy_handler = urllib.request.ProxyHandler(self._proxy)
                feed_data = feedparser.parse(url, agent=USER_AGENT, handlers=[proxy_handler])
            else:
                feed_data = feedparser.parse(url, agent=USER_AGENT)

            if feed_data.status == 429:
                raise RateLimitError("Rate limit exceeded while fetching news.")
            return [item for item in map(self._process, feed_data.entries[:self._max_results]) if item]

        except RateLimitError:
            raise
        except Exception as err:
            raise NetworkError(f"Failed to fetch or parse news feed: {err}") from err
