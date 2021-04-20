import requests
from datetime import datetime
from bs4 import BeautifulSoup
from flask import Flask, make_response, request
from validator_collection import checkers

app = Flask(__name__)


# {
#     url1: {
#         s1: (7, t),
#         s2: (5, t),
#         s3: (6, t)
#     },
#     url2: {...}
# }

class Searches(object):
    def __init__(self):
        self.search_history = {}


def send_response(url, search_term, count):
    response_body = {
        "url": url,
        "search_term": search_term,
        "count": count,
    }
    resp = make_response(response_body)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


def update_search_history(url, search_term, count):
    if url not in sh.search_history:
        count_time = (count, datetime.utcnow())
        temp = {search_term: count_time}
        sh.search_history[url] = temp
    else:
        count_time = (count, datetime.utcnow())
        sh.search_history[url][search_term] = count_time


def is_within_time_span(count_time):
    search_time = count_time[1]
    now = datetime.utcnow()
    diff = (now - search_time).total_seconds()
    if diff < 0:
        raise RuntimeError("Our timing is off! Check your datetimes.")
    return diff < 30


@app.route('/')
def scrape():
    # print("sh:", sh)
    # print("sh.search_history:", sh.search_history)
    # get params from request body
    search_term = request.args.get("search_term", "")  # default to empty string
    url = request.args.get("url", "")  # default to empty string

    # look to see if we have made this search before
    if url in sh.search_history:
        if search_term in sh.search_history[url]:
            count_time = sh.search_history[url][search_term]
            if is_within_time_span(count_time):
                count = count_time[0]
                # return existing results
                print("we have already seen these results")
                return send_response(url, search_term, count)

    # validate url
    url_is_good = checkers.is_url(url, allow_empty = False)
    if not url_is_good:
        update_search_history(url, search_term, -1)
        # temp_results = {search_term: -1}
        # sh.search_history[url] = temp_results
        return send_response(url, search_term, -1)

    # try to make request
    try:
        req = requests.get(url, timeout=0.5)
        req.raise_for_status()
    except:
        # temp_results = {search_term: -1}
        # sh.search_history[url] = temp_results
        update_search_history(url, search_term, -1)
        return send_response(url, search_term, -1)

    parsed_request = request_to_list_of_text(req)
    count = count_search_terms(search_term, parsed_request)

    # temp_results = {search_term: count}
    # sh.search_history[url] = temp_results
    update_search_history(url, search_term, count)
    return send_response(url, search_term, count)


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
        # each element in indices is the beginning of an occurence of the search_term
        indices = [i for i in range(len(text_lowered)) if text_lowered.startswith(search_term, i)]
        count += len(indices)

    return count


sh = Searches()
app.run(debug=False, port=8000, host='0.0.0.0')
