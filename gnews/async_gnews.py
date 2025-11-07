import asyncio
import datetime
import inspect
import logging
import re
import time
import warnings
from typing import Any, Dict, List, Optional

import aiohttp
import feedparser
from aiohttp import ClientError, ClientResponseError
from bs4 import BeautifulSoup as Soup

from gnews.exceptions import InvalidConfigError, NetworkError, RateLimitError
from gnews.utils.constants import (
    AVAILABLE_COUNTRIES,
    AVAILABLE_LANGUAGES,
    BASE_URL,
    GOOGLE_NEWS_REGEX,
    SECTIONS,
    TOPICS,
    USER_AGENT,
)


logger = logging.getLogger(__name__)


class GNewsAsync:
    def __init__(
        self,
        language: str = "en",
        country: str = "US",
        max_results: int = 100,
        period: Optional[str] = None,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None,
        exclude_websites: Optional[List[str]] = None,
        proxy: Optional[Dict[str, str]] = None,
        session: Optional[aiohttp.ClientSession] = None,
        request_timeout: Optional[float] = None,
    ) -> None:
        """Async interface for Google News fetching using aiohttp."""

        if max_results <= 0:
            raise InvalidConfigError("max_results must be a positive integer.")

        self.countries = (tuple(AVAILABLE_COUNTRIES),)
        self.languages = (tuple(AVAILABLE_LANGUAGES),)

        self._max_results = max_results
        self._language = language
        self._country = country
        self._period = period
        self._end_date: Optional[datetime.datetime] = None
        self._start_date: Optional[datetime.datetime] = None
        self.end_date = end_date
        self.start_date = start_date
        self._exclude_websites = (
            exclude_websites if exclude_websites and isinstance(exclude_websites, list) else []
        )
        self._proxy = proxy if proxy else None

        self._external_session = session
        self._session: Optional[aiohttp.ClientSession] = session
        self._request_timeout = aiohttp.ClientTimeout(total=request_timeout) if request_timeout else None
        self._owns_session = session is None

    async def __aenter__(self) -> "GNewsAsync":
        await self._ensure_session()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if self._owns_session and self._session and not self._session.closed:
            await self._session.close()
        self._session = None

    close = aclose

    async def _ensure_session(self) -> aiohttp.ClientSession:
        if self._session and not self._session.closed:
            return self._session

        if self._external_session and not self._external_session.closed:
            self._session = self._external_session
            self._owns_session = False
            return self._session

        headers = {"User-Agent": USER_AGENT}
        self._session = aiohttp.ClientSession(headers=headers, timeout=self._request_timeout)
        self._owns_session = True
        return self._session

    def _ceid(self) -> str:
        time_query = ""
        if self._start_date or self._end_date:
            if inspect.stack()[2][3] != "get_news":
                warnings.warn(
                    "Only searches using get_news support date ranges. Start and end dates will be ignored.",
                    UserWarning,
                    stacklevel=4,
                )
                if self._period:
                    time_query += "when%3A".format(self._period)
            if self._period:
                warnings.warn(
                    f"\nPeriod ({self.period}) will be ignored in favour of the start and end dates",
                    UserWarning,
                    stacklevel=4,
                )
            if self.end_date is not None:
                time_query += "%20before%3A{}".format(self.end_date)
            if self.start_date is not None:
                time_query += "%20after%3A{}".format(self.start_date)
        elif self._period:
            time_query += "%20when%3A{}".format(self._period)

        return (
            time_query
            + "&hl={}&gl={}&ceid={}:{}".format(
                self._language,
                self._country,
                self._country,
                self._language,
            )
        )

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        self._language = AVAILABLE_LANGUAGES.get(language, language)

    @property
    def exclude_websites(self) -> List[str]:
        return self._exclude_websites

    @exclude_websites.setter
    def exclude_websites(self, exclude_websites: List[str]) -> None:
        if not isinstance(exclude_websites, list):
            raise InvalidConfigError("exclude_websites must be a list.")
        self._exclude_websites = exclude_websites

    @property
    def max_results(self) -> int:
        return self._max_results

    @max_results.setter
    def max_results(self, size: int) -> None:
        if size <= 0:
            raise InvalidConfigError("max_results must be greater than 0.")
        self._max_results = size

    @property
    def period(self) -> Optional[str]:
        return self._period

    @period.setter
    def period(self, period: Optional[str]) -> None:
        self._period = period

    @property
    def start_date(self) -> Optional[str]:
        if self._start_date is None:
            return None
        self.period = None
        return self._start_date.strftime("%Y-%m-%d")

    @start_date.setter
    def start_date(self, start_date: Optional[datetime.datetime]) -> None:
        if isinstance(start_date, tuple):
            start_date = datetime.datetime(start_date[0], start_date[1], start_date[2])
        if start_date and self._end_date:
            if start_date - self._end_date == datetime.timedelta(days=0):
                warnings.warn("The start and end dates should be at least 1 day apart.")
            elif self._end_date < start_date:
                warnings.warn("End date should be after start date.")
        self._start_date = start_date

    @property
    def end_date(self) -> Optional[str]:
        if self._end_date is None:
            return None
        self.period = None
        return self._end_date.strftime("%Y-%m-%d")

    @end_date.setter
    def end_date(self, end_date: Optional[datetime.datetime]) -> None:
        if isinstance(end_date, tuple):
            end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])
        if end_date and self._start_date:
            if end_date - self._start_date == datetime.timedelta(days=0):
                warnings.warn("The start and end dates should be at least 1 day apart.")
            elif end_date < self._start_date:
                warnings.warn("End date should be after start date.")
        self._end_date = end_date

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        self._country = AVAILABLE_COUNTRIES.get(country, country)

    async def get_full_article(self, url: str) -> Any:
        try:
            import newspaper # type: ignore
        except ImportError as error:
            raise InvalidConfigError(
                "get_full_article() requires the `newspaper3k` library. Install it via `pip install newspaper3k`."
            ) from error

        async def _download() -> Any:
            """
            https://github.com/codelucas/newspaper/issues/297
            https://github.com/AndyTheFactory/newspaper4k/issues/56
            Now library `newspaper3k` not support async. And this wrapper resolve this problem.
            """
            try:
                article = newspaper.Article(url=url, language=self._language)
                article.download()
                article.parse()
                return article
            except Exception as err:
                raise NetworkError(f"An error occurred while fetching the article: {err}") from err

        return await asyncio.to_thread(_download)

    @staticmethod
    def _clean(html: str) -> str:
        soup = Soup(html, features="html.parser")
        text = soup.get_text()
        return text.replace("\xa0", " ")

    async def get_news(self, key: str) -> List[Dict[str, Any]]:
        if not key:
            raise InvalidConfigError("Search key cannot be empty.")

        if self._max_results > 100:
            return await self._get_news_more_than_100(key)

        query = "/search?q={}".format("%20".join(key.split(" ")))
        return await self._get_news(query)

    async def _get_news_more_than_100(self, key: str) -> List[Dict[str, Any]]:
        articles: List[Dict[str, Any]] = []
        seen_urls = set()
        earliest_date: Optional[datetime.datetime] = None

        if self._start_date or self._end_date or self._period:
            warnings.warn("Searches for over 100 articles ignore date ranges.", category=UserWarning)

        original_start = self._start_date
        original_end = self._end_date

        self._start_date = None
        self._end_date = None

        try:
            while len(articles) < self._max_results:
                fetched_articles = await self._get_news(f"/search?q={key}")
                if not fetched_articles:
                    break

                for article in fetched_articles:
                    url = article.get("url")
                    if not url or url in seen_urls:
                        continue
                    articles.append(article)
                    seen_urls.add(url)
                    published_date = article.get("published date")
                    try:
                        if published_date:
                            parsed_date = datetime.datetime.strptime(published_date, "%a, %d %b %Y %H:%M:%S GMT")
                        else:
                            parsed_date = None
                    except Exception as error:  # noqa: BLE001
                        logger.warning("Failed to parse published date: %s", error)
                        parsed_date = None

                    if parsed_date and (earliest_date is None or parsed_date < earliest_date):
                        earliest_date = parsed_date

                    if len(articles) >= self._max_results:
                        return articles[: self._max_results]

                if len(fetched_articles) < 100:
                    break

                if earliest_date is None:
                    break

                self._end_date = earliest_date
                self._start_date = earliest_date - datetime.timedelta(days=7)
        finally:
            self._start_date = original_start
            self._end_date = original_end

        return articles[: self._max_results]

    async def get_top_news(self) -> List[Dict[str, Any]]:
        return await self._get_news("?")

    async def get_news_by_topic(self, topic: str) -> List[Dict[str, Any]]:
        topic_upper = topic.upper()
        if topic_upper in TOPICS:
            return await self._get_news("/headlines/section/topic/" + topic_upper + "?")
        if topic_upper in SECTIONS:
            return await self._get_news("/topics/" + SECTIONS[topic_upper] + "?")
        raise InvalidConfigError(f"Invalid topic '{topic}'. Must be one of {list(TOPICS) + list(SECTIONS.keys())}.")

    async def get_news_by_location(self, location: str) -> List[Dict[str, Any]]:
        if not location:
            raise InvalidConfigError("Location cannot be empty.")
        return await self._get_news("/headlines/section/geo/" + location + "?")

    async def get_news_by_site(self, site: str) -> List[Dict[str, Any]]:
        if not site:
            raise InvalidConfigError("Site domain cannot be empty.")
        return await self.get_news(f"site:{site}")

    async def _get_news(self, query: str) -> List[Dict[str, Any]]:
        url = BASE_URL + query + self._ceid()
        session = await self._ensure_session()
        proxy = self._get_proxy_for_url(url)

        try:
            time_start = time.time()
            async with session.get(url, proxy=proxy, ssl=False) as response:
                time_end = time.time()
                if response.status == 429:
                    raise RateLimitError("Rate limit exceeded while fetching news.")
                response.raise_for_status()
                raw_feed = await response.text()
        except RateLimitError:
            raise
        except ClientResponseError as error:
            raise NetworkError(f"Failed to fetch news feed: {error}") from error
        except ClientError as error:
            raise NetworkError(f"Failed to fetch news feed: {error}") from error

        feed_data = feedparser.parse(raw_feed)


        entries = feed_data.entries[: self._max_results]
        processed_entries = await asyncio.gather(
            *(self._process(entry) for entry in entries), return_exceptions=True
        )

        results: List[Dict[str, Any] | BaseException] = []
        for item in processed_entries:
            if isinstance(item, Exception):
                logger.debug("Skipping entry due to processing error: %s", item)
                continue
            if item is not None:
                results.append(item)

        return results

    async def _process(self, item: Any) -> Optional[Dict[str, Any]]:
        url = await self._resolve_entry_url(item)
        if not url:
            return None

        title = item.get("title", "")
        return {
            "title": title,
            "description": self._clean(item.get("description", "")),
            "published date": item.get("published", ""),
            "url": url,
            "publisher": item.get("source", " "),
        }

    async def _resolve_entry_url(self, item: Any) -> Optional[str]:
        source = item.get("source")
        if source:
            href = source.get("href")
            if href and not self._is_allowed_website(href):
                return None

        url = item.get("link")
        if not url:
            return None

        if re.match(GOOGLE_NEWS_REGEX, url):
            return await self._follow_redirect(url)
        return url

    def _is_allowed_website(self, source_url: str) -> bool:
        if not self._exclude_websites:
            return True
        for website in self._exclude_websites:
            pattern = rf"^http(s)?://(www.)?{website.lower()}.*"
            if re.match(pattern, source_url.lower()):
                return False
        return True

    async def _follow_redirect(self, url: str) -> Optional[str]:
        session = await self._ensure_session()
        proxy = self._get_proxy_for_url(url)

        try:
            async with session.head(url, allow_redirects=False, proxy=proxy, ssl=False) as response:
                if response.status in {301, 302, 303, 307, 308}:
                    location = response.headers.get("Location")
                    if location:
                        return location
                if 200 <= response.status < 400:
                    return str(response.url)
                if response.status == 405:
                    return await self._follow_redirect_with_get(url, proxy)
        except ClientResponseError:
            return None
        except ClientError:
            return None

        return url

    async def _follow_redirect_with_get(self, url: str, proxy: Optional[str]) -> Optional[str]:
        session = await self._ensure_session()
        try:
            async with session.get(url, allow_redirects=True, proxy=proxy) as response:
                if 200 <= response.status < 400:
                    return str(response.url)
        except ClientResponseError:
            return None
        except ClientError:
            return None
        return url

    def _get_proxy_for_url(self, url: str) -> Optional[str]:
        if not self._proxy:
            return None
        try:
            scheme = url.split(":", 1)[0]
        except IndexError:
            return None
        return self._proxy.get(scheme)


