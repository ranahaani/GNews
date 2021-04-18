import pip

from gnews.utils.constants import languages, countries


def lang_mapping(lang):
    return languages.get(lang)


def country_mapping(country):
    return countries.get(country)


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])
