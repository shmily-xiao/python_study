#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
    def __init__(self):
        self.__a = "asdas" # 这个类似于java的private 去修饰的变量
        self._b = "dssg"
        self.c = "oihjoihjo"


if __name__ == '__main__':
    tt = MyClass()
    # 报错
    # 具有真正意义的私有变量，实例无法访问
    # print tt.__a

    # 这个有些奇怪，在你使用 . 去看这个实例有哪些属性的时候查看不到，但是在使用的时候却可以使用
    # 是约定类型的私有变量，你用还是可以的，不拦着你
    print tt._b

    # 默认是一个公开的变量，默认public
    print tt.c
