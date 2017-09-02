#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from util import asRowMatrix
from scripts.subspace import pca, project,fisherfaces

from distance import EuclideanDistance


class BaseModel(object):
    def __init__(self, X=None, y=None, dist_metric=EuclideanDistance(), num_components=0):
        # 距离选择器,策略模式，默认有一个策略
        self.dist_metric = dist_metric
        self.num_components = 0
        # projections 预测
        self.projections = []
        self.W = []
        self.mu = []
        if (X is not None) and (y is not None):
            self.compute(X, y)

    def compute(self, X, y):
        raise NotImplementedError(" Every BaseModel must implement the compute method .")

    # 如果要预测的话这个地方的X就是我们要识别的照片了
    # 注意放入照片的size
    def predict(self, X):
        # 最大的可表示的数
        minDist = np.finfo("float").max
        minClass = -1
        Q = project(self.W, X.reshape(1, -1), self.mu)
        for i in xrange(len(self.projections)):
            # 计算距离
            dist = self.dist_metric(self.projections[i], Q)
            # 记录最小的那个距离
            # 然后返回相应的识别结果
            # 这地方可以设置阀值，超过一定的阀值就不算识别成功
            if dist < minDist:
                minDist = dist
                # 在子类中会动态添加
                minClass = self.y[i]

        return minClass


class EigenfacesModel(BaseModel):
    def __init__(self, X=None, y=None, dist_metric=EuclideanDistance(), num_components=0):
        super(EigenfacesModel, self).__init__(X=X, y=y, dist_metric=dist_metric,
                                              num_components=num_components)

    def compute(self, X, y):
        if not self.W and not self.mu :
            # 主成分分析，获取特征值，特征向量，和平均值
            [D, self.W, self.mu] = pca(asRowMatrix(X), y, self.num_components)

        print "特征值，特征向量，和平均值 计算完毕...."
        # store labels
        # 识别的类别存放的地方
        self.y = y
        self.X = X
        # store projections
        for xi in X:
            # 预处理
            # 将图像与特征向量做点积
            self.projections.append(project(self.W, xi.reshape(1,- 1), self.mu))

        print "预处理完毕..."

class FisherfacesModel(BaseModel):
    def __init__(self, X=None, y=None, dist_metric=EuclideanDistance(), num_components=0):
        super(FisherfacesModel, self).__init__(X=X, y=y, dist_metric=dist_metric,
                                              num_components=num_components)

    def compute(self, X, y):
        if not self.W and not self.mu:
            # 主成分分析，获取特征值，特征向量，和平均值
            [D, self.W, self.mu] = fisherfaces(asRowMatrix(X), y, self.num_components)
        print "特征值，特征向量，和平均值 计算完毕...."
        # store labels
        # 识别的类别存放的地方
        self.y = y
        self.X = X
        # store projections
        for xi in X:
            # 预处理
            # 将图像与特征向量做点积
            self.projections.append(project(self.W, xi.reshape(1,- 1), self.mu))

        print "预处理完毕..."


