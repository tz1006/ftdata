#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: futu.py
# version: 0.0.1
# description: futu.py

import pandas as pd
import futuquant as ft

from tools import *


q = ft.OpenQuoteContext(host='198.13.60.168', port=11111)

# 沪深A股
hs = q.get_plate_stock('SH.3000005')

# 富途牛牛Code
ftcode_dict = hs[1].set_index('code').drop(columns=['stock_owner','stock_name', 'lot_size', 'stock_child_type', 'stock_type', 'list_time']).T.to_dict('records')[0]

# DataFrame
df = pd.DataFrame(columns=['code','last_4_average','price', 'ratio'])


def init_df():
    for i in ftcode_dict:
        # 去除停牌
        if suspend(i) == False:
            code = 
            last_4_average = 
            price = 
            ratio = 
            df.loc[len(df)] = [code, last_4_average, price, ratio]
            print('添加(%s, %s, %s, %s)' % (code, last_4_average, price, ratio))
        else:
            pass
    message = ''

def update_df():
    
