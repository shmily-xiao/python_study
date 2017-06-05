#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mysingleton import my_singleton


class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        print (args, kwargs)
        print "cls: %s" % cls
        print dir(cls)
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls).__new__(cls, *args, **kwargs)
            orig.__dict__ = cls._state
            cls._instance = orig
        return cls._instance


class MyClass(Singleton):
    a = 1

    def __init__(self, a):
        self.a = a

# def singleton(func):
#     instances = {}
#     def getinstance(*args, **kwargs):
#         print (args, kwargs)
#         for key in instances:
#             print "key: %s" % key
#             print "value: %s" %instances[key]
#         if func not in instances:
#             instances[func] = func(*args, **kwargs)
#         return instances[func]
#     return getinstance
#
# @singleton
# class MyClass:
#     a = 1
#
#     def __init__(self, a):
#         self.a = a
#
#     def prt(self):
#         print "dgsgsg"

if __name__ == '__main__':
    cm = MyClass(2)
    print cm # 输出 2
    print cm.a

    cn = MyClass(3)
    print cn
    print cn.a  # 3 这里输出的是3




