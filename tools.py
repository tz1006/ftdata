#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: tools.py
# version: 0.0.1
# description: tools.py


import requests
from datetime import datetime
from pytz import timezone
import json



########--Tools--########

def ftcode(code):
    if code[0]+code[1] =='60':
        code = 'SH.' + code
    else:
        code = 'SZ.' + code
    return code


def sscode(code):
    if code[0]+code[1] =='60':
        code = 'sh%s' % code
    else:
        code = 'sz%s' % code
    return code


def stock_name(code):
    url = 'http://hq.sinajs.cn/list=%s' % sscode(code)
    r = None
    while r == None:
        r = s.get(url, timeout=timeout)
    name = r.text.split("\"")[1].split(",",1)[0]
    return name



