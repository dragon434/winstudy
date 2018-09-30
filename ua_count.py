#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : @jiawenlong
# 2018/9/29 0029

import re
import os, sys

# ua_file = "E:\lrzsz\sz\\ua"
#
# f = open(ua_file, 'r')
# line = f.readlines()
# f.close()
#
# for i in line:
#     print(i.strip('\n'))

ua = 'Mozilla/5.0 (Linux; Android 7.1.2; M6 Note Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 \
Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044303 Mobile Safari/537.36 V1_AND_SQ_7.7.8_908_YYB_D QQ/7.7.8.3705 \
NetType/4G WebP/0.3.0 Pixel/1080'
# Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)
#

agent = {'Os': ['Windows', 'Android', 'iOS', 'Macintosh'], 'At': ['PC', 'Tablet', 'Mobile'],
         'Browser': ['Safari', 'Chrome', 'Edge', 'IE', 'Firefox', 'Firefox Focus', 'Chromium', 'Opera', 'Vivaldi',
                     'Yandex', 'Arora', 'Lunascape', 'QupZilla', 'Coc Coc', 'Kindle', 'Iceweasel', 'Konqueror',
                     'Iceape', 'SeaMonkey', 'Epiphany', '360', '360SE', '360EE', 'UC', 'QQBrowser', 'QQ', 'Baidu',
                     'Maxthon', 'Sogou', 'LBBROWSER', '2345Explorer', 'TheWorld', 'XiaoMi', 'Quark', 'Qiyu', 'Wechat',
                     'Taobao', 'Alipay', 'Weibo', 'Douban', 'Suning', 'iQiYi'],
         'Windows': {
             '10.0': '10',
             '6.3': '8.1',
             '6.2': '8',
             '6.1': '7',
             '6.0': 'Vista',
             '5.2': 'XP',
             '5.1': 'XP',
             '5.0': '2000'
         }
         }
# ua = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
ua_at = ua.replace('(', '').replace(')', '').split(' ')
print(ua_at)
for at in ua_at:
    if at in agent['Os']:
        print(at)
        if at != 'Windows':
            print(ua_at[3])
    if at in agent['Windows']:
        print(agent['Windows'][at])
    if '/' in at:
        bro, version = at.split('/')
        if bro in agent['Browser']:
            print(bro)
        # print(bro, version)


end_agent = {
    'agent_type': 1,
    'agent_name': 2,
    'agent_version': 3,
    'os_type': 4,
    'os_name': 5,
    'os_versionName': 6,
    'os_versionNumber': 7,
    'linux_distibution': 8
}
