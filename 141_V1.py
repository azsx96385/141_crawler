import requests
from bs4 import BeautifulSoup
import re
import time


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def crawler():
    resp = requests.get('http://141hongkong.com/forum.php')
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 目標| 抓出排行榜|版名|在線人數|今日帖數-----------------------------
    leaderboards = soup.find('div', {'class': 'module'}).children

    for leaderboard in leaderboards:
        list = []
        for data in leaderboard:
            if data.name == 'strong':
                strong = leaderboard.find('strong')
                list.append(strong.text)
                # print(strong.text)

            if data.name == 'small':
                smalls = leaderboard.find_all('small')
                for small in smalls:
                    list.append(small.text)
                    # print(small.text)
        print(list)

    #     # for data in leaderboard:
        #     print(data)
    #     # print([s for s in leaderboard.stripped_strings])
    #     print(leaderboard.div.div)


if __name__ == '__main__':
    crawler()
