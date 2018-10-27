#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: ftid.py
# version: 0.0.1
# description: ftid.py


import futuquant as ft


q = ft.OpenQuoteContext(host='sz.omg.tf', port=11111)

# 沪深A股
hs = q.get_plate_stock('SH.3000005')[1]

q.close()

hs['code'] = hs['code'].map(lambda x: x[3:])


# 富途牛牛Code
ftid = hs.set_index('code').drop(columns=['stock_owner','stock_name', 'lot_size', 'stock_child_type', 'stock_type', 'list_time']).T.to_dict('records')[0]

print('ftid %d' % len(ftld))

