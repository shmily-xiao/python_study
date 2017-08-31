#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
from PIL import Image
import cv2

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

def train_and_save():
    current_path = os.getcwd()
    path = current_path + "\\att_faces"
    images,values = read_images(path)
    # model = cv2.createEigenFaceRecognizer()
    model = cv2.createLBPHFaceRecognizer()
    # dir(model)
    model.train(images, np.asarray(values))
    model.save("model_faces.data")


def detect_faces(image):
    current_path = os.getcwd()
    # 效果最差 haarcascade_frontalface_alt_tree
    # 效果适中 haarcascade_frontalface_alt2
    # 效果容错率较高 haarcascade_frontalface_default
    classifier = current_path + '\\haarcascade_frontalface_alt2.xml'
    # classifier = current_path +  '\\haarcascade_frontalface_default.xml'

    # 灰度转换
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 获取人脸检测训练数据
    face_casacade = cv2.CascadeClassifier(classifier)

    # 探测人脸
    faces = face_casacade.detectMultiScale(image)

    return faces

def get_image():
    current_path = os.getcwd()
    print current_path
    # photopath = current_path + '\\zipai0.jpg'
    photopath = current_path + '\\image\\2.jpg'

    # 读取图片
    image = cv2.imread(photopath)

    return image

def predict(cv_image):

    faces = detect_faces(cv_image)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    result = None
    for x, y, width, height in faces:
        face_img = cv_image[y:y + height, x:x + width]
        face_img = cv2.resize(face_img, (92, 112), fx=0, fy=0)
        cv2.imshow("asdasd",face_img)
        # model = cv2.createFisherFaceRecognizer()
        # model = cv2.createFisherFaceRecognizer()
        model = cv2.createLBPHFaceRecognizer()
        model.load("model_faces.data")
        prediction = model.predict(np.asarray(face_img))
        print prediction[0]
        # result = {
        #     'face': {
        #         'name': prediction[0],
        #         'distance': prediction[1],
        #         'coords': {
        #             'x': str(faces[0][0]),
        #             'y': str(faces[0][1]),
        #             'width': str(faces[0][2]),
        #             'height': str(faces[0][3])
        #         }
        #     }
        # }
    # return result

if __name__ == '__main__':
    # model = cv2.createFisherFaceRecognizer()
    # print dir(model)# ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'getAlgorithm', 'getBool', 'getDouble', 'getInt', 'getMat', 'getMatVector', 'getParams', 'getString', 'load', 'paramHelp', 'paramType', 'predict', 'save', 'setAlgorithm', 'setBool', 'setDouble', 'setInt', 'setMat', 'setMatVector', 'setString', 'train', 'update']
    train_and_save()
    image = get_image()
    predict(image)

