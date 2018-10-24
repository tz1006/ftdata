
#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: ftapi.py
# version: 0.0.1
# description: ftapi.py


import requests
import time

from ftid import ftid


import futuquant as ft

q = ft.OpenQuoteContext(host='sz.omg.tf', port=11111)

# 一次API

def get_history_kline(ftcode):
    data = q.get_history_kline(ftcode, start='2018-01-20', end='2019-06-22')[1]
    return data

def get_stock_basicinfo(ftcode):
    market = ftcode[:2]
    data = q.get_stock_basicinfo(market, 'STOCK', ftcode)[1]
    return data



# 二次API                       
                        
def closing_average(ftcode):
    kline = q.get_history_kline(ftcode)[1]
    try:
        average_4 = kline[-4:]['close'].mean()
    except:
        average_4 = None
    try:
        average_9 = kline[-9:]['close'].mean()
    except:
        average_9 = None
    try:
        average_19 = kline[-19:]['close'].mean()
    except:
        average_19 = None
    try:
        average_29 = kline[-29:]['close'].mean()
    except:
        average_29 = None
    try:
        average_59 = kline[-59:]['close'].mean()
    except:
        average_59 = None
    average = [average_4, average_9, average_19, average_29, average_59]
    return average

                        
def name_listing_suspension(ftcode):
    data = get_stock_basicinfo(ftcode)
    name = data['name'].to_string(index=False)
    listing_date = data['listing_date'].to_string(index=False)
    suspension = data['suspension'].to_string(index=False)
    if suspension == 'N/A':
        suspension = False
    else:
        suspension = True
    #stock_id = data['stock_id']
    #delisting = data['delisting']
    info = [name, listing_date, suspension]
    return info


# 参数



s = requests.session()
s.keep_alive = False


def get_data():
    url = 'http://hq.sinajs.cn/list=%s' % sscode(code)
    r = None
    while r == None:
        r = s.get(url, timeout=timeout)
