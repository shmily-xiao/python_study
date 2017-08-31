#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
# append tinyfacerec to module search path
sys . path . append ("..")
# import numpy and matplotlib colormaps
import numpy as np
# import tinyfacerec modules

from face_detection.study_test.util import read_images
from face_detection.study_test.model import EigenfacesModel

# 读取图片
current_path = os.getcwd()
path = current_path + "\\..\\..\\att_faces"
# read images
[X , y] = read_images (path)
# compute the eigenfaces model
# 其实这里就只训练了1-40的数据，X[0]的数据不在训练范围之类
model = EigenfacesModel (X [0:(len(X)-1)] , y [0:(len(y)-1)])
# get a prediction for the first observation
print " expected =", y[len(X)-1], "/", " predicted =", model.predict(X[len(X)-1])
