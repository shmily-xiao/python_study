#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    给定一个数组 构造一个二叉树
"""

class Tree(object):
    def __init__(self, data= None):
        self.data = data
        self.lchild = None
        self.rchild = None


def find_root(tree, value):

    if not tree:
        return None

    if tree.data == None or tree.data == value:
        return tree

    root = find_root(tree.lchild, value)

    if not root or root.data != value:
        root = find_root(tree.rchild, value)
    return root


def build_tree(tree, a, i=0):
    if i >= len(a):
        return tree
    index = (i-1)/2
    if index < 0:
        index = 0
    root = find_root(tree, a[index])
    if root.data == None:
        root.data = a[i]
        i= i+1
        build_tree(tree, a, i)

    root.lchild = Tree(a[i])
    if i+1 < len(a):
        root.rchild = Tree(a[i+1])
    i = i + 2
    build_tree(tree, a, i)

if __name__ == '__main__':

    a = [1,2,3,4,8,6,9]
    tree = Tree()
    build_tree(tree, a)
    print tree