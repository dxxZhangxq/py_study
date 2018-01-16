#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-16 上午12:59
# @Author  : Zhang_xq
# @File    : OS.py
# @Software: PyCharm
import os


# a = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(a)
def search_file(dir_path, name):
    for p in os.listdir(dir_path):
        fp = os.path.join(dir_path, p)
        if os.path.isdir(fp):
            search_file(fp, name)
        elif os.path.isfile(fp) and name in p:
            print('匹配到文件 %s' % fp)
search_file('/home/zhangxq/Documents/Python/', name='OO')