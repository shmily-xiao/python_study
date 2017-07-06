#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  动态的向类中添加属性
"""

import time
def now(s):
    print time.time()

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

class A(object):

    a = 1
    b = 2
    def __init__(self, arg):
        for i,j in arg.items():
            setattr(self, i,j)

    @log
    def validate(self):
        print self.r
        return self.r


if __name__ == '__main__':
    # a = A()
    # print A.__dict__
    # setattr(a, 'c', 3)
    # print a.c
    # print a.__dict__
    # b = A()
    # print b.c

    a = {'c':3,'r':'eee'}
    aa = A(a)
    # print aa.__dict__
    # print aa.r
    # print aa.c
    # print aa.a
    dd = aa.validate()
    print dd


