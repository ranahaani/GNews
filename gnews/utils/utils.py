import hashlib
import json
import logging

import pip
import pymongo
from pymongo import MongoClient

from gnews.utils.constants import AVAILABLE_LANGUAGES, AVAILABLE_COUNTRIES


def lang_mapping(lang):
    return AVAILABLE_LANGUAGES.get(lang)


def country_mapping(country):
    return AVAILABLE_COUNTRIES.get(country)


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


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
