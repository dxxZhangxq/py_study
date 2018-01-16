#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 1:51
# @Author  : Zhang_xq
# @File    : generator.py
# @Software: PyCharm

g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

for nu in (x * x for x in range(11)):
    print(nu)


def fib(max_number):
    """斐波拉契数列"""
    n, a, b = 0, 0, 1
    while n < max_number:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for numbers in fib(6):
    print(numbers)

g = fib(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as wrong:
        print(wrong.value)
        break


def triangles():
    """输出杨辉三角"""
    start = [1]
    while True:
        temp = start[:]
        yield start[:]
        for i in range(len(start)):
            if i != 0:
                start[i] = temp[i] + temp[i - 1]
        start.append(1)


# def triangles():
#     num = [1]
#     while True:
#         temp = num[:]
#         yield temp
#         for i in range(len(num)):
#             if i != 0:
#                 num[i] = temp[i] + temp[i-1]
#         num.append(1)


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
