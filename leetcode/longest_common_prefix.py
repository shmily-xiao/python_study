#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""

https://leetcode.com/problems/longest-common-prefix/description/


    还有一个解题思路是 ：
        对字符串排序，这样就只用比较第一个和最后一个了
"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str



    leetcode  32ms

    """
    if not strs:
        return ""

    result = ""

    for i in xrange(len(strs)):

        if i==0:
            result = strs[i]
            continue

        if not result:
            return ""

        while(result):
            if not strs[i].startswith(result):
                result = result[:-1]
            else:
                break

    return result

def longestCommonPrefixV2(strs):
    """
    :type strs: List[str]
    :rtype: str

    leetcode  20ms

    """
    if not strs:
        return ""

    result = ""

    temps = sorted(strs, key=lambda x:x)

    result = temps[0]
    last = temps[-1]

    while (result):
        if not last.startswith(result):
            result = result[:-1]
        else:
            break
    return result



if __name__ == '__main__':

    # strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]

    print longestCommonPrefixV2(strs)