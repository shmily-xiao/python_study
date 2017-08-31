#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
from PIL import Image
import numpy as np
import sys

from face_detection.study_test.model import EigenfacesModel, FisherfacesModel
from face_detection.study_test.scripts.subspace import LBP

class RecognitionUtils(object):
    def default(self):
        pass

    def read_images(self,path, sz=None):
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
        X, y = [], []
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
                c = c + 1
        return [X, y]


    def get_image(self, path):

        # 读取图片
        image = cv2.imread(path)
        # 将彩色变成灰度的
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image

    def video_image_stream(self):

        return cv2.VideoCapture(0)


    def cut_face(self, faces, image):
        face_imgs = []

        for x, y, width, height in faces:
            face_img = image[y:y + height, x:x + width]
            face_img = cv2.resize(face_img, (92, 112), fx=0, fy=0)
            face_imgs.append(face_img)
        return face_imgs

    def detect_faces(self, image):
        current_path = os.getcwd()
        # 效果最差 haarcascade_frontalface_alt_tree
        # 效果适中 haarcascade_frontalface_alt2
        # 效果容错率较高 haarcascade_frontalface_default
        classifier = current_path + '\\..\\..\\haarcascade_frontalface_alt2.xml'

        # 获取人脸检测训练数据
        face_casacade = cv2.CascadeClassifier(classifier)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 探测人脸
        # faces = face_casacade.detectMultiScale(image)
        faces = face_casacade.detectMultiScale(

            image,

            scaleFactor=1.2,

            minNeighbors=5,

            minSize=(30, 30),

            flags=cv2.CASCADE_SCALE_IMAGE

        )
        # x, y, width, height
        return faces

    def train(self):
        current_path = os.getcwd()
        all_faces = current_path + '\\..\\..\\att_faces'
        [X, y] = self.read_images(all_faces)
        print y
        # X = LBP(X)
        # self.model = EigenfacesModel(X, y)
        self.model = FisherfacesModel(X, y)


    def recognition(self, need_rec_face):
        return self.model.predict(need_rec_face)


if __name__ == '__main__':
    util = RecognitionUtils()
    util.train()
    print "训练结束。。。"
    video_capture = cv2.VideoCapture(0)
    while True:
        # 输入的图片
        ret, image = video_capture.read()
        # 检测到的人脸
        faces = util.detect_faces(image)


        for (x, y, width, height) in faces:
            face_img = image[y:y + height, x:x + width]
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            face_img = cv2.resize(face_img, (92, 112), fx=0, fy=0)
            name = util.recognition(face_img)
            cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 1)
            cv2.putText(image, str(name), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

        # Display the resulting frame

        cv2.imshow('Video', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break





        


