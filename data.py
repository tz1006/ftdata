#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: futu.py
# version: 0.0.1
# description: futu.py

import pandas as pd
import futuquant as ft

from tools import *


q = ft.OpenQuoteContext(host='sz.omg.tf', port=11111)

# 沪深A股
hs = q.get_plate_stock('SH.3000005')[1]

hs['code'] = hs[1]['code'].map(lambda x: x[3:])

# 富途牛牛Code
ftcode_dict = hs.set_index('code').drop(columns=['stock_owner','stock_name', 'lot_size', 'stock_child_type', 'stock_type', 'list_time']).T.to_dict('records')[0]

# DataFrame
df = pd.DataFrame(columns=['code','last_4_average','last_9_average'])



def init_df():
    for i in ftcode_dict:
        df_insert_ma(i)

def update_df():
    
    
def df_insert_ma(ftcode):
    try:
        # 去除停牌
        suspension = False
        if suspension == False:
            code = ccode(ftcode)
            last_4_average = q.request_history_kline(ftcode, start='2017-06-20', end='2019-06-22', max_count=4)[1]['close'].mean()
            last_9_average = q.request_history_kline(ftcode, start='2017-06-20', end='2019-06-22', max_count=9)[1]['close'].mean()
            df.loc[len(df)] = [code, last_4_average, last_9_average]
            print('添加(%s, %s, %s)' % (code, last_4_average,last_9_average))
    except:
        print(ftcode)
