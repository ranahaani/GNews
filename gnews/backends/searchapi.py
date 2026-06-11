import requests
from gnews.exceptions import NetworkError, InvalidConfigError
from gnews.utils.constants import SEARCHAPI_BASE_URL


class SearchApiBackend:
    def __init__(self, api_key: str):
        if not api_key:
            raise InvalidConfigError("searchapi_key cannot be empty.")
        self._api_key = api_key

    def get_news(self, query: str, language: str = "en", country: str = "US",
                 start_date: str = None, end_date: str = None,
                 max_results: int = 10, page: int = 1) -> list[dict]:
        params = {
            "engine": "google_news",
            "q": query,
            "hl": language,
            "gl": country,
            "api_key": self._api_key,
            "page": page,
        }
        if start_date or end_date:
            tbs_parts = []
            if start_date:
                tbs_parts.append(f"cdr:1,cd_min:{start_date}")
            if end_date:
                tbs_parts.append(f"cd_max:{end_date}")
            params["tbs"] = ",".join(tbs_parts)

        return self._fetch(params, max_results)

    def _fetch(self, params: dict, max_results: int) -> list[dict]:
        try:
            response = requests.get(SEARCHAPI_BASE_URL, params=params, timeout=10)
            if response.status_code != 200:
                raise NetworkError(f"SearchApi returned {response.status_code}: {response.text}")
            data = response.json()
            results = data.get("organic_results", [])
            return [self._map_article(item) for item in results[:max_results]]
        except NetworkError:
            raise
        except Exception as e:
            raise NetworkError(f"SearchApi request failed: {e}") from e

    @staticmethod
    def _map_article(item: dict) -> dict:
        return {
            "title": item.get("title", ""),
            "description": item.get("snippet", ""),
            "published date": item.get("date", ""),
            "iso_date": item.get("iso_date", ""),
            "url": item.get("link", ""),
            "publisher": item.get("source", ""),
            "thumbnail": item.get("thumbnail", ""),
            "favicon": item.get("favicon", ""),
            "rank": item.get("position", 0),
        }
