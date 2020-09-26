import requests
from bs4 import BeautifulSoup

url = "https://yandex.ru/news/"
first_news_class = "news-card__annotation"


def parse():
    response = str(requests.get(url=url).content.decode())
    soup = BeautifulSoup(response[1 : len(response)-2], "html.parser")
    tmp = soup.find('div', class_=first_news_class)
    tmp = str(tmp)

    begin_text_index = tmp.find('>') + 1
    tmp_cut_left = tmp[begin_text_index:]
    end_text_index = tmp_cut_left.find('<')
    cut = tmp_cut_left[:end_text_index]
    return cut


if __name__ == '__main__':
    print(parse())
