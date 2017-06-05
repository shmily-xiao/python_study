#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A:
    def prt(self):
        print "A"


class B(A):
    def prt(self):
        print "B"


class C(A):
    def prt(self):
        print "C"


class D(A):
    pass


class E:
    def prt(self):
        print "E"


class F:
    pass


def test(arg):
    arg.prt()


a = A()
b = B()
c = C()
d = D()
e = E()
f = F()

test(a)
test(b)
test(c)
test(d)
test(e)
# test(f)