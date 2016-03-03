# -*- coding: utf-8 -*-
__author__ = 'florije'

import re
import os
import requests
from bs4 import BeautifulSoup


base_dir = 'shuxie'
base_url = 'http://shouxieke.net/zile/'

user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36"
headers = {
    "User-Agent": user_agent,
    "Host": "pachong.org",
    "Referer": "http://pachong.org/"
}


def get_web_content(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.content  # .decode('GBK').encode('utf-8')  # 处理下比较好，暂时先这样。
    else:
        return ''


def deal_content(content):
    if content:
        soup = BeautifulSoup(content)
        # 首先获取分页。
        content_divs = soup.find_all('div', attrs={'style': 'background-color:#ddd;width:100%;'})
        for div in content_divs:
            img_url = '{base_url}{img_url}'.format(base_url=base_url, img_url=div.find('img', attrs={'class': 'scrollLoading rightimg'}).get('data-url'))
            print img_url
            save_img(img_url)
    else:
        return ''


def save_img(img_url):
    file_path = os.path.join(base_dir, re.search(r'\d{18}\.jpg', img_url).group())
    if not os.path.exists(file_path):
        response = requests.get(img_url, stream=True, headers=headers)
        with open(file_path, "wb") as img:
            img.write(response.content)

if __name__ == '__main__':
    start_url = '{base_url}index.asp'.format(base_url=base_url)
    content = get_web_content(start_url)
    print content
    deal_content(content)
