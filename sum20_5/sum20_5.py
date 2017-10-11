#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

"""
    问题的描述：
    20个数，两两之差 的 和 是 5000， 去掉 5 个数之后 两两之差的和的最大值是多少
"""

b = []
for i in xrange(10):
    b.append(20-(i*2+1))

b = np.asarray(b)

num = 50
aa = []
for i in xrange(num):
    aa.append(num-i)

for a1 in aa:
    for a2 in aa:
        for a3 in aa:
            for a4 in aa:
                for a5 in aa:
                    for a6 in aa:
                        for a7 in aa:
                            for a8 in aa:
                                for a9 in aa:
                                    for a10 in aa:
                                         temp = 19 * a1 + 17 * a2 + 15 * a3 + 13 * a4 + 11 * a5 + 9 * a6 + 7 * a7 + 5 * a8 + 3 * a9 + a10
                                         if temp == 5000:
                                             print a1 ,a2, a3, a4, a5, a6, a7, a8, a9, a10
