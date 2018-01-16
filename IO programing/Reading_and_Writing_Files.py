#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-16 上午12:32
# @Author  : Zhang_xq
# @File    : Reading_and_Writing_Files.py
# @Software: PyCharm

with open('/home/zhangxq/Documents/Python/py_study/test.png', 'rb') as test_1:
    print(test_1.read())
print('\\\\\\\\\\\\\\\\\\\\\\\\')
with open('/home/zhangxq/Documents/Python/py_study/test.txt', 'r', encoding='ascii', errors='ignore') as test_2:
    print(test_2.read())
print('\\\\\\\\\\\\\\\\\\\\\\\\')
with open('/home/zhangxq/Documents/Python/py_study/test.txt', 'r', encoding='gbk', errors='ignore') as test_3:
    print(test_3.read())
with open('/home/zhangxq/Documents/Python/py_study/test_write', 'a', encoding='utf- 8') as test_4:
    test_4.write('\nfuck you')
with open('/home/zhangxq/Documents/Python/py_study/test.txt', 'a') as test_5:
    test_5.write('\nfuck off')
