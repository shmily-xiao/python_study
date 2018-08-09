#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    对一个链表 进行 倒叙，
    要求是不能单独创建一个链表

    算法很巧妙，递归的方式， 构造一个 T 型的数据链

    如果是使用 栈 或者是 新建链表都会 产生额外的空间
"""


class MyLinkList(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def my_reversed(h):

    if h == None or h.next == None:
        return h
    result = my_reversed(h.next)
    h.next.next = h
    h.next = None
    return result

def print_link_list(h):
    if h == None:
        return h
    print h.data
    print_link_list(h.next)

if __name__ == '__main__':
    l1 = MyLinkList(1)
    l2 = MyLinkList(2)
    l1.next = l2
    l3 = MyLinkList(3)
    l2.next = l3
    l4 = MyLinkList(4)
    l3.next = l4
    l5 = MyLinkList(5)
    l4.next = l5
    l6 = MyLinkList(6)
    l5.next = l6
    l7 = MyLinkList(7)
    l6.next = l7
    l8 = MyLinkList(8)
    l7.next = l8

    print_link_list(l1)
    print "-------"
    l_reversed = my_reversed(l1)
    print_link_list(l_reversed)

