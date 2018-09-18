#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一张html上多个图表
from __future__ import unicode_literals
import xlrd
from pyecharts import Bar, Grid
from pyecharts import Page

# 创建一个页面
page = Page()

# excel
data = xlrd.open_workbook('E:\lrzsz\sz\\201809.xlsx')
table = data.sheets()[0]
bank = data.sheets()[1]

print(table.col_values(0))
print(bank.col_values(0))

# X轴
CLOTHES = table.col_values(0)
# 数据
clothes_pv = table.col_values(1)
clothes_uv = table.col_values(2)
clothes_ip = table.col_values(3)
# print(clothes_pv, clothes_uv, clothes_ip)

# bar = Bar("account_ekeguan_com", height=720)
bar = Bar("account_ekeguan_com", height=350)
bar.add("PV", CLOTHES, clothes_pv)
bar.add("UV", CLOTHES, clothes_uv)
bar.add("IP", CLOTHES, clothes_ip, is_stack=False, is_datazoom_show=True)

# X轴
CLOTHES = bank.col_values(0)
# 数据
clothes_pv = bank.col_values(1)
clothes_uv = bank.col_values(2)
clothes_ip = bank.col_values(3)
# print(clothes_pv, clothes_uv, clothes_ip)

line = Bar("www_ekeguan_com", title_top='1%')
line.add("PV", CLOTHES, clothes_pv)
line.add("UV", CLOTHES, clothes_uv)
line.add("IP", CLOTHES, clothes_ip, is_stack=False, is_datazoom_show=True)

page.add(bar)
page.add(line)
page.render('E:\lrzsz\sz\\201809.html')

# grid = Grid()
# grid.add(bar, grid_bottom="60%")
# grid.add(line, grid_top='60%')
# grid.render('E:\lrzsz\sz\\201809.html')
