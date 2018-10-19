
#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: ftapi.py
# version: 0.0.1
# description: ftapi.py


import requests
import time

from ftid import ftid


# 参数



s = requests.session()
s.keep_alive = False


def get_data():
    url = 'http://hq.sinajs.cn/list=%s' % sscode(code)
    r = None
    while r == None:
        r = s.get(url, timeout=timeout)
