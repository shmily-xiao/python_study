#!/usr/bin/env python
# -*- coding: utf-8 -*-

# reduce( func, [1, 2,3] ) = func( func(1, 2), 3)

def f_multiplication(x,y):
    return x*y
n = 5
m_initial = 1 # m = 2
array_list = range(1, n+1)
print reduce(f_multiplication, array_list, m_initial)
# ( ( ( 1*2 ) *3 ) *4 ) *5

# 上面的写法等效于下面的写法
# print reduce(lambda x, y: x * y, range(1, n + 1))