#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    arr = { "a","b","d","d","a","d","a","e","d","c"}
    统计该数组字母的个数并安从多到少进行输出
"""

# -------------------------------------------------
# 使用类似C的方式来写
# -------------------------------------------------

def main(a):
    d = {}

    # 生成一个map
    for i in xrange(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1

    # 将key 和value 对调
    v_k = {}

    for k, v in d.items():
        if v not in v_k:
            v_k[v] = [k]
        else:
            v_k[v].append(k)

    nums = v_k.keys()
    print nums
    # nums.sort(reverse=True)
    for i in xrange(len(nums)):
        index = i + 1
        for j in xrange(len(nums)-i):
            if index == len(nums):
                continue
            if nums[index] > nums[i]:
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp
            index += 1

    print nums
    result = []
    for i in nums:
        result.extend(v_k[i])
    return result



# -------------------------------------------------
# 使用python的方式
# -------------------------------------------------


def main2(a):
    from collections import OrderedDict
    d = {}
    # 生成一个map
    for i in xrange(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1

    return OrderedDict(sorted(d.items(), key=lambda t:t[1], reverse=True))


if __name__ == '__main__':
    a = [ "a","b","d","d","a","d","a","e","d","c"]
    print main(a)

    print main2(a).keys()

