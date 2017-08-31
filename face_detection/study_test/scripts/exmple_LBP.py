#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# append tinyfacerec to module search path
sys.path.append("..")
# import numpy and matplotlib colormaps
import numpy as np
# import tinyfacerec modules
import os

from subspace import fisherfaces, project, reconstruct, LBP
from face_detection.study_test.util import normalize, asRowMatrix, read_images
from face_detection.study_test.visual import subplot

current_path = os.getcwd()
path = current_path + "\\..\\..\\att_faces"
# read images
[X, y] = read_images(path)
# perform a full pca
# X = LBP(X)
X = LBP(X)
[D, W, mu] = fisherfaces(asRowMatrix(X), y)
# import colormaps
import matplotlib.cm as cm

# turn the first (at most ) 16 eigenvectors into grayscale
# images ( note : eigenvectors are stored by column !)
E = []
for i in xrange(min(W.shape[1], 16)):
    e = W[:, i].reshape(X[0].shape)
    E.append(normalize(e, 0, 255))
# plot them and store the plot to " python_fisherfaces_fisherfaces . pdf "
subplot(title=" LBP AT&T Facedatabase ", images=E, rows=4, cols=4, sptitle="Fisherface ", colormap=cm.jet,
        filename=" python_LBP.jpg")

EE = []
for i in xrange(min(W.shape[1], 20)):
    e = W[:, i].reshape(-1, 1)
    P = project(e, X[0].reshape(1, -1), mu)
    R = reconstruct(e, P, mu)

    R = R.reshape(X[0].shape)
    EE.append(normalize(R, 0, 255))

subplot(title=" LBP Reconstruction Yale FDB ", images=EE, rows=4, cols=5, sptitle=" Fisherface",
        colormap=cm.gray, filename="python_LBP_reconstruction.jpg")
