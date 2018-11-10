#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : @jiawenlong
# date : 2018/11/1 0001


# coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
# driver = webdriver.Chrome()
driver_path = 'D:\Program Files\Python3.7\Scripts\chromedriver.exe'  # 这里放的就是下载的driver本地路径
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("https://www.baidu.com/")

text = driver.find_element_by_css_selector('#kw')
search = driver.find_element_by_css_selector('#su')
text.send_keys('headless chrome')
# search
search.click()
time.sleep(1)
driver.get_screenshot_as_file("One.png")  # 截取当前页面的图片（全屏）。括号里面的路径为保存到本地电脑上面的路径，可随意设置。
driver.quit()

# for image in driver.find_elements_by_tag_name("img"):  # 获取当前页面的图片信息
#     print(image.text)
#     print(image.size)
#     print(image.tag_name)
#     print("=="*20)
#     time.sleep(2)
#
# for link in driver.find_elements_by_xpath("//*[@href]"):  # 获取当前页面的href
#     print(link.get_attribute('href'))
#     print("=="*20)
#
# for id in driver.find_elements_by_xpath("//*[@id]"):  # 获取当前页面的id
#
#     print(id.get_attribute('id'))
#     print("=="*20)

# driver.get_screenshot_as_file("One.png")  # 截取当前页面的图片（全屏）。括号里面的路径为保存到本地电脑上面的路径，可随意设置。
#
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time
#
#
# # 启动driver
# def init_web_driver():
#     global driver
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     driver_path = 'D:\Program Files\Python3.7\Scripts\chromedriver.exe'  # 这里放的就是下载的driver本地路径
#     driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
#     driver.maximize_window()
#
#
# # 关掉driver
# def close_web_driver():
#     driver.quit()
#
#
# def get_data():
#     driver.get('https://www.baidu.com')
#     driver.implicitly_wait(10)  # wait up to 10 seconds for the elements to become available
#     # ======  网页中静态部分抓取，采用BeautifulSoup去解析
#     html = driver.page_source  # 获取网页html
#     # print(type(html))
#     # html_soup = BeautifulSoup(html.text, "lxml")
#     html_soup = BeautifulSoup(html, "html.parser")
#     # print(html_soup)
#     # coin_list = html_soup.find(name='table', attrs={"class": "table maintable"})
#     coin_list = html_soup.find_all('a', 'mnav')
#     print(coin_list)
#     # 页面元素的提取请查看 BeautifulSoup的用法
#     # ====== 网页中动态部分抓取，采用driver自带的方法
#     # 下面展示的从调用百度搜索，在搜索框中输入"headless chrome"，然后获取结果。具体自行百度driver的用法
#     text = driver.find_element_by_css_selector('#kw')
#     search = driver.find_element_by_css_selector('#su')
#     # text.send_keys('headless chrome')
#     text.send_keys('headless chrome')
#     # search
#     search.click()
#
#     time.sleep(3)
#     driver.get_screenshot_as_file('search-result.png')
#     results = driver.find_elements_by_xpath('//div[@class="result c-container "]')
#     for result in results:
#         res = result.find_element_by_css_selector('a')
#         title = res.text
#         link = res.get_attribute('href')
#         print('Title: %s \nLink: %s\n' % (title, link))
#
#
# if __name__ == '__main__':
#     init_web_driver()
#     get_data()
#     close_web_driver()
