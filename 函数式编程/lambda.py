#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 1:23
# @Author  : Zhang_xq
# @File    : lambda.py
# @Software: PyCharm

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
a = list(range(1, 5))
print(a)
a = list(map(lambda x: x + 1, a))
print(a)

f = lambda x: x * x  # do not assign a lambda expression, use a def
print(f)
print(f(23))


def build(x, y):
    """test"""
    return lambda: x * 10 + y


a = build(2, 3)
print(a())


# 练习
# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
L_myself = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L_myself)

if print(L_myself) == print(L):
    print('测试成功')
else:
    print('fuck off')

a = 4*6