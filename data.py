#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: futu.py
# version: 0.0.1
# description: futu.py

from tqdm import tqdm
import pandas as pd
import futuquant as ft

from tools import *


q = ft.OpenQuoteContext(host='sz.omg.tf', port=11111)

# 沪深A股
hs = q.get_plate_stock('SH.3000005')[1]

#hs['code'] = hs[1]['code'].map(lambda x: x[3:])

# 富途牛牛Code
ftcode_dict = hs.set_index('code').drop(columns=['stock_owner','stock_name', 'lot_size', 'stock_child_type', 'stock_type', 'list_time']).T.to_dict('records')[0]

# DataFrame
df = pd.DataFrame(columns=['code', 'name', 'last_4_average','last_9_average'])



def init_df():
    print('初始化df...')
    # 除去当日停牌以及刚上市股票(数据)
    # 插入MA初始值(数据)
    for i in tqdm(ftcode_dict):
        df_insert_ma(i)
    # 去除MA不符合条件(计算)


#def update_df():

def df_insert_ma(ftcode):
    # print(ftcode)
    nls = name_listing_suspension(ftcode)
    name = nls[0]
    listing = nls[1]
    suspension = nls[2]
    # 去除停牌
    if suspension == False:
        average_data = closing_average(ftcode)
        last_4_average = average_data[0]
        last_9_average = average_data[1]
        last_19_average = average_data[2]
        if last_9_average/1.03 < last_4_average < last_9_average < last_19_average:
            df.loc[len(df)] = [ftcode, name, last_4_average, last_9_average]
        #print('添加(%s, %s, %s)' % (code, last_4_average,last_9_average))


