#!/usr/bin/env python
# -*- coding:utf-8 -*-

import foo

a = [1, 'python']

a = "a string"

def func():
    a = 1
    b = 257
    print(a + b)

print a

if __name__ == '__main__':
    func()
    foo.add(1,2)
    func2 = type("func2",(object,),{"funnc":func, "b":2})
    f = func2()
    print f.b
    print f.funnc
    print func
