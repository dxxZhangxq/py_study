#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-16 上午12:59
# @Author  : Zhang_xq
# @File    : os_test.py
# @Software: PyCharm
import os


# 练习
# 1.利用os模块编写一个能实现dir -l输出的程序。
#
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def search(path, filename):
    """search file"""
    for dir_s in os.listdir(path):
        file_path = os.path.join(path, dir_s)
        if os.path.isdir(file_path):
            search(file_path, filename)
        elif os.path.isfile(file_path) and filename in dir_s:
            print('搜索到含“ %s ”的文件，路径为 %s' % (filename, file_path))


# 别人想的
#  def search_file(dir_path, name):
#     """search file that include the 'name' in file name"""
#     for p in os.listdir(dir_path):
#         fp = os.path.join(dir_path, p)
#         if os.path.isdir(fp):
#             search_file(fp, name)
#         elif os.path.isfile(fp) and name in p:
#             print('匹配到文件 %s' % fp)


print(search('/home/zhangxq/Documents/Python/', '.py'))
