#!/usr/bin/python
#  -*- coding: UTF-8 -*-


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(1, 15, 1)
#
# plt.plot(x, x*2)
#
# plt.plot(x, x*3+3)
#
# plt.plot(x, x*4+4)
#
# plt.legend(['Normal', 'Fast', 'Faster'])
#
# plt.show()


# import numpy as np
# import pandas as pd
#
# # 导入图表库以进行图表绘制
# import matplotlib.pyplot as plt
#
# loandata = pd.DataFrame(pd.read_excel('E:\gittest\puv.xlsx'))
#
# # 设置日期字段issue_d为loandata数据表索引字段
# loandata = loandata.set_index('日期')
#
# # 按月对贷款金额loan_amnt求均值，以0填充空值
# loan_plot = loandata['pv']
#
# # 图表字体为华文细黑，字号为15
# plt.rc('font', size=15)
#
# # 创建一个一维数组赋值给a
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# # 创建折线图，数据源为按月贷款均值，标记点，标记线样式，线条宽度，标记点颜色和透明度
# plt.plot(loan_plot, 'h', loan_plot, 'g', color='#99CC01', linewidth=3, markeredgewidth=3, markeredgecolor='#99CC01',
#          alpha=0.8)
#
# # 添加x轴标签
# plt.xlabel('Month')
# # 添加y周标签
# plt.ylabel('Sumber')
# # 添加图表标题
# plt.title('xxxxxx')
# # 添加图表网格线，设置网格线颜色，线形，宽度和透明度
# plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
# # 设置数据分类名称
# # plt.xticks(a, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
# plt.xticks(a)
# # 输出图表
# plt.show()


# 做成html
# xlrd 对excel 进行读操作，xlwt 对exce进行写操作
import xlrd
from pyecharts import Bar, Line
import numpy as np

data = xlrd.open_workbook('E:\lrzsz\sz\jiaoshipai\\201810.xlsx')
table = data.sheets()[0]

print('xlrd模块的简单使用：')
print("工作簿里的所有工作表名字和对象：", data.sheet_names(), data.sheets())
print('第一个sheet表名 和对象：', data.sheet_names()[0], data.sheet_by_name('account_jiaoshipai'))
print('第2个sheet表名：', data.sheet_names()[1])
# 获取 表的总行数
print('第一sheet表行数：', table.nrows)
# 获取 表的总列数
print('第一sheet表列数：', table.ncols)
# 获取单元格的值
print('第一个 shett的 0行0列 的值:', table.cell(0, 0).value)
print('第一个 shett的 1行1列 的值:', table.cell(1, 1).value)
# 获取 表 的第一例的值
print("获取 表 的第一例的值:", table.col_values(1))


def get_sheet_number(sheet):
    return sheet.nrows+1


print('可以继续写入的行，即没有数据的行号：', get_sheet_number(table))
'''
比上面的复杂多了
获取工作表的名字list中的第一个
table_name = data.sheet_names()[0]
print(table_name)
# 根据表明获取 表对象 即 sheet对象
table_sheet = data.sheet_by_name(table_name)
print(table_sheet)
通过sheet 对象获取 表的行数
nrows = table_sheet.nrows
print(data.sheet_by_name(table_name).nrows)
'''

# # X轴
# CLOTHES = table.col_values(0)
# # 数据
# clothes_pv = table.col_values(1)
# clothes_uv = table.col_values(2)
# clothes_ip = table.col_values(3)
#
# (Line("www.ekeguan.com")
#     .add("PV", CLOTHES, clothes_pv, is_stack=False)
#     .add("UV", CLOTHES, clothes_uv, is_stack=False)
#     .add("IP", CLOTHES, clothes_ip, is_stack=False)
#     .render('E:\lrzsz\sz\\201809.html'))


# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib
# from pyecharts import Bar
# from matplotlib.ticker import FuncFormatter
#
# df = pd.read_excel("E:\gittest\puv.xlsx")
# # print(df)
# data = df
# # 中文支持
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.size'] = 10
#
# # print(plt.style.available)
# # print(data)
#
#
# def currency(x):
#     """The two args are the value and tick position"""
#     if x >= 100000:
#         return '{:1.1f}M'.format(x * 1e-6)
#     return '{:1.0f}K'.format(x * 1e-3)
#
#
# plt.style.use('ggplot')
# # data.plot(kind='line', y="pv", x="日期")
#
#
# fig, ax = plt.subplots()
# data.plot(kind='line', y="pv", x="date", ax=ax)
# data.plot(kind='line', y='uv', x="date", ax=ax)
# data.plot(kind='line', y='ip', x="date", ax=ax)
#
# # 修改x 和y 轴标题
# # # ax.set_xlim([-10000, 140000])
# # ax.set_xlabel('pv')
# # ax.set_ylabel('date')
#
# # 修改x 和y 轴标题 更便捷
# ax.set(title='www.ekeguan.com pv uv ip', xlabel='2018-09月', ylabel='值')
#
# # 计算想轴数字为k等[在kind=brah模式下]
# # formatter = FuncFormatter(currency)
# # ax.xaxis.set_major_formatter(formatter)
#
# # 删除图例说明
# # ax.legend().set_visible(False)
#
# plt.show()
# # Bar.add(plt.show())
# # Bar.render('E:\gittest\puv.html')
