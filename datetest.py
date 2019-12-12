from datetime import datetime


def today_url():
    url = 'http://penza-afisha.ru/index.php?date='
    today = datetime.now()
    return url+today.strftime("%Y%m%d")

print(today_url())