import requests
from bs4 import BeautifulSoup
import re
import time
import csv


time = time.strftime("%m_%d_%H", time.localtime())
day = time.split('_')[1]
hour = time.split('_')[2]


def crawler():
    resp = requests.get('http://141hongkong.com/forum.php')
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 目標| 抓出排行榜|版名|在線人數|今日帖數-----------------------------
    leaderboards = soup.find('div', {'class': 'module'})
    list = []
    count = 0
    for leaderboard in leaderboards:

        title = leaderboard.strong.text
        online_number = leaderboard.find('small', {'style': 'color:red'}).text
        online_number = int(re.findall('\d+', online_number)[0])
        article_number = leaderboard.find(
            'small', {'style': 'color:blue'}).text
        article_number = int(re.findall('\d+', article_number)[0])
        print([title, online_number, article_number])
        list.append([day, hour, count, title, online_number, article_number])
        count += 1

    with open(time+'leaderboard.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('日', '時', '排名', '板塊', '在線人數', '今日帖數'))
        for data in list:
            writer.writerow((column for column in data))


if __name__ == '__main__':
    crawler()
