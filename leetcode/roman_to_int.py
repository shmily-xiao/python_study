#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/roman-to-integer/description/

"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    my_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IX': 9,
        'IV': 4,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    length = len(s)
    sum = 0
    if not length:
        return sum
    while(i < length):
        temp = my_map.get(s[i])
        if i + 1 == length:
            return sum + temp
        d_temp = my_map.get(s[i:i+2], 0)
        if d_temp:
            sum += d_temp
            i = i + 2
        else:
            sum += temp
            i = i + 1


    return sum


if __name__ == '__main__':
    s = "MCMXCIV"
    print romanToInt(s)