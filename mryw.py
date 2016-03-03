# -*- coding: utf-8 -*-
__author__ = 'florije'

import re
import os
import base64
import requests
from bs4 import BeautifulSoup

# res = requests.get('http://www.luoo.net/music/799')
# print res.content
#
# re_res = re.search(r'var pl = ".*";', res.content)
# if re_res:
#     print re_res.group()[10:-2]


base_dir = 'meiriyiwen'
base_url = 'http://voice.meiriyiwen.com'
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36"
headers = {
    "User-Agent": user_agent,
    "Host": "pachong.org",
    "Referer": "http://pachong.org/"
}


def get_volume_list():
    """
    get volume list
    """
    www_res = requests.get('{}/voice/list_all'.format(base_url), headers=headers)
    soup = BeautifulSoup(www_res.content)
    list_div = soup.find('div', attrs={'class': 'list_table'})
    res_dict = []
    for row in list_div.find('table').find_all('tr'):
        cells = row.findAll("td")
        if cells:  # 去掉头
            name = cells[0].text.strip()
            href = cells[0].find('a').get('href')
            vid = href.split('?')[1][4:]
            author = cells[1].text.strip()
            anchor = cells[2].text.strip()
            res_dict.append({'vid': vid, 'name': name, 'url': '{base}{href}'.format(base=base_url, href=href), 'author': author, 'anchor': anchor})
    return res_dict


def get_mp3_list(volume_list):
    """
    get mp3 list
    """
    for volume in volume_list:
        www_res = requests.get(volume.get('url'))
        soup = BeautifulSoup(www_res.content)
        music_file = re.search(r'\?url=[A-Za-z0-9=]+&', soup.find('p', attrs={'class': 'p_file'}).find('embed').get('src'))
        if music_file:
            print base64.b64decode(music_file.group()[5:-1])
            download_mp3(volume.get('vid'), base64.b64decode(music_file.group()[5:-1]))


def download_mp3(dir_name, url):
    """
    download mp3
    """
    create_dir(dir_name)
    # f = urllib2.urlopen(url)
    response = requests.get(url, stream=True, headers=headers)
    file_path = os.path.join(base_dir, dir_name, re.search(r'\d{8}\.mp3', url).group())
    if not os.path.exists(file_path):
        with open(file_path, "wb") as mp3:
            mp3.write(response.content)


def create_dir(dir_name):
    """
    create_dir
    """
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    if not os.path.exists(os.path.join(base_dir, dir_name)):
        os.mkdir(os.path.join(base_dir, dir_name))


if __name__ == '__main__':
    volume_list = get_volume_list()
    get_mp3_list(volume_list)
