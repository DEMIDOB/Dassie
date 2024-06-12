import urllib.parse
import xml

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import concurrent.futures
import time

from duckduckgo_search import DDGS


def parse(req):
    ret = "Error"

    wiki_info = ""
    duck_info = ""

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            wiki_info_T   = executor.submit(parse_wiki, req)
            ddg_info_T = executor.submit(parse_ddg, req)

            wiki_info   = wiki_info_T.result()
            duck_info = ddg_info_T.result()
    except Exception as e:
        print("Failed to complete the search:", e)

    # print(f"Wiki told: {wiki_info}")
    # print(f"Duck cryacked: {duck_info}")
    ret = wiki_info if len(wiki_info) > len(duck_info)  else duck_info
    # print("Used Wiki!" if len(wiki_info) > len(duck_info)  else "Used Duck!")

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
    response = requests.get(wikiUrl, params={"action": "opensearch", "search": str(req), "format": "xml"})
    response_str = str(response.content.decode('utf-8'))
    # print(response_str)
    tree = etree.fromstring(response_str)

    succeded = not response_str.endswith("/></SearchSuggestion>")
    if not succeded:
        return ""

    sectionXml: xml.etree.ElementTree.Element = tree
    page_name = ""

    for c in sectionXml:
        # print(c.tag)
        if c.tag.endswith("Section"):
            for item in c:
                for item_field in item:
                    if item_field.tag.endswith("Url"):
                        page_name = urllib.parse.unquote(str(item_field.text.split("/")[-1].strip()))
                        break
                if page_name:
                    break
            if page_name:
                break

    if not page_name:
        return ""

    pageParams = {
        "action": "parse",
        "page": page_name,
        "format": "json"
    }

    respPage = requests.get(wikiUrl, pageParams)
    pageJSON = respPage.json()
    pageHTML = pageJSON["parse"]["text"]["*"]

    wiki_soup = BeautifulSoup(pageHTML, features="html.parser")

    description_raw = ""

    for par in wiki_soup.find_all("p"):
        if str(par).strip().startswith("<p><b>"):
            description_raw = par.text
            break

    description = ""
    writing = True

    for symbol in description_raw:
        if symbol in ('<', '['):
            writing = False
        elif symbol in ('>', ']'):
            writing = True
            continue

        if writing:
            description += symbol

    # print(description)

    return description


def _main():
    # res = parse_wiki("фильм ")
    # print(res)
    # return

    start = time.perf_counter()
    print(parse("кто z"))
    finish = time.perf_counter()
    print(finish-start)
    # print(parse_ddg("путин"))
    # print(parse_wiki("путин"))


if __name__ == "__main__":
    _main()