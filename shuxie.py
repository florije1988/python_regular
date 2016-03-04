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


def get_content(start_url):
    """
    所有开始的地方
    """
    next_url = start_url
    has_next = True
    while has_next:
        print next_url
        res = requests.get(next_url, headers=headers)
        if res.status_code == 200:
            content = res.text
        else:
            content = ''
        has_next, next_url = deal_page_content(content, start_url)


def deal_page_content(content, start_url):
    """
    处理内容
    """
    if content:
        soup = BeautifulSoup(content)
        # 首先获取分页。
        # print content
        pagination = soup.find('div', attrs={'class': 'page_turner'}).find_all('a')
        has_next = True if re.search(r'\?page=\d+', pagination[-1].get('href')) else False
        next_url = ''
        if has_next:
            next_url = pagination[-1].get('href')
        content_divs = soup.find_all('div', attrs={'style': 'background-color:#ddd;width:100%;'})
        for div in content_divs:
            img_url = '{base_url}{img_url}'.format(base_url=base_url, img_url=div.find('img', attrs={
                'class': 'scrollLoading rightimg'}).get('data-url'))
            print img_url
            save_img(img_url)
        return has_next, '{home_url}{next_url}'.format(home_url=start_url, next_url=next_url)
    else:
        return False, ''


def save_img(img_url):
    """
    保存数据
    """
    file_path = os.path.join(base_dir, re.search(r'\d+\.j?pe?n?g', img_url, re.IGNORECASE).group())
    if not os.path.exists(file_path):
        response = requests.get(img_url, stream=True, headers=headers)
        with open(file_path, "wb") as img:
            img.write(response.content)


if __name__ == '__main__':
    start_url = '{base_url}index.asp'.format(base_url=base_url)
    get_content(start_url)
