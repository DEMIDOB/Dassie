import urllib.parse

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import concurrent.futures
import time

from duckduckgo_search import DDGS


def parse(req):
    ret = "Error"

    wiki_info = ""
    google_info = ""

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            wiki_info_T   = executor.submit(parse_wiki, req)
            google_info_T = executor.submit(parse_google, req)

            wiki_info   = wiki_info_T.result()
            google_info = google_info_T.result()
    except Exception as e:
        print("Failed to complete the search:", e)

    ret = wiki_info if len(wiki_info) > len(google_info)  else google_info
    print("Used Wiki!" if len(wiki_info) > len(google_info)  else "Used Google!")

    return ret

def parse_google(req):
    return parse_ddg(req)
    ret = "Error"

    response = str(requests.get("https://google.com/search?q={0}".format(req)).content.decode("ISO-8859-1"))
    # response = str(requests.get("https://google.com/search?hl=ru&q={0}".format(req)).content.decode('cp1251'))
    print(response)
    soup = BeautifulSoup(response, features="html.parser")
    # first_title = soup.find('div', class_='BNeawe vvjwJb AP7Wnd')
    description = (soup.find('div', class_='BNeawe s3v9rd AP7Wnd')).find('div', class_='BNeawe s3v9rd AP7Wnd')
    # search_string_title = '<div class="BNeawe vvjwJb AP7Wnd">'
    search_string_descr = '<div class="BNeawe s3v9rd AP7Wnd">'
    str_description = str(description)
    description_start_index = str_description.find(search_string_descr) + len(search_string_descr)
    description_cut_left = str_description[description_start_index:]
    description_end_index = description_cut_left.find('<')
    description_cut = description_cut_left[:description_end_index]
    # print(description_cut)
    description_str = str(description_cut)
    ret = description_str

    print(ret)

    return ret


def parse_ddg(req):
    result = ""
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://duckduckgo.com/',
            'Sec-Fetch-Mode': 'navigate',
            'Host': 'html.duckduckgo.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Dest': 'document',
            'Connection': 'keep-alive',
        }

        params = {
            'q': req,
        }

        print(params)

        response = requests.get('https://html.duckduckgo.com/html', params=params, headers=headers).text

        most_relevant_description, mrd_score = "", 0

        soup = BeautifulSoup(response, features="html.parser")
        descriptions = (soup.find_all("a", class_="result__snippet"))
        for i, description in enumerate(descriptions):
            # calculate score:
            current_score = len(description) * (len(descriptions) - i) / len(descriptions)
            if current_score > mrd_score:
                mrd_score = current_score
                most_relevant_description = description.text

        return most_relevant_description

    except Exception as e:
        print("DDG search failed:", e)

    return result


def parse_wiki(req):
    wikiUrl = "https://ru.wikipedia.org/w/api.php"
    response = requests.get(wikiUrl, params={"action": "opensearch", "search": str(req), "prop": "info", "format": "xml", "inprop": "url"})
    response_str = str(response.content.decode('utf-8'))
    tree = etree.fromstring(response_str)

    succeded = not response_str.endswith("/></SearchSuggestion>")
    if not succeded:
        return ""

    sectionXml = tree
    pageName = sectionXml[2][0][0].text

    pageParams = {
        "action": "parse",
        "page": pageName,
        "format": "json"
    }

    respPage = requests.get(wikiUrl, pageParams)
    pageJSON = respPage.json()
    pageHTML = pageJSON["parse"]["text"]["*"]

    wikiSoup = BeautifulSoup(pageHTML, features="html.parser")
    descriptionNP = str(wikiSoup.find('p'))

    description = ""
    writing = False

    for symbol in descriptionNP:
        if symbol in ('<', '['):
            writing = False
        elif symbol in ('>', ']'):
            writing = True
            continue

        if writing:
            description += symbol

    # print(description)

    return description


if __name__ == "__main__":
    start = time.perf_counter()
    print(parse("кто такой навальный"))
    finish = time.perf_counter()
    print(finish-start)
    # print(parse_ddg("путин"))
    # print(parse_wiki("путин"))
