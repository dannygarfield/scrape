import requests
from bs4 import BeautifulSoup
import re
from flask import Flask, make_response, request, abort
from validator_collection import validators, checkers, errors

app = Flask(__name__)


@app.route('/')
def scrape():
    # get params from request body
    search_term = request.args.get("search_term", "")  # default to empty string
    url = request.args.get("url", "google.com")  # default to empty string

    # validate url
    url_is_good = checkers.is_url(url, allow_empty = False)
    if not url_is_good:
        response_body = {
            "url": url,
            "search_term": search_term,
            "count": -1,
            "error_code": "bad url given"
        }
        resp = make_response(response_body)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp

    # try to make request
    try:
        req = requests.get(url, timeout=0.5)
        req.raise_for_status()
    except:
        response_body = {
            "url": url,
            "search_term": search_term,
            "count": -1,
            "error_code": "bad url given"
        }
        resp = make_response(response_body)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp

    parsed_request = request_to_list_of_text(req)
    count = count_search_terms(search_term, parsed_request)

    response_body = {
        "url": url,
        "search_term": search_term,
        "count": count
    }
    resp = make_response(response_body)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


def request_to_list_of_text(req):
    page_content = req.content.decode(encoding='UTF-8')
    parsed_html = BeautifulSoup(page_content, 'html.parser')
    text_list = [text for text in parsed_html.stripped_strings]
    return text_list


def count_search_terms(search_term, text_list):
    count = 0
    search_term = search_term.lower()
    # loop through all text
    for text in text_list:
        text_lowered = text.lower()
        # find all instances of our search_term in each text element on the page
        indices = [i for i in range(len(text_lowered)) if text_lowered.startswith(search_term, i)]
        count += len(indices)

    return count


app.run(debug=True, port=8000, host='0.0.0.0')
