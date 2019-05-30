import requests
from bs4 import BeautifulSoup
import re
import time


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def crawler():
    resp = requests.get('http://141hongkong.com/forum-353-1.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 熱門 | 類別 | 標題 | 讚數 | 發帖人 | 留言數 | 瀏覽數|-----------------------------
    articles = soup.find_all('tbody', {'id': re.compile('normalthread_\d{7}')})

    for article in articles:

        # # 標題===================================
        # title = article.find('a', {'class': 'xst'})
        # print(title.text)
        # # 類別 | 有些文章部會有分類===========================
        # category = article.find('a', {'class': 'xst'}).previous_sibling
        # if category.string == '\n':
        #     print(title.string, 'No_category')
        # else:
        #     print(title.string, category.string)
        # # 版主 | ===========================
        # poster = article.find('td', {'class': 'by'}).cite
        # print(poster.text)
        # # 讚數 | ===========================
        # thumb = article.find('span', {'class': 'xi1'})
        # print('讚數', thumb.text)

        # # 留言數/瀏覽數 | ===========================
        # message = article.find('a', {'class': 'xi2'})
        # vistnumber = message.next_sibling
        # print('留言數', message.text,
        #       '瀏覽量', vistnumber.text)

        # test.append(category.string)

        # if category:
        #     print(title.text, category.text)
        # else:
        #     print(None)


if __name__ == '__main__':
    crawler()
