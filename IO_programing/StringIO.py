#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-16 上午12:51
# @Author  : Zhang_xq
# @File    : StringIO.py
# @Software: PyCharm
from io import StringIO, BytesIO

f_0 = StringIO()
print(f_0.write('hello, world'))
print(f_0.write(', '))
print(f_0.write('this is the end of this StringIO'))
print(f_0.getvalue())

f_1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f_1.readline()
    if s == '':
        break
    print(s.strip())

f_2 = BytesIO()
f_2.write('中文'.encode('utf-8'))
print(f_2.getvalue())

f_3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f_3.read())