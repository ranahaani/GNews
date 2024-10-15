from datetime import datetime, timedelta
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

def str_to_datetime(date_str:str):
    return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')

def period_to_datetime(period: str):
    now = datetime.now()
    ammount = int(period[:-1])
    delta = period[-1]
    
    if delta == 'd':
        init_date = now - timedelta(days=ammount)
    elif delta == 'h':
        init_date = now - timedelta(hours=ammount)
    elif delta == 'm':
        init_date = now - timedelta(days=ammount*30)
    
    return init_date
