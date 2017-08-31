#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# 为了将模块添加到搜索路径
sys.path.append("..")

import numpy as np
import matplotlib.cm as cm

from subspace import pca
from face_detection.study_test.util import asRowMatrix, read_images, normalize
from face_detection.study_test.visual import subplot
from face_detection.study_test.scripts.subspace import project, reconstruct, LBP

# 读取图片
current_path = os.getcwd()
path = current_path + "\\..\\..\\att_faces"
[X, y] = read_images(path)
# X = LBP(X)
# X = LBP(X)
# 执行一个完整的主成分分析
# 获取特征值，特征向量，均值
[D, W, mu] = pca(asRowMatrix(X), y)

E = []
for i in xrange(min(len(X), 16)):
    e = W[:, i].reshape(X[0].shape)
    E.append(normalize(e, 0, 255))
subplot(title="Eigenfaces AT&T Facedatabase", images=E, rows=4, cols=4, sptitle="Eignface",
        colormap=cm.jet, filename="python_pca_eigenfaces.jpg")

# 重建
# reconstruction steps
steps = [i for i in xrange(10, min(len(X), 320), 20)]
EE = []
for i in xrange(min(len(steps), 16)):
    numEvs = steps[i]
    # 获取第一照片
    P = project(W[:, 0:numEvs], X[19].reshape(1, -1), mu)

    R = reconstruct(W[:, 0:numEvs], P, mu)

    # 重新构建 同时压平
    R = R.reshape(X[0].shape)
    EE.append(normalize(R, 0, 255))

subplot(title=" Reconstruction AT&T Facedatabase ", images=EE, rows=4, cols=4, sptitle="Eigenvectors",
            sptitles=steps, colormap=cm.gray, filename="python_pca_reconstruction.jpg")
