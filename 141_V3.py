import requests
from bs4 import BeautifulSoup
import re
import time

# 整合版

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def crawler():
    resp = requests.get('http://141hongkong.com/forum-353-1.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 熱門 | 類別 | 標題 | 讚數 | 發帖人 | 留言數 | 瀏覽數|-----------------------------
    articles = soup.find_all('tbody', {'id': re.compile('normalthread_\d{7}')})

    report = [['類別', '標題', '讚數', '發帖人', '留言數', '瀏覽數']]
    for article in articles:
        # 類別 | 有些文章部會有分類===========================
        category = article.find('a', {'class': 'xst'}).previous_sibling.string
        # 標題===================================
        title = article.find('a', {'class': 'xst'}).text
        # 讚數 | ===========================
        thumb = article.find('span', {'class': 'xi1'}).text
        # 版主 | ===========================
        poster = article.find('td', {'class': 'by'}).cite.text
        # 留言數/瀏覽數 | ===========================
        message_number = article.find('a', {'class': 'xi2'}).text
        vist_number = article.find('a', {'class': 'xi2'}).next_sibling.text

        if category == '\n':
            report.append(['No_category', title, thumb,
                           poster, message_number, vist_number])
        else:
            report.append([category, title, thumb, poster,
                           message_number, vist_number])
    for data in report:
        print(data)


if __name__ == '__main__':
    crawler()
