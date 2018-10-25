
#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: ftapi.py
# version: 0.0.1
# description: ftapi.py


import requests
import time

from ftid import ftid


import futuquant as ft



# 准备
q = ft.OpenQuoteContext(host='sz.omg.tf', port=11111)

lines = [q,b,c,d]

ftcode_dict = q.get_plate_stock('SH.3000005')[1].set_index('code').drop(columns=['stock_owner','stock_name', 'lot_size', 'stock_child_type', 'stock_type', 'list_time']).T.to_dict('records')[0]
stock_gourps = group(list(ftcode_dict),100)
groups_dict = { i : 9 for i in lines}
groups_dict.fromkeys(stock_gourps, 1)
def subscribe_all():
    groups = list(stock_gourps)
    for line in lines:
        line.subscribe(groups[0], [SubType.QUOTE])
        groups_dict



# 一次API

def get_history_kline(ftcode):
    data = q.get_history_kline(ftcode, start='2018-01-20', end='2019-06-22')[1]
    return data

def get_stock_basicinfo(ftcode):
    market = ftcode[:2]
    data = q.get_stock_basicinfo(market, 'STOCK', ftcode)[1]
    return data


def quote_basic(ftcode):
    # generate URL
    security_id = ftcode_dict[ftcode]
    timestamp = int(time.time() * 1000)
    url = 'https://www.futunn.com/trade/quote-basic-v3?security_id=%s&_=%s' % (security_id, timestamp)
    #print(url)
    # web
    s = requests.session()
    s.headers['Connection'] = 'close'
    s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    r = None
    while r == None:
        r = s.get(url)
    # data
    data = r.json()['data']
    try:
        price = data['one_queue']['ask_price']
    except:
        price = None
    change = float(data['quote']['change'])
    ratio = float(data['quote']['change_ratio'][:-1])
    buysell = float(data['quote']['buysell_ratio'][:-1])
    # info
    info = {'price': price,
            'change': change, 
            'ratio': ratio,
            'buysell': buysell }
    return info

def get_stock_quote(ftcode):
    ctx = 
    data = ctx.get_stock_quote(all_stocks2)
    price = 

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
