#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mysingleton import my_singleton

if __name__ == '__main__':

    # 使用import是天然的单例模式
    print my_singleton # 输出 23
    print my_singleton.da
    my_singleton.foo()

# 使用 动态加载类的方法也可以对其初始化，
# 但是这样类似于java中的反射，java中的反射会破坏代码结构，
# Python 应该也是的吧，不过好像在Python里面运用反射机制的地方挺多的  0.0