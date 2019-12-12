from bs4 import BeautifulSoup
import requests


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def get_event_info(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_='lc_fulf').find('div', class_='header_row').text
    table = soup.find('div', class_='lc_fulf').find('div', class_='text_col1')
    trs = table.find_all('td')
    production = trs[3].text
    creation_year = trs[5].text.strip()
    genre = trs[9].text.strip()
    role = trs[13].text.strip()
    description = trs[19].text.strip()
    print(description)


def main():
    url = 'http://penza-afisha.ru/films.php?f=3744'
    get_event_info(get_html(url))


if __name__ == '__main__':
    main()
