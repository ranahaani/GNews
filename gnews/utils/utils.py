import hashlib
import json
import logging
import re

import requests
from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, GOOGLE_NEWS_REGEX


def lang_mapping(lang):
    return AVAILABLE_LANGUAGES.get(lang)


def country_mapping(country):
    return AVAILABLE_COUNTRIES.get(country)


def process_url(item, exclude_websites):
    source = item.get('source').get('href')
    if not all([not re.match(website, source) for website in
                [f'^http(s)?://(www.)?{website.lower()}.*' for website in exclude_websites]]):
        return
    url = item.get('link')
    if re.match(GOOGLE_NEWS_REGEX, url):
        url = requests.head(url).headers.get('location', url)
    return url

@staticmethod
def _get_final_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        final_url = response.url
        return final_url
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None