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


def get_seans_data(html):
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', id='screen').text.split()
    print(div)
    for item in div:
        print(item)


def main():
    url = 'http://penza-afisha.ru/seans.php?film=3744'
    html = get_html(url)
    get_seans_data(html)


if __name__ == '__main__':
    main()
