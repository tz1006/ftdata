
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
                        
def closing_average(ftcode, day):
    kline = q.get_history_kline(ftcode)[1]
    average = kline[-day:]['close'].mean()
    return average

                        
def name_listing_suspension(ftcode):
    data = get_stock_basicinfo(ftcode)
    name = data['name'].to_string(index=False)
    listing_date = data['listing_date'].to_string(index=False)
    suspension = data['suspension']
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
