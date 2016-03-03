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
            content = res.content  # .decode('GBK').encode('utf-8')
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
        print content
        pagination = soup.find('div', attrs={'class': 'page_turner'}).find_all('a')
        has_next = True if re.search(r'\?page=\d+', pagination[-1].get('href')) else False
        next_url = ''
        if has_next:
            next_url = pagination[-1].get('href')
        content_divs = soup.find_all('div', attrs={'style': 'background-color:#ddd;width:100%;'})
        for div in content_divs:
            img_url = '{base_url}{img_url}'.format(base_url=base_url, img_url=div.find('img', attrs={'class': 'scrollLoading rightimg'}).get('data-url'))
            print img_url
            save_img(img_url)
        return has_next, '{home_url}{next_url}'.format(home_url=start_url, next_url=next_url)
    else:
        return False, ''


def save_img(img_url):
    """
    保存数据
    """
    file_path = os.path.join(base_dir, re.search(r'\d{18}\.jpg', img_url).group())
    if not os.path.exists(file_path):
        response = requests.get(img_url, stream=True, headers=headers)
        with open(file_path, "wb") as img:
            img.write(response.content)

if __name__ == '__main__':
    # start_url = '{base_url}index.asp'.format(base_url=base_url)
    # get_content(start_url)

    html = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml"  xml:lang="zh-CN" lang="zh-CN">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
      <link href=http://shouxieke.net/favicon.ico rel="shortcut icon">

        <title>������ - ��˵��д �������� - �����д����ͼƬ</title>
        <meta name="description" content="����һ������ṩ��д���ֵ���վ��������������ύ����д���룬վ�����ڿ���ʱ��д�ú󷢲�������ʱ���ύ�����䣬����ʱ��������䷢��д�õ�ͼƬ�����κν��黶ӭ���ԣ���ϲ����վ����ӭ����������" />

        <meta name="keywords" content="Ӳ���鷨,�ֱ���,Ӳ����,������վ,д����Ƶ,������Ƶ,��дף��,��д����,��д���,������,�����鷨,��д,��д����ͼƬ,����д,���Գ�д,��д��,��д����,��д����,����,�鷨��ϰ,�鷨����,����д" />
        <link rel="stylesheet" id="css" type="text/css" href="inc/style.css" title="cssfile" />
        <link rel="stylesheet" id="css" type="text/css" href="inc/flexslider.css" title="cssfile" />
    <script type="text/javascript" src="plug-ins/dingcai/js/jquery.min.js"></script>
    <script type="text/javascript" src="plug-ins/dingcai/js/dingcai.js"></script>
    <script type="text/javascript" src="plug-ins/dingcai/js/jquery.scrollLoading-min.js"></script>
    <script type="text/javascript" src="plug-ins/dingcai/js/jquery.flexslider-min.js"></script>
    <script>
    $(function() {
        $(".scrollLoading").scrollLoading();
    });
    $(function() {
        $(".flexslider").flexslider({
            slideshowSpeed: 4000, //չʾʱ����ms
            animationSpeed: 400, //����ʱ��ms
            touch: true //�Ƿ�֧�ִ�������
        });
    });
    </script>

    <Script language="javascript" type="text/javascript">
    function openwindow(url,name,iWidth,iHeight)
     {
      var url;                                 //ת����ҳ�ĵ�ַ;
      var name;                           //��ҳ���ƣ���Ϊ��;
      var iWidth;                          //�������ڵĿ��;
      var iHeight;                        //�������ڵĸ߶�;
      var iTop = (window.screen.availHeight-30-iHeight)/2;       //��ô��ڵĴ�ֱλ��;
      var iLeft = (window.screen.availWidth-10-iWidth)/2;           //��ô��ڵ�ˮƽλ��;
      window.open(url,name,'height='+iHeight+',,innerHeight='+iHeight+',width='+iWidth+',innerWidth='+iWidth+',top='+iTop+',left='+iLeft+',toolbar=no,menubar=no,scrollbars=no,resizeable=no,location=no,status=no');
     }
    </Script>
    </head>

    <BODY>
    <center>
    <div class="content">

    <div class="keeptop">
    <div class="toplogo"><img src=images/logo.jpg alt="������" title="������"></div>
    <div class="topmenu">
    <UL class="nav">
    <LI><A href="index.asp">��ҳ</A></LI>
    <LI><A href="?action=hot"><img src=images/ding.png style="margin-bottom:-2px;">������</A></LI>
    <LI><A href="?action=video">Ӱ��</A></LI>
    <LI><A href="?key=%D0%C4%C2%B7%C0%FA%B3%CC">�ĵ�</A></LI>
    <LI><A href="index.asp?id=1269">����Ƭ����</A></LI>
    <LI><A href="index.asp?id=1474">����ʱ��</A></LI>
    <LI><A href="index.asp?id=1475">�ղؼ�</A></LI>
    <LI><A href="index.asp?id=662">����</A></LI>
    <LI><a href="JavaScript:openwindow('add.asp','add','360','480')" style="color:#fff;border:#ffCC00 solid 0px;padding:5px;background-color:#FF3B47"> ������</a></LI>
    </UL>
    </div>
    </div>
    <div class="split"></div>


      <div class="left" style="text-align:left;padding:18px;padding-top:6px;text-decoration:none;word-wrap:break-word;">

      <hr style="margin-top:15px;height:1px;border:none;border-top:1px solid #E2E2E2;">
      <center><span style="color:#ffffff;background-color:#AAB0C6;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:4px 16px 4px 16px;"> <b>ͼ��</b> | <a href="list.asp?page=7" style="color:#fff;" title="�л����б�ģʽ">�б�</a></span></center>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1387 target="_blank"><b class="a_title">ǩ��</b></a> / ���� / 2015-12-13
    </p>
      <center><a href="index.asp?id=1387" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512141651332649.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ����...<br><br>



    <a href='javascript:void(0)' onclick='digg(1387,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1387'>0</span>��</a>

    <a href="index.asp?id=1387#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1387 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1385 target="_blank"><b class="a_title">лл����</b></a> / �����û� / 2015-12-11
    </p>
      <center><a href="index.asp?id=1385" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512141650565472.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    Ҷ�M...<br><br>



    <a href='javascript:void(0)' onclick='digg(1385,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1385'>1</span>��</a>

    <a href="index.asp?id=1385#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1385 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1384 target="_blank"><b class="a_title">���������˭��Ķ�ã�Ҳ���˭��Ķ�...</b></a> / �����û� / 2015-12-11
    </p>
      <center><a href="index.asp?id=1384" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512141654035225.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ������
    ���˭��Ķ�ã�Ҳ���˭��Ķ�...<br><br>



    <a href='javascript:void(0)' onclick='digg(1384,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1384'>1</span>��</a>

    <a href="index.asp?id=1384#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1384 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1383 target="_blank"><b class="a_title">վ������д������ɶ</b></a> / �����û� / 2015-12-10
    </p>
      <center><a href="index.asp?id=1383" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512141650378841.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ���...<br><br>



    <a href='javascript:void(0)' onclick='digg(1383,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1383'>0</span>��</a>

    <a href="index.asp?id=1383#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1383 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1382 target="_blank"><b class="a_title">����</b></a> / �����û� / 2015-12-10
    </p>
      <center><a href="index.asp?id=1382" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512141650220239.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ���ݷ�...<br><br>



    <a href='javascript:void(0)' onclick='digg(1382,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1382'>0</span>��</a>

    <a href="index.asp?id=1382#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1382 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1381 target="_blank"><b class="a_title">��д������</b></a> / ���� / 2015-12-10
    </p>
      <center><a href="index.asp?id=1381" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512141648308245.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    Τ��...<br><br>



    <a href='javascript:void(0)' onclick='digg(1381,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1381'>0</span>��</a>

    <a href="index.asp?id=1381#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1381 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1380 target="_blank"><b class="a_title">лл������</b></a> / Alzyan / 2015-12-10
    </p>
      <center><a href="index.asp?id=1380" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512100937542413.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ����&#19886;...<br><br>



    <a href='javascript:void(0)' onclick='digg(1380,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1380'>4</span>��</a>

    <a href="index.asp?id=1380#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1380 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1379 target="_blank"><b class="a_title">�ҵ����֣�������ллվ������~...</b></a> / ������ / 2015-12-9
    </p>
      <center><a href="index.asp?id=1379" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512100741494754.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    �ҵ����֣�������
    ллվ������~...<br><br>



    <a href='javascript:void(0)' onclick='digg(1379,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1379'>1</span>��</a>

    <a href="index.asp?id=1379#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1379 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1378 target="_blank"><b class="a_title">�鷳վ����д������ л��</b></a> / ��СĪ / 2015-12-8
    </p>
      <center><a href="index.asp?id=1378" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091010141437.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ���鲩...<br><br>



    <a href='javascript:void(0)' onclick='digg(1378,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1378'>0</span>��</a>

    <a href="index.asp?id=1378#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1378 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1377 target="_blank"><b class="a_title">���Ǻ�...</b></a> / Ī�� / 2015-12-8
    </p>
      <center><a href="index.asp?id=1377" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091010278023.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ���Ǻ�...<br><br>



    <a href='javascript:void(0)' onclick='digg(1377,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1377'>0</span>��</a>

    <a href="index.asp?id=1377#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1377 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1375 target="_blank"><b class="a_title">����������</b></a> / �𵰻һ� / 2015-12-7
    </p>
      <center><a href="index.asp?id=1375" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091005509332.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    �Ϲ���Ѱ...<br><br>



    <a href='javascript:void(0)' onclick='digg(1375,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1375'>1</span>��</a>

    <a href="index.asp?id=1375#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1375 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1374 target="_blank"><b class="a_title">�ޣ�ллѽ~��</b></a> / �����ܹ�С���� / 2015-12-7
    </p>
      <center><a href="index.asp?id=1374" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091009595774.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    �����ܹ�С����...<br><br>



    <a href='javascript:void(0)' onclick='digg(1374,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1374'>0</span>��</a>

    <a href="index.asp?id=1374#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1374 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1373 target="_blank"><b class="a_title">����</b></a> / �����û� / 2015-12-7
    </p>
      <center><a href="index.asp?id=1373" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091005041447.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ��͢��...<br><br>



    <a href='javascript:void(0)' onclick='digg(1373,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1373'>0</span>��</a>

    <a href="index.asp?id=1373#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1373 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1372 target="_blank"><b class="a_title">����</b></a> / �����û� / 2015-12-7
    </p>
      <center><a href="index.asp?id=1372" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091006245366.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ���ɽ�...<br><br>



    <a href='javascript:void(0)' onclick='digg(1372,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1372'>0</span>��</a>

    <a href="index.asp?id=1372#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1372 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1371 target="_blank"><b class="a_title">֧��</b></a> / �곤ôô�� / 2015-12-6
    </p>
      <center><a href="index.asp?id=1371" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091009435704.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ֧��...<br><br>



    <a href='javascript:void(0)' onclick='digg(1371,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1371'>1</span>��</a>

    <a href="index.asp?id=1371#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1371 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1370 target="_blank"><b class="a_title">������...</b></a> / ������ / 2015-12-6
    </p>
      <center><a href="index.asp?id=1370" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512091004380277.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ������...<br><br>



    <a href='javascript:void(0)' onclick='digg(1370,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1370'>0</span>��</a>

    <a href="index.asp?id=1370#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1370 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1369 target="_blank"><b class="a_title">����</b></a> / ľľ / 2015-12-6
    </p>
      <center><a href="index.asp?id=1369" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512062125596186.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ������...<br><br>



    <a href='javascript:void(0)' onclick='digg(1369,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1369'>1</span>��</a>

    <a href="index.asp?id=1369#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1369 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1368 target="_blank"><b class="a_title">�ǫh...</b></a> / ������ / 2015-12-4
    </p>
      <center><a href="index.asp?id=1368" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512062125229935.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    �ǫh...<br><br>



    <a href='javascript:void(0)' onclick='digg(1368,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1368'>1</span>��</a>

    <a href="index.asp?id=1368#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1368 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1365 target="_blank"><b class="a_title">�ƽ�...</b></a> / ���� / 2015-12-4
    </p>
      <center><a href="index.asp?id=1365" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512062124396809.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    �ƽ�...<br><br>



    <a href='javascript:void(0)' onclick='digg(1365,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1365'>0</span>��</a>

    <a href="index.asp?id=1365#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1365 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>

    <div style="background-color:#ddd;width:100%;">
     <p style="padding:10px 10px 0px 10px;"><a href=index.asp?id=1364 target="_blank"><b class="a_title">������лл</b></a> / �԰� / 2015-12-4
    </p>
      <center><a href="index.asp?id=1364" title="�鿴ȫ��" target="_blank">
    <img class="scrollLoading rightimg" data-url="upload/201512062124582902.jpg" src="images/load.gif"></a>
    </center>
    <p style="padding:15px;">
    ���ǿ...<br><br>



    <a href='javascript:void(0)' onclick='digg(1364,1)' style="color:#ffffff;background-color:#FF3B47;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title="ϲ���Ͷ���ǰ��ȥ��"><img src=images/ding.png style="margin-bottom:-3px;height:15px;"> ����<span class='ding1364'>0</span>��</a>

    <a href="index.asp?id=1364#comments" target="_blank" style="color:#ffffff;background-color:#5071B8;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;" title=""><img src=images/ping.png style="margin-bottom:-3px;height:15px;"> ����</a>

    <a href=index.asp?id=1364 target="_blank"><span style="color:#ffffff;background-color:#55648B;-moz-border-radius: 2px;-webkit-border-radius:2px;padding:6px;"><img src=images/all.png style="margin-bottom:-3px;height:15px;"> �Ķ�ȫ�� </span></a>


    </p>
      </div>
    <div class="page_turner"><a title="��ҳ" href="?page=1">1...</a><a title="��2ҳ" href="?page=2">2</a><a title="��3ҳ" href="?page=3">3</a><a title="��4ҳ" href="?page=4">4</a><a title="��5ҳ" href="?page=5">5</a><a title="��6ҳ" href="?page=6">6</a><a title="��7ҳ" class="c">7</a><a title="��8ҳ" href="?page=8">8</a><a title="��9ҳ" href="?page=9">9</a><a title="��10ҳ" href="?page=10">10</a><a title="��11ҳ" href="?page=11">11</a><a title="��12ҳ" href="?page=12">12</a><a title="ĩҳ" href="?page=69">...69</a><a title="��һҳ" href="?page=6">&#8249;&#8249;</a><a title="��һҳ" href="?page=8">&#8250;&#8250;</a><span>20��<cite>/</cite>ҳ&nbsp;��<label id="total">1363</label>��</span></div>
      </div>
      <div class="right" style="text-align:left;padding:18px;line-height:2;text-decoration:none;word-wrap: break-word;">


    <center>
    <div style="width: 201px; height: 30px;background: url(images/bg_search_box.gif);">
    <form name=form1 method=get action="index.asp">
    <input name="key" size="15" style="float:left;margin: 4px 0 0 6px; border:0px; height:22px;width: 160px; background: none;outline:none;line-height:22px;">
    <input type="submit" style="width:27px;height:24px;border:0;background: none;float: right; margin: 3px 4px 0 0;" value="" title="����">
    </form>
    </div>
    <p style="letter-spacing: 4px">
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=ϲ>ϲ</a>
    <a href=index.asp?key=ŭ>ŭ</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a><br>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=ѩ>ѩ</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a><br>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a><br>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=ҹ>ҹ</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a><br>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=ɽ>ɽ</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a><br>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=ƶ>ƶ</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    <a href=index.asp?key=��>��</a>
    </p>
    </center>
    <hr style="margin-top:8px;height:1px;border:none;border-top:2px solid #ffffff;">

    <fieldset>
      <legend>��վ˵��</legend>
    ��һ������ṩ��д���ֵ���վ��<br>
    ��վ�����ڿ���ʱ��д�ú󷢲���<br>
    <center>
    <hr class=hr>
    <img src="images/rss.png" style="margin-bottom:-4px;"> <a href="rss.asp" target="_blank">RSS����</a>
    </center>
    </fieldset>

    <br>

    <a href="luck.asp"><div style="font-size:14px;color:#fff;background-color:#178BC8;border:#178BC8 solid 1px;padding:10px;">
    <center><img src=images/ding.png style="margin-bottom:-2px;"> ��㿴��</center>
      </div></a>

    <div style="font-size:14px;color:#fff;background-color:#178BC8;border:#178BC8 solid 1px;padding:10px;display:none;">
    <center>�� ��</center><hr style="height:1px;border:none;border-top:1px dashed #ffffff;">
    ��ʼ½�����£��ȸ����ٵ�<br><span style="padding-left:100px;">2015-14-04</span>
      </div>


    <fieldset>
      <legend>������վ</legend>
    <center>
    <img src=images/alipay.png width="180px">
    <hr class=hr>
    ��֧����Ǯ��ɨ������ / <a href="index.asp?id=1233">����</a>
    </center>
    </fieldset>

    <fieldset>
      <legend>���˵���</legend>
    <li><a href=index.asp?id=1084>��ֽ����</a> <a href="http://weibo.com/120050530" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=610>Ѱ����Ҷ��sara</a> <a href="http://weibo.com/919sara" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=650>�С����</a> <a href="http://weibo.com/u/2271701384" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=835>īȾ�����ƹ�</a> <a href="http://weibo.com/p/1005051910663347" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=844>���ֵ���СԲ</a> <a href="http://weibo.com/u/2624525623" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=884>��Ϧ�ı�</a> <a href="http://user.qzone.qq.com/532450167" target="_blank"><img src=images/qqkongjian.png title="��ta��QQ�ռ�"></a></li>
    <li><a href=index.asp?id=892>��ʱ��</a> <a href="http://weibo.com/u/3849499656" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=889>Mrؼ��</a> <a href="http://weibo.com/u/2110700181" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=894>����MissZhao</a> <a href="http://weibo.com/zhaoli90" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=923>Miss��-����õ�ʱ��</a> <a href="http://weibo.com/u/1765586750" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=1085>LVMEAL-����</a> <a href="http://weibo.com/u/2639511751" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=1129>��·ԶBrucelv</a> <a href="http://weibo.com/u/2954541897" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=1134>��Ľ�������ĺ�</a> <a href="http://weibo.com/u/1958894775" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    <li><a href=index.asp?id=1459>һ���</a> <a href="http://weibo.com/yitunjun" target="_blank"><img src=images/weibo.png title="��ta��΢��"></a></li>
    </fieldset>

    <fieldset>
      <legend><a href="http://shouxieke.net/b/b.asp?b=0&action=list&type=2" target="_blank">��̳����</a></legend>
    <script language=javascript src=http://shouxieke.net/other/Article/topic.asp?PithFlag=1&Number=8&StrLen=28&NewWindow=yes></script>
    </fieldset>

    <fieldset>
      <legend><a href="http://shouxieke.net/b/b.asp?b=3" target="_blank">��д�ĵ�</a></legend>
    <script language=javascript src=http://shouxieke.net/other/Article/topic.asp?GoodAssort=7&Number=8&StrLen=28&NewWindow=yes></script>
    </fieldset>

    <fieldset>
      <legend><a href="http://shouxieke.net/b/b.asp?b=5" target="_blank">���ʻ</a></legend>
    <script language=javascript src=http://shouxieke.net/other/Article/topic.asp?BoardID=5&Number=8&StrLen=28&NewWindow=yes></script>
    </fieldset>

      <fieldset>
      <legend>��������</legend>
      <li style="float:left;width:60px;"><a href="http://shouxieke.net/oldfile/bbs" target="_blank">�ɵĻ���</a></li>
      <li style="float:left;width:60px;"><a href="http://www.v2ex.com/?r=weiwei202" target="_blank">V2EX</a></li>
      <li style="float:left;width:60px;"><a href="http://zhihu.com" target="_blank">֪��</a></li>
      <li style="float:left;width:60px;"><a href="http://leadbbs.com" target="_blank">LeadBBS</a></li>
      <li style="float:left;width:60px;"><a href="http://shufazidian.com" target="_blank">�鷨�ֵ�</a></li>
      <li style="float:left;width:60px;"><a href="http://qiuziti.com" target="_blank">������</a></li>
      <li style="float:left;width:60px;"><a href="http://www.shouxiefang.com" target="_blank">��д��</a></li>
      <li style="float:left;width:60px;"><a href="http://www.shouxieti.com" target="_blank">��д����</a></li>
      <li style="float:left;width:60px;"><a href="https://shuge.org" target="_blank">���</a></li>
      <li style="float:left;width:60px;"><a href="http://www.luoo.net" target="_blank">����</a></li>
      <li style="float:left;width:60px;"><a href="https://pixabay.com" target="_blank">Pixabay</a></li>
      <li style="float:left;width:60px;"><a href="http://so.chongbuluo.com/" target="_blank">����</a></li>

      </fieldset>

      <fieldset>
      <legend>�ر���л</legend>

      <li style="float:left;width:60px;"><a href="http://www.fcontex.com/content/read-25.html" target="_blank">EasyIDE</a></li>
      <li style="float:left;width:60px;"><a href="http://jquery.com" target="_blank">Jquery</a></li>
      <li style="float:left;width:60px;"><a href="http://iconfont.cn" target="_blank">Iconfont</a></li>
      <li style="float:left;width:60px;"><a href="http://duoshuo.com" target="_blank">��˵</a></li>
      <li style="float:left;width:60px;"><a href="http://alipay.com" target="_blank">֧����</a></li>

      </fieldset>


      </div>
      <div style="float:left;" class="content"><hr class="hr">
    <div style="float:left;padding-bottom:20px;"><A href="index.asp?action=unfinished">����</A> | <a href="index.asp?id=422">����</a> | <a href="index.asp?id=883">����</a> | <a href="index.asp?id=1233">����</a>  | <a href="rss.asp" target="_blank">RSS</a><span style="display:none">
    <script src='http://w.cnzz.com/c.php?id=1256012485&l=3' language='JavaScript'></script>
    </span></div><div style="float:right;padding-bottom:20px;">Copyright <span style="font:1.0em Tahoma,Arial,sans-serif;">&copy;</span> 2013-2016 ������<br><span style="color:gray;display:none;">31.250 ms</span></div>
    </div>
    </div>
    </center>
    <div class="sidemenu">

    <script>
    function show_div(){
     var obj=document.getElementById('menu2');
    var btn=document.getElementById('show_menu2');
        if(obj.style.display=='none'){
            obj.style.display='block';
            btn.innerHTML='����';
        }else{
            obj.style.display='none';
            btn.innerHTML='�˵�';
        }
    }
    </script>
    <div id="menu2" style="display:block;">
    <!--<a href="add.asp"><div class="sidemenudiv">����</div></a>
    <a href="index.asp?id=1235"><div class="sidemenudiv">����</div></a>
    <a href="index.asp"><div class="sidemenudiv">��ҳ</div></a>-->

    <a href="?page=6"><div class="sidemenudiv">��ҳ</div></a>
    <a href="?page=8"><div class="sidemenudiv">��ҳ</div></a>

    </div>
    <!--<div id='show_menu2' class="sidemenudiv" onclick="show_div()">�˵�</div>-->
    </div>
     </BODY>
    </html>"""

    soup = BeautifulSoup(html)
    pagination = soup.find('div', attrs={'class': 'page_turner'})
    if pagination:
        pass
