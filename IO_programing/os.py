#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-16 下午10:31
# @Author  : Zhang_xq
# @File    : os.py
# @Software: PyCharm
import os
import shutil

print(os.path.abspath('.'))
print(os.path.join('/home/zhangxq/Documents/Python/py_study/IO_programing', 'fuck'))
os.mkdir('/home/zhangxq/Documents/Python/py_study/IO_programing/fuck')
# 不能已存在的目录使用mkdir
os.rmdir('/home/zhangxq/Documents/Python/py_study/IO_programing/fuck')
print(os.path.split('/home/zhangxq/Documents/Python/py_study/IO_programing/fuck'))
print(os.path.splitext('/home/zhangxq/Documents/Python/py_study/IO_programing/StringIO.py'))
# os.rename('fuck.txt', 'test.py')
# os.remove('fuck.txt')
# shutil.copyfile()
# print([x for x in os.listdir('.') if os.path.isdir(x)])
a = [x for x in os.listdir('.') if os .path.isfile(x)]
print(a)