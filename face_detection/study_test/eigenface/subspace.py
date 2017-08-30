#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def pca(X, y, num_components=0):
    """
    获取特征值，特征向量和 平均值
    :param X: 
    :param y: 
    :param num_components: 
    :return: 
    """
    # 得到矩阵的 行和列
    # n 为列 d 行
    # [n, d] = X.shape
    [d, n] = X.shape
    if (num_components <= 0) or (num_components > n):
        num_components = n
    # 计算均值
    mu = X.mean(axis=0)
    # 减去均值
    X = X - mu
    if n > d:
        # 如果行大于列
        # 这么做的原因是，生成最小的队列(d x d)

        # 计算两个数的点积 转置之后 X 它本身  相当于平方
        C = np.dot(X.T, X)
        # 计算对称矩阵的 特征值和特征向量
        [eigenvalues, eigenvectors] = np.linalg.eigh(C)
    else:
        # 列大于行

        # 计算两个数的点积 转置之后 X 它本身  相当于平方
        C = np.dot(X, X.T)
        # 计算对称矩阵的 特征值和特征向量
        [eigenvalues, eigenvectors] = np.linalg.eigh(C)

        for i in xrange(n):
            #  np.linalg.norm(eigenvectors[:, i]) 计算矩阵获向量的范数
            # 默认是 Frobenius norm
            # 就是 将 所有的元素平方 求和 开根号
            # http://astrowww.bnu.edu.cn/sites/Computational_Astronomy/html/5ketang/2jiangyi/Chen_kejian/%E6%96%B010.pdf
            # 这里可以理解是为了“归一化”
            eigenvectors[:, i] = eigenvectors[:, i] / np.linalg.norm(eigenvectors[:, i])
    # or simply perform an economy size decomposition
    # eigenvectors , eigenvalues , variance = np. linalg . svd (X.T, full_matrices = False )
    # sort eigenvectors descending by their eigenvalue
    # 按照特征值倒叙排列
    idx = np.argsort(-eigenvalues)
    # 按照刚刚排的顺序赋值
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # select only num_components
    # components 部分
    # num_components <= min(n,d)
    eigenvalues = eigenvalues[0: num_components].copy()
    eigenvectors = eigenvectors[:, 0: num_components].copy()
    return [eigenvalues, eigenvectors, mu]


def project(W, X, mu=None):
    """
        如果均值存在就计算减去均值的点积，否则就直接计算
    :param W: 
    :param X: 
    :param mu: 
    :return: 
    """
    if mu is None:
        return np.dot(X, W)
    return np.dot(X - mu, W)


def reconstruct(W, Y, mu=None):
    """
    reconstruct 重建
    :param W: 
    :param Y: 
    :param mu: 
    :return: 
    """
    if mu is None:
        return np.dot(Y, W.T)
    return np.dot(Y, W.T) + mu
