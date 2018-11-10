#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : @jiawenlong
# date : 2018/11/2 0002


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get('http://www.python.org')
# assert 'Python' in browser.title
#
# elem = browser.find_element_by_name('q')
# elem.send_keys('pycon')
# elem.send_keys(Keys.RETURN)
#
# print(browser.page_source)
#
#
# # time.sleep(2)
# # browser.quit()

# 测试用例
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn('Python', driver.title)

        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert "No resault Found" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
    print(os.name)