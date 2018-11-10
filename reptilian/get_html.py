#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : @jiawenlong
# date : 2018/11/1 0001

# 在 urllib 库里 查找 request 模块，导入 urlopen 方法【函数】
from urllib.request import urlopen
# 导入 BeautifualSoup
from bs4 import BeautifulSoup

# 打开 url 获取 html 内容
# html = urlopen('http://jr.jd.com')
html = urlopen('http://www.ekeguan.com')
print(html.read())
# 把 html 内容 传给 BeautifulSoup 对象
bs_obj = BeautifulSoup(html.read(), 'html.parser')
# print(bs_obj)
# 找到 所有 class = 'nav-item-primary' 的 a 标签
# text_list = bs_obj.find_all("a", 'nav-item-primary')
text_list = bs_obj.find_all("a", 'com-nav-zx-n')
# print(text_list)

for text in text_list:
    # 打印导航栏文本
    print(text.get_text())

html.close()