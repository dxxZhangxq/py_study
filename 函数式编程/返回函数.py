#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 1:08
# @Author  : Zhang_xq
# @File    : 返回函数.py
# @Software: PyCharm


def calc_sum(*args):
    """求和"""
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_calc_sum(*args):
    """返回求和函数"""

    def _sum():
        ax = 0
        for n in args:
            ax = n + ax
        return ax

    return _sum


print(lazy_calc_sum(1, 3, 5, 6, 7))
a = lazy_calc_sum(1, 3, 5, 6, 7)
print(a())
print(a)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1)
print(f1())


def count_():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, h2, h3 = count_()
print(f1())
print(h2())
print(h3())


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def create_counter():
    """每次调用它返回递增整数"""
    x = 0

    def counter():
        """1"""
        nonlocal x
        x += 1
        return x

    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
