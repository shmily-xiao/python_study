#!/usr/bin/env python
# -*- coding:utf-8 -*-


# python  反射

class A(object):

    DEFAULT = "zidongyi"

    def __init__(self):
        self.name = "nnn"

    def a_test(self):
        print "i am a test"

    def b_test(self, a1, a2):
        print "i am a test, {0}, {1}".format(a1, a2)


    def _c_test(self):
        print "asdewgernf gh"

    def __d_test(self):
        print "as32324 gh"


if __name__ == '__main__':
    a = A()
    data = {'a1':'sd',"a2":"wewe"}
    getattr(a, "b_test")(**data)
    getattr(a, "_c_test")()
    print dir(a)
    getattr(a, "_A__d_test")()