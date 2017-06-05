#!/usr/bin/env python
# -*- coding:utf-8 -*-


# A 是装饰装饰器的函数
def A (d_t_enhance):
    def B (*args, **kwargs):
        def C (func):
            return d_t_enhance(func, *args, **kwargs)
        return C
    return B


# D 是装饰器的函数
@A
def D (func, *args, **kwargs):
    def E (arg1, arg2):
        # 可以做一些额外的参数处理
        print '/************ start **************/'
        print "I am in E and arg1, arg2 : {0}, {1}".format(arg1, arg2)
        print "I can change the parameter"
        arg1 = arg1 + 100
        print '/************ end **************/'
        return func(arg1, arg2)
    return E


# F 是被装饰的函数
@D('a','b','c')
def F (arg1, arg2):
    print " "
    print "I am in F and arg1, arg2 : {0}, {1}".format(arg1, arg2)

# 调用：
F(100, 100)

# 看起来给出的都是100，但是实际执行的就是200,100了，
# 没有中间商转差价，只是给你看看的

