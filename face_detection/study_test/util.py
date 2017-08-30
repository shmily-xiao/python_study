#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
import numpy as np
import sys


def read_images(path, sz=None):
    """
    读取读片信息
    :param path: 图片信息的根目录
    :param sz: 如果需要设置重置大小
    :return: 
    """
    c = 0
    X, y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = Image.open(os.path.join(subject_path, filename))
                    im = im.convert("L")
                    # resize to given size (if given )
                    if (sz is not None):
                        im = im.resize(sz, Image.ANTIALIAS)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error ({0}) : {1} ".format(errno, strerror)
                except:
                    print " Unexpected error :", sys.exc_info()[0]
                    raise
            c = c + 1
    return [X, y]


def asRowMatrix(X):
    """
    将矩阵 X 从三维变成2维矩阵，原来的第三维压平到第二维上
    :param X: 
    :return: 
    """
    if len(X) == 0:
        return np.array([])
    # 创建一个空矩阵
    mat = np.empty((0, X[0].size), dtype=X[0].dtype)
    for row in X:
        # 将两个矩阵合并
        mat = np.vstack((mat, np.asarray(row).reshape(1, -1)))
    return mat


def asColumnMatrix(X):
    if len(X) == 0:
        return np.array([])
    mat = np.empty((X[0].size, 0), dtype=X[0].dtype)
    for col in X:
        mat = np.hstack((mat, np.asarray(col).reshape(-1, 1)))
    return mat

def normalize(X, low, high, dtype=None):
    # 将输入装换成为矩阵
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    # normalize to [0...1].
    # 归一化
    X = X - float(minX)
    X = X / float(maxX - minX)

    # 设置 比例 ， 放大比例
    X = X * (high - low)
    X = X + low

    if dtype is None:
        return np.asarray(X)

    # dtype 默认情况下，数据类型是从输入数据中推断出来的。
    return np.asarray(X, dtype=dtype)



if __name__ == '__main__':
    X = [[2.3, 1, 34, 5], [34, 45, 45, 434, 33]]
    X = np.asarray(X)
    print np.empty((0, X[0].size), dtype=X[0].dtype)
