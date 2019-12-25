```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Dec  2 19:09:30 2018

@author: yh6788
"""
import requests
import sys
import re
from bs4 import BeautifulSoup


# 获取外网IP

def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip地址   :   ' + ip)
    return ip


def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt, "lxml").iframe
    return soup["src"]
    print('ip1:' + ip)


def dizhi():
    #                kw = ip
    url1 = "http://ip138.com/ips138.asp"
    kw2 = {'ip': kw}
    r = requests.request('GET', url1, params=kw2)
    r.encoding = 'gbk'
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    soup = soup.ul
    # print(r.request.url)
    print("查询接口1:  ", soup.contents[0].string[5:])
    # print("查询接口2：\n",soup.contents[1].string[6:])
    # print("查询接口3：\n",soup.contents[2].string[6:])


def jiange():
    print("==" * 20)


if __name__ == '__main__':
    jiange()
    kw = get_out_ip(get_real_url())
    #                get_out_ip(get_real_url())
    dizhi()
    jiange()
```

