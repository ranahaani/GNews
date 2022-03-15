import hashlib
import json
import logging
import re

import pymongo
import requests
from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, GOOGLE_NEWS_REGEX
from pymongo import MongoClient


def lang_mapping(lang):
    return AVAILABLE_LANGUAGES.get(lang)


def country_mapping(country):
    return AVAILABLE_COUNTRIES.get(country)


def connect_database(db_user, db_pw, db_name, collection_name):
    """Mongo DB Establish Cluster Connection"""

    # .env file Structure:

    # DB_USER="..."
    # DB_PW="..."
    # DB_NAME="..."
    # COLLECTION_NAME="..."

    # name of the mongodb cluster as well as the database name should be "gnews"

    try:
        cluster = MongoClient(
            "mongodb+srv://" +
            db_user +
            ":" +
            db_pw +
            "@gnews.stjap.mongodb.net/" +
            db_name +
            "?retryWrites=true&w=majority"
        )

        db = cluster[db_name]
        collection = db[collection_name]

        return collection

    except Exception as e:
        print("Connection Error.", e)


def post_database(collection, news):
    """post unique news articles to mongodb database"""
    doc = {
        "_id": hashlib.sha256(str(json.dumps(news)).encode('utf-8')).hexdigest(),
        "title": news['title'],
        "description": news['description'],
        "published_date": news['published date'],
        "url": news['url'],
        "publisher": news['publisher']
    }

    try:
        collection.update_one(doc, {'$set': doc}, upsert=True)
    except pymongo.errors.DuplicateKeyError:
        logging.error("Posting to database failed.")


def process_url(item, exclude_websites):
    source = item.get('source').get('href')
    if not all([not re.match(website, source) for website in
                [f'^http(s)?://(www.)?{website.lower()}.*' for website in exclude_websites]]):
        return
    url = item.get('link')
    if re.match(GOOGLE_NEWS_REGEX, url):
        url = requests.head(url).headers.get('location', url)
    return url
