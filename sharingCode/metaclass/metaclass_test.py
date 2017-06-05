#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    name = 'foo'
    def bar(self):
        print 'bar'

def test(self):
    print 'test'

if __name__ == '__main__':
    f = Foo()
    print f.name
    # 等同创建了一个
    TestClass = type('TestClass', (object,), {'test': test,'name':'testName'})
    testClass = TestClass()
    testClass.test()
    print testClass.name
