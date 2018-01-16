#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-12 下午11:31
# @Author  : Zhang_xq
# @File    : 继承和多态.py
# @Software: PyCharm


class Animal(object):
    """animal"""

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is eating...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
cat = Cat()
dog.run()
cat.run()

a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly......................')


run_twice(Tortoise())


class Timer(object):
    """this is a duck"""

    def run(self):
        print('tik tok')


run_twice(Timer())
