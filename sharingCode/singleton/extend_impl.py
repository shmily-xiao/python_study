#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        print (args, kwargs)
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls).__new__(cls, *args, **kwargs)
            orig.__dict__ = cls._state
            cls._instance = orig
        return cls._instance


class MyClass(Singleton):
    a = 1

    def __init__(self, a):
        self.a = a

if __name__ == '__main__':
    print '/************************************/'
    cm = MyClass(2)
    print cm # 输出 2
    print cm.a

    print '/************************************/'
    cn = MyClass(3)
    print cn
    print cn.a  # 3 这里输出的是3
