#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from face_detection.facerec.feature import Fisherfaces
from face_detection.facerec.distance import EuclideanDistance
from face_detection.facerec.classifier import NearestNeighbor
from face_detection.facerec.model import PredictableModel
from face_detection.facerec.validation import KFoldCrossValidation,LeaveOneOutCrossValidation
from face_detection.facerec.visual import subplot
from face_detection.facerec.util import minmax_normalize
from face_detection.facerec.serialization import save_model, load_model
# import numpy, matplotlib and logging
import numpy as np
from PIL import Image
import matplotlib.cm as cm
import logging

def read_images(path, sz=None):
    """Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes 

    Returns:
        A list [X,y]

            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
    """
    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = Image.open(os.path.join(subject_path, filename))
                    im = im.convert("L")
                    # resize to given size (if given)
                    if (sz is not None):
                        im = im.resize(sz, Image.ANTIALIAS)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c = c+1
    return [X,y]

def train():
    current_path = os.getcwd()
    path = current_path + "\\att_faces"
    images,values = read_images(path)


