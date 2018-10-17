#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: futu.py
# version: 0.0.1
# description: futu.py

import futuquant as ft

q = ft.OpenQuoteContext(host='198.13.60.168', port=11111)

# 沪深A股
hs = q.get_plate_stock('SH.3000005')

# 富途牛牛Code
ftcode_dict = hs[1].set_index('code').drop(columns=['stock_owner','stock_name', 'lot_size', 'stock_child_type', 'stock_type', 'list_time']).T.to_dict('records')[0]

