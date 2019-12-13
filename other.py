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


def get_events_info(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_='lc_fulf').find('div', class_='header_row').text
    divs = soup.find('div', class_='lc_fulf').find('div', class_='text_col1').find_all('td')

    try:
        info = divs[1].text.split()[:-5]
        info = ' '.join(info)
    except:
        info = 'No information'

    try:
        description = divs[14].text
    except:
        description = 'No information'

    data = {
        'Название': title,
        'Информация': info,
        'Описание': description
    }

    return data


def main():
    url = 'http://penza-afisha.ru/action.php?id=77824'
    html = get_html(url)
    data = get_events_info(html)
    print(data)


if __name__ == '__main__':
    main()
