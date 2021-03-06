#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : @jiawenlong
# date : 2018/11/1 0001

from selenium import webdriver
import csv

# 网易云音乐歌单第一页url
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

# 用 PhantomJs几口创建一个Selenium 的 webdriver
# driver = webdriver.PhantomJS()

# 最新的selenium不支持phantomjs
# 需要用Chrome或者Firefox替代
# 下载chromedriver代替phantomjs
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)

# 准备好存储歌单的文件 csv
csv_file = open('E:\lrzsz\sz\play_list.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])


# 解析第一页，直到 下一页 为空
while url != 'javascript:void(0)':
    # 用 webdriver 加载页面
    driver.get(url)
    driver.switch_to.frame('contentFrame')
    data = driver.find_element_by_id('m-pl-container').find_element_by_tag_name('li')
    for i in range(len(data)):
        nb = data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0]) > 500:
            msk = data[i].find_element_by_css_selector('a.msk')
            writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
    url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')

csv_file.close()
driver.quit()