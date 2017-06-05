#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 装饰器
def singleton(func):
    instances = {}

    def get_instance(*args, **kwargs):
        print (args, kwargs)
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]
    return get_instance


@singleton
class MyClass:
    a = 1

    def __init__(self, a):
        self.a = a

    def prt(self):
        print "dgsgsg"


if __name__ == '__main__':
    print "/**********************************/"
    cm = MyClass(2)
    print cm # 输出 2
    print cm.a

    print "/**********************************/"
    cn = MyClass(3)
    print cn
    print cn.a  # 2 这里输出的是2
