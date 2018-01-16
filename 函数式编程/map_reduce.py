#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 15:44
# @Author  : Zhang_xq
# @File    : map_reduce.py
# @Software: PyCharm

from functools import reduce


def power(x):
    """test"""
    return x * x


r = map(power, [1, 2, 3, 4, 5, 6, 7])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))


def add(x, y):
    """test"""
    return x + y


print(reduce(add, [1, 3, 5, 6, 7, 8, 4]))


# def fn(x, y):
#     """test"""
#     return x * 10 + y


# print(reduce(fn, [1, 2, 3, 5, 6, 7, 3]))

# digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    """str to int"""
    if not isinstance(s, str):
        raise TypeError

    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        """return"""
        return x * 10 + y

    def str2int_s(s):
        """return"""
        s1 = s[:]
        return digits[s1]

    return reduce(fn, map(str2int_s, s))


print(list(map(str2int, ['2333', '23423'])))


def char2num(s):
    """dic返回int"""
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2int_v2(s):
    """str to int"""
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(list(map(str2int, ['2333', '23423'])))


# 练习_0
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


def normalize(name):
    """

    将不规范的英文名字，变为首字母大写，其他小写的规范名字

    输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
    这个没想出来
    """

    # def step_1(n):
    #     if not isinstance(n, str):
    #         raise TypeError
    #     else:
    #         return n.title()
    # return list(map(step_1, name))

    # def step_1(name):
    #     return list(map(name.lower(), name))
    #
    # def step_2(name):
    #     return map(name.upper(), name)
    #
    # return (step_1(name))
    return name[0].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

names = ['adam', 'LISA', 'barT']


# print(list(map(lambda name: name[0].upper() + name[1:].lower(), ['adam', 'LISA', 'barT'])))

# 练习_1
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：


def prod(l):
    """接受一个list求积"""

    def power(x, y):
        """return x*y"""
        return x * y

    return reduce(power, l)


# 测试:
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习_2
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：


def str2float(s):
    """将字符串转化为浮点数"""
    s_0 = s.split('.')  # 将字符串由'.'切片为两部分
    s_1 = s_0[1]
    s_0[1] = s_1[::-1]  # 小数部分字符串颠倒
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fint(s):
        """字符串转整数？"""
        return digits[s]

    def f_0(x, y):
        """整数部分"""
        return x * 10 + y

    def f_1(x, y):
        """小数部分"""
        return x * 0.1 + y

    # t = reduce(f_1, map(fint, s_0[1]))
    # return reduce(f_0, map(fint, s_0[0])) + t * 0.1
    return reduce(f_0, map(fint, s_0[0])) + reduce(f_1, map(fint, s_0[1])) * 0.1


# 测试：
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
