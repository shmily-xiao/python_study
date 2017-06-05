#!/usr/bin/env python
# -*- coding: utf-8 -*-

# range(10) xrange(10)

def A(max):
    n = 0
    while n < max:
        yield n
        # print n
        n = n+1

class MyYield(object):
    max_num = 0
    n = 0

    def __init__(self, max_num):
        self.max_num = max_num

    def next(self):
        if self.n < self.max_num:
            temp = self.n
            self.n = self.n + 1
            return temp
        # 为了中断这个迭代器
        raise StopIteration()

if __name__ == '__main__':
    print "//------------自定义的迭代器---------------//"
    b = MyYield(3)
    print b.next() # 0
    print b.next() # 1
    print b.next() # 2
    # print b.next() #  <StopIteration>

    print "//----------------yeild-------------------//"
    print A(3) # <generator object A at 0x0267A6E8>
    for i in A(3):
        print i
    # 0
    # 1
    # 2



