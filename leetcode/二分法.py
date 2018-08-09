#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---------------------------
        |
        |   |        砍掉h0高度之后剩下的长度的总和是S
    |   |   |
--------------------  砍掉
    |   |   |   |
    |   |   |   |   |   计算 h0
--------------------------
    h1  h2  h3  h4  h5

    已知 h1 .... hn 的树的高度
    已知最后我们砍掉一节 之后剩下的长度的总和是S

    求  h0

"""

def sum_left(h0 , h):
    """

    :param h0:  是一个数值
    :param h:  是一个list
    :return:  返回 砍掉之后的剩余的高度，，注意小于0的按照0来算

    """
    result = 0
    for item in h:
        if item - h0 > 0:
            result += item - h0

    return result

def get_half_h(start, end):
    if end>start:
        return start + (end-start)/2.0
    return start


def main(h, S):
    """
        二分法
    :param h:
    :param S:
    :return:
    """
    h_max = max(h)
    h_sum = sum(h)
    start = 0
    end = h_max

    while(True):
        h0 = get_half_h(start, end)
        temp_s = sum_left(h0, h)

        # 从工程的意义上讲米有绝对的相等，只有无限的接近
        if abs(temp_s - h_sum + S) < 0.0001:
            return h0

        if temp_s > h_sum - S:
            start = h0
        elif temp_s < h_sum - S:
            end = h0
        else:
            return h0




if __name__ == '__main__':

    h = [1,2,3,4,6,7,8,4,34,23,12,67,78,10]
    s = 20
    print main(h, s)