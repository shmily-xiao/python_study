#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A(object):
    test = "12"
    def foo(self, x):
        print "exceuting foo(%s, %s)"%(self, x)

    @classmethod
    def class_foo(cls, x):
        # 这个可以通过cls使用类的资源
        print cls.test
        print "executing class_foo(%s, %s)"%(cls, x)

    @staticmethod
    def static_foo(x):
        # 这个仅仅是类的一个函数而已，你可以写在class外面也可以写在class里面
        print "executing static_foo(%s)"%x

if __name__ == '__main__':
    a = A()
    a.foo(1)
    a.class_foo(2)
    a.static_foo(4)
    A.class_foo(5)
    A.static_foo(6)

    print a.foo
    print a.class_foo
    print a.static_foo
