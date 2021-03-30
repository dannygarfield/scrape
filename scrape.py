import requests
from bs4 import BeautifulSoup
import re
from flask import Flask

app = Flask(__name__)

# url = "https://www.mela-health.com/"
url = "http://localhost:3000/"
search_term = "MY NAME IS DANNY"


@app.route('/')
def hello_world():
    return count_search_terms(url, search_term)


req = requests.get(url)
page_content = req.content.decode(encoding='UTF-8')
soup = BeautifulSoup(page_content, 'html.parser')
lst = [text for text in soup.stripped_strings]


def count_search_terms(url, search_term):
    count = 0
    search_term = search_term.lower()

    req = requests.get(url)
    # print(req.status_code)
    # print(req.text)
    page_content = req.content.decode(encoding='UTF-8')

    soup = BeautifulSoup(page_content, 'html.parser')
    # body = soup.find('body')
    # all_text = soup.get_text().lower()
    print(soup.stripped_strings)
    text_list = [text for text in soup.stripped_strings]

    for text in text_list:
        text_lowered = text.lower()
        for i in range(len(text_lowered)):
            if text.startswith(search_term, i):
                print(text_lowered)
                count += 1

    print("count:", count)
    resp = {"count": count}
    return resp


app.run(debug=True, port=8000, host='0.0.0.0')
