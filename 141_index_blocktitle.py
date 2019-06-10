import requests
from bs4 import BeautifulSoup
import re
import time
import csv


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def crawler():
    resp = requests.get('http://141hongkong.com/forum.php')

    soup = BeautifulSoup(resp.text, 'html5lib')
    # 目標 | 抓出首頁所有板塊名稱 | 主題-|帖子數----------------------------
    #blocks = soup.find_all('td', {'class': 'fl_g'})
    blocks = soup.find_all('div', {'class': 'flg'})
    datas = []
    for block in blocks:
        block_title = block.h2.text
        subblock = block.find_all('td', {'class': 'fl_g'})

        for block in subblock:
            title = block.dt.a.text
            try:
                subject_number = int(re.findall(
                    '\d+', block.dd.find_all('em')[0].text)[0])
                res_number = int(re.findall(
                    '\d+', block.dd.find_all('em')[1].text)[0])
            except:
                subject_number = 0
                res_number = 0
            print([block_title, title, subject_number, res_number])
            datas.append([block_title, title, subject_number, res_number])

    with open('index_blocktitle.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('版位主題', '版位名稱', '主題數', '帖子數'))
        for data in datas:
            writer.writerow((column for column in data))


if __name__ == '__main__':
    crawler()
