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
    [n, d] = X.shape
    # [d, n] = X.shape
    if (num_components <= 0) or (num_components > n):
        num_components = n
    # 计算均值
    mu = X.mean(axis=0)
    # 减去均值
    X = X - mu
    if n < d:
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


def lda(X, y, num_components=0):
    # 将输入转化成矩阵
    y = np.asarray(y)
    # 获取矩阵的行数和列数
    [n, d] = X.shape
    # 数组去重
    c = np.unique(y)

    if (num_components <= 0) or (num_components > (len(c) - 1)):
        num_components = len(c) - 1
    # 计算X的均值 总的均值
    meantotal = X.mean(axis=0)
    # 创建 d阶 0矩阵
    Sw = np.zeros((d, d), dtype=np.float32)
    Sb = np.zeros((d, d), dtype=np.float32)

    for i in c:
        # 找到 y 数组中 第一个 为 i 的元素
        # y = [1,2,3,4]
        #  y = np.asarray(y)
        # np.where(y==2) ==> (array([1], dtype=int64),)
        # np.where(y==3) ==> (array([2], dtype=int64),)
        Xi = X[np.where(y == i)[0], :]
        # 计算每个 Xi 的均值， 每类照片的第一张照片的均值
        meanClass = Xi.mean(axis=0)

        Sw = Sw + np.dot((Xi - meanClass).T, (Xi - meanClass))
        # 这里n 对应公式里面的Ni ，但是我们这里是数组都是登长的，所以直接就是n，n是列，是n类
        Sb = Sb + n * np.dot((meanClass - meantotal).T, (meanClass - meantotal))

    # 计算特征值和特征向量
    # eig 计算一个方阵的特征值和特征向量。
    # np.linalg.inv(Sw) 计算矩阵 Sw 的逆
    eigenvalues, eigenvectors = np.linalg.eig(np.linalg.inv(Sw) * Sb)

    # 排序
    idx = np.argsort(- eigenvalues.real)
    eigenvalues, eigenvectors = eigenvalues[idx], eigenvectors[:, idx]

    # num_components 种类的数量
    eigenvalues = np.array(eigenvalues[0: num_components].real, dtype=np.float32, copy=True)
    eigenvectors = np.array(eigenvectors[0:, 0: num_components].real, dtype=np.float32, copy=True)

    return [eigenvalues, eigenvectors]


def fisherfaces(X, y, num_components=0):
    """
    这里都是在翻译论文中的公式
    :param X: 
    :param y: 
    :param num_components: 
    :return: 
    """
    y = np.asarray(y)
    [n, d] = X.shape
    c = len(np.unique(y))
    [eigenvalues_pca, eigenvectors_pca, mu_pca] = pca(X, y, (n - c))
    [eigenvalues_lda, eigenvectors_lda] = lda(project(eigenvectors_pca, X, mu_pca), y, num_components)
    eigenvectors = np.dot(eigenvectors_pca, eigenvectors_lda)
    return [eigenvalues_lda, eigenvectors, mu_pca]


def LBP(X):
    """
    (x-1,y-1) \   (x,y-1) \ (x-1,y-1)
    -------------------------------------
    (x-1,y)   \   (x,y)   \ (x+1,y)
    -------------------------------------
    (x-1,y+1) \  (x,y+1)  \ (x+1,y+1)
    
    对图像进行预处理
    局部二值模式
    :param X: 
    :return: 
    """
    # A = np.asarray(X)
    A = np.asarray(X)
    LBP_A = np.zeros(A.shape)
    index = 0
    for array in A:
        [cols, rows] = array.shape
        for x in xrange(cols):
            for y in xrange(rows):
                sum = 0
                center = array[x][y]
                sum = sum + compute_center_value(array, cols, rows, x-1, y-1,center, 7)
                sum = sum + compute_center_value(array, cols, rows, x, y-1,center, 6)
                sum = sum + compute_center_value(array, cols, rows, x-1, y-1,center, 5)
                sum = sum + compute_center_value(array, cols, rows, x+1, y,center, 4)
                sum = sum + compute_center_value(array, cols, rows, x+1, y+1,center, 3)
                sum = sum + compute_center_value(array, cols, rows, x, y+1,center, 2)
                sum = sum + compute_center_value(array, cols, rows, x-1, y+1,center, 1)
                sum = sum + compute_center_value(array, cols, rows, x-1, y,center, 0)

                LBP_A[index][x][y] = sum

        index = index + 1

    return LBP_A

def compute_center_value(array, cols, rows, x,y,center, num):
    """
    
    :param array:  矩阵
    :param cols:   矩阵的列
    :param rows:   矩阵的行
    :param x:      所选的x位置
    :param y:      所选的y位置
    :param center: 9宫格的中间值
    :param num:    00010000 比如第一个1 的num为 4 ，从0开始计算
    :return: 
    """
    if cols > x > 0 and rows >y > 0:
        if array[x][y] >= center:
            return 2**num
    return 0

# 这里可能和公式有点不同的地方，那是因为利用了一个公式
# A*B^T = (B*A)^T
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


if __name__ == '__main__':
    # x = [[1, 2], [2, 3]]
    # y = [[2, 3], [3, 4]]
    # print np.dot(np.asarray(x), np.asarray(y).T)
    # print np.dot(np.asarray(y), np.asarray(x)).T
    X = [[
        [1, 2, 3, 4, 4, 4, 4, 46, 6, 3, 2],
        [12, 2, 3, 4, 5, 4, 4, 46, 6, 3, 2],
        [1, 23, 3, 4, 4, 4, 34, 46, 6, 3, 2],
        [1, 2, 3, 4, 6, 4, 4, 46, 6, 3, 2],
        [1, 22, 3, 4, 4, 4, 4, 46, 6, 3, 2],
        [1, 2, 3, 8, 41, 42, 4, 46, 6, 3, 2],
        [31, 2, 3, 42, 9, 4, 4, 46, 6, 3, 2],
        [1, 23, 3, 4, 4, 4, 43, 46, 6, 3, 2]],
        [
            [1, 2, 3, 4, 4, 4, 4, 46, 6, 3, 2],
            [12, 2, 3, 4, 5, 4, 4, 46, 6, 3, 2],
            [1, 23, 3, 4, 4, 4, 34, 46, 6, 3, 2],
            [1, 2, 3, 4, 6, 4, 4, 46, 6, 3, 2],
            [1, 22, 3, 4, 4, 4, 4, 46, 6, 3, 2],
            [1, 2, 3, 8, 41, 42, 4, 46, 6, 3, 2],
            [31, 2, 3, 42, 9, 4, 4, 46, 6, 3, 2],
            [1, 23, 3, 4, 4, 4, 43, 46, 6, 3, 2]
        ]
    ]
    print LBP(X)
