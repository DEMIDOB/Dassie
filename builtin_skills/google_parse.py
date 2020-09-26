import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import concurrent.futures
import time

def parse(req):
    ret = "Error"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        wiki_info_T   = executor.submit(parse_wiki, req)
        google_info_T = executor.submit(parse_google, req)

        wiki_info   = wiki_info_T.result()
        google_info = google_info_T.result()

    ret = wiki_info if len(wiki_info) > len(google_info)  else google_info
    print("Used Wiki!" if len(wiki_info) > len(google_info)  else "Used Google!")

    return ret

def parse_google(req):
    ret = "Error"

    # response = str(requests.get("https://google.com/search?q={0}".format(req)).content.decode("ISO-8859-1"))
    response = str(requests.get("https://google.com/search?hl=ru&q={0}".format(req)).content.decode('cp1251'))

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

    print(description)

    return description


if __name__ == "__main__":
    start = time.perf_counter()
    print(parse("Алабай"))
    finish = time.perf_counter()
    print(finish-start)
