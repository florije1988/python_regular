# -*- coding: utf-8 -*-
__author__ = 'florije'

import re
import os
import requests
from bs4 import BeautifulSoup


base_url = 'http://shouxieke.net/zile/'


def get_web_content(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.content  # .decode('GBK').encode('utf-8')  # 处理下比较好，暂时先这样。
    else:
        return ''


def deal_content(content):
    if content:
        soup = BeautifulSoup(content)
        content_divs = soup.find_all('div', attrs={'style': 'background-color:#ddd;width:100%;'})
        for div in content_divs:
            img = '{base_url}{img_url}'.format(base_url=base_url, img_url=div.find('img', attrs={'class': 'scrollLoading rightimg'}).get('data-url'))
            print img
    else:
        return ''

if __name__ == '__main__':
    start_url = '{base_url}index.asp'.format(base_url=base_url)
    content = get_web_content(start_url)
    print content
    deal_content(content)
