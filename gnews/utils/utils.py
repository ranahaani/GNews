import hashlib
import json
import logging
import re
import time
from urllib.parse import urlparse, quote
from selectolax.parser import HTMLParser

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
        print('url', url)
        decoded_url = decode_google_news_url(url)
        if decoded_url.get("status"):
            print("Decoded URL:", decoded_url["decoded_url"])
            return decoded_url['decoded_url']
        else:
            print("Error:", decoded_url["message"])
    return url


def get_base64_str(source_url):
    """
    Extracts the base64 string from a Google News URL.

    Parameters:
        source_url (str): The Google News article URL.

    Returns:
        dict: A dictionary containing 'status' and 'base64_str' if successful,
              otherwise 'status' and 'message'.
    """
    try:
        url = urlparse(source_url)
        path = url.path.split("/")
        if (
            url.hostname == "news.google.com"
            and len(path) > 1
            and path[-2] in ["articles", "read"]
        ):
            return {"status": True, "base64_str": path[-1]}
        return {"status": False, "message": "Invalid Google News URL format."}
    except Exception as e:
        return {"status": False, "message": f"Error in get_base64_str: {str(e)}"}


def fetch_data_attributes(url):
    """
    Fetches data attributes from the HTML content of the given URL.

    Parameters:
        url (str): The URL to fetch and parse.

    Returns:
        dict: A dictionary containing 'status', 'signature', 'timestamp' if successful,
              otherwise 'status' and 'message'.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        parser = HTMLParser(response.text)
        data_element = parser.css_first("c-wiz > div[jscontroller]")
        if data_element is None:
            return {"status": False, "message": "Failed to fetch data attributes."}

        return {
            "status": True,
            "signature": data_element.attributes.get("data-n-a-sg"),
            "timestamp": data_element.attributes.get("data-n-a-ts"),
        }
    except requests.exceptions.RequestException as req_err:
        return {"status": False, "message": f"Request error: {str(req_err)}"}
    except Exception as e:
        return {"status": False, "message": f"Unexpected error: {str(e)}"}


def get_decoding_params(base64_str):
    """
    Fetches signature and timestamp required for decoding from Google News.
    Tries the primary URL format first, and falls back to an alternative if necessary.

    Parameters:
        base64_str (str): The base64 string extracted from the Google News URL.

    Returns:
        dict: A dictionary containing 'status', 'signature', 'timestamp', and 'base64_str' if successful,
              otherwise 'status' and 'message'.
    """
    urls = [
        f"https://news.google.com/articles/{base64_str}",
        f"https://news.google.com/rss/articles/{base64_str}"
    ]

    for url in urls:
        result = fetch_data_attributes(url)
        if result["status"]:
            # Add the base64 string to the result on success
            result["base64_str"] = base64_str
            return result

    return {
        "status": False,
        "message": "Failed to fetch decoding parameters from both URLs."
    }


def send_post_request(url, headers, payload):
    """
    Sends a POST request to the given URL with the specified headers and payload.

    Parameters:
        url (str): The URL to send the POST request to.
        headers (dict): The request headers.
        payload (str): The payload to send in the request body.

    Returns:
        requests.Response: The response object from the request.
    """
    response = requests.post(url, headers=headers, data=f"f.req={quote(json.dumps([[payload]]))}")
    response.raise_for_status()
    return response


def parse_response(response):
    """
    Parses the response from the server and extracts the decoded URL.

    Parameters:
        response (requests.Response): The response object to parse.

    Returns:
        str: The decoded URL if parsing is successful.

    Raises:
        JSONDecodeError, IndexError, TypeError: If any parsing error occurs.
    """
    parsed_data = json.loads(response.text.split("\n\n")[1])[:-2]
    return json.loads(parsed_data[0][2])[1]


def decode_url(signature, timestamp, base64_str):
    """
    Decodes the Google News URL using the signature and timestamp.

    Parameters:
        signature (str): The signature required for decoding.
        timestamp (str): The timestamp required for decoding.
        base64_str (str): The base64 string from the Google News URL.

    Returns:
        dict: A dictionary containing 'status' and 'decoded_url' if successful,
              otherwise 'status' and 'message'.
    """
    try:
        url = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
        payload = [
            "Fbv4je",
            f'["garturlreq",[["X","X",["X","X"],null,null,1,1,"US:en",null,1,null,null,null,null,null,0,1],"X","X",1,[1,1,1],1,1,null,0,0,null,0],"{base64_str}",{timestamp},"{signature}"]',
        ]
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        # Send POST request and get the response
        response = send_post_request(url, headers, payload)

        # Parse the response and extract the decoded URL
        decoded_url = parse_response(response)

        return {"status": True, "decoded_url": decoded_url}

    except requests.exceptions.RequestException as req_err:
        return {"status": False, "message": f"Request error in decode_url: {str(req_err)}"}
    except (json.JSONDecodeError, IndexError, TypeError) as parse_err:
        return {"status": False, "message": f"Parsing error in decode_url: {str(parse_err)}"}
    except Exception as e:
        return {"status": False, "message": f"Error in decode_url: {str(e)}"}


def decode_google_news_url(source_url, interval=None):
    """
    Decodes a Google News article URL into its original source URL.

    Parameters:
        source_url (str): The Google News article URL.
        interval (int, optional): Delay time in seconds before decoding to avoid rate limits.

    Returns:
        dict: A dictionary containing 'status' and 'decoded_url' if successful,
              otherwise 'status' and 'message'.
    """
    try:
        base64_response = get_base64_str(source_url)
        if not base64_response["status"]:
            return base64_response

        decoding_params_response = get_decoding_params(base64_response["base64_str"])
        if not decoding_params_response["status"]:
            return decoding_params_response

        decoded_url_response = decode_url(
            decoding_params_response["signature"],
            decoding_params_response["timestamp"],
            decoding_params_response["base64_str"],
        )
        if interval:
            time.sleep(interval)

        return decoded_url_response
    except Exception as e:
        return {
            "status": False,
            "message": f"Error in decode_google_news_url: {str(e)}",
        }
