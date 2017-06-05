#!/usr/bin/env python
# -*- coding: utf8 -*-

import time

# 一个list的情况
def f_multiplication(x):
    return x*x
# array_list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_list_one = xrange(10000000)
array_list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultList_one = []
resultList_two = []
resultList_three = []

start = time.time()
for i in array_list_one:
    resultList_one.append(f_multiplication(i))
end = time.time()
time_one = end-start

start = time.time()
resultList_two = map(f_multiplication, array_list_one)
end = time.time()
time_two = end-start

start = time.time()
resultList_three = [f_multiplication(i) for i in array_list_one]
end = time.time()
time_three = end-start

print "for  time1 : %s" %time_one
print "map  time2 : %s" %time_two
print "List comprehension time3 : %s" %time_three


# # 多个list的情况
# def f_addition(x,y):
#     return x+y
# print map(f_addition, array_list_one, array_list_two)