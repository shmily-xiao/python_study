#!/usr/bin/env python
# -*- coding:utf-8 -*-

import foo
import time

a = [1, 'python']

a = "a string"

def func():
    a = 1
    b = 257
    print(a + b)

print a


def func1(a=1+1, b=[], c={}, t = time.time()):
    print a
    a += 1
    print a

    print id(b)
    b.append("func1")
    print b

    print c
    c["func1"]="func1"
    print c

    print t
    print " ---------- "

def fun2(d = 8*22, b=[], f={}):
    print d
    d += 1
    print d

    print id(b)
    b.append("func2")
    print b

    print f
    f["func2"] = "func2"
    print f
    print " ---------- "


if __name__ == '__main__':
    func()
    foo.add(1,2)
    func2 = type("func2",(object,),{"funnc":func, "b":2})
    f = func2()
    print f.b
    print f.funnc
    print func


    func1()
    func1()
    print "------"
    fun2()
    fun2()
