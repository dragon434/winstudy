#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 做成html
# import xlrd
# from pyecharts import Bar, Line
#
# # excel
# data = xlrd.open_workbook('E:\gittest\puv.xlsx')
# table = data.sheets()[0]
#
# # X轴
# CLOTHES = table.col_values(0)
# # 数据
# clothes_pv = table.col_values(1)
# clothes_uv = table.col_values(2)
# clothes_ip = table.col_values(3)
#
# # bar = Line("www.ekeguan.com的pv、uv、ip", extra_html_text_label=["日期", "color:red"])
# bar = Line("www.ekeguan.com的pv、uv、ip")
# bar.add("PV", CLOTHES, clothes_pv, is_stack=False)
# bar.add("UV", CLOTHES, clothes_uv, is_stack=False)
# bar.add("IP", CLOTHES, clothes_ip, is_stack=False)
# bar.render('E:\gittest\puv.html')

# 官方实例
# 多次显示图表
# from pyecharts import Bar, Line
# from pyecharts.engine import create_default_environment
#
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
#
# line = Line("我的第一个图表", "这里是副标题")
# line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
#
# env = create_default_environment("html")
# # 为渲染创建一个默认配置环境
# # create_default_environment(filet_ype)
# # file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'
#
# env.render_chart_to_file(bar, path='E:\gittest\\bar.html')
# env.render_chart_to_file(line, path='E:\gittest\line.html')


# 一张html上多个图表
import xlrd
from pyecharts import Bar, Line, Grid

# excel
# data = xlrd.open_workbook('E:\gittest\\puv.xlsx')
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
print(clothes_pv, clothes_uv, clothes_ip)

bar = Bar("account_ekeguan_com", height=720)
bar.add("PV", CLOTHES, clothes_pv, is_stack=False)
bar.add("UV", CLOTHES, clothes_uv, is_stack=False)
bar.add("IP", CLOTHES, clothes_ip, is_stack=False)

# X轴
CLOTHES = bank.col_values(0)
# 数据
clothes_pv = bank.col_values(1)
clothes_uv = bank.col_values(2)
clothes_ip = bank.col_values(3)
print(clothes_pv, clothes_uv, clothes_ip)


line = Bar("www_ekeguan_com", title_top='50%')
line.add("PV", CLOTHES, clothes_pv, is_stack=False)
line.add("UV", CLOTHES, clothes_uv, is_stack=False)
line.add("IP", CLOTHES, clothes_ip, is_stack=False)

# bar.render('E:\gittest\puv.html')
grid = Grid()
grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")
grid.render('E:\lrzsz\sz\\201809.html')
# grid.render('E:\gittest\puv.html')
