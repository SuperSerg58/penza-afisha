import requests
from bs4 import BeautifulSoup
from datetime import datetime


def today_url():
    url = 'http://penza-afisha.ru/index.php?date='
    today = datetime.now()
    return url+today.strftime("%Y%m%d")


def get_html(url):
    """
    получаем HTML главной страницы сайта
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.ok:  # 200 - True, another 403, 404 - False
        return r.text
    else:
        print(r.status_code)


def get_films_url(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_="col2").find_all('div')
    films_urls = []
    for div in divs:
        """_________ФИЛЬМЫ___________"""
        try:
            trs = div.find('table', id="tab_films").find_all('tr')
            for td in trs:
                items = td.find_all('a')
                for item in items:
                    url = 'http://penza-afisha.ru/' + item.get('href') + '\n'
                    if 'http://penza-afisha.ru/films.php?' in url:
                        films_urls.append(url)

            return list(set(films_urls))

        except:
            return 'NO DATA'


def get_other_events(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_="col2").find_all('div', class_="text_col1")[2]
    events = []
    for div in divs:
        try:
            trs = div.find_all('tr')
            for td in trs:
                items = td.find_all('a')
                for item in items:
                    url = 'http://penza-afisha.ru/' + item.get('href') + '\n'
                    if 'orgs' in url:
                        continue
                    events.append(url)

            return list(set(events))

        except:
            return 'NO DATA'


def event_info(url):
    pass


def main():
    html = get_html(today_url())
    urls = get_films_url(html) + get_other_events(html)
    number = 1
    for i in urls:
        print(number, i)
        number+=1


if __name__ == '__main__':
    main()
