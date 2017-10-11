#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
from PIL import Image
import numpy as np
import sys

from face_detection.study_test.model import EigenfacesModel, FisherfacesModel
from face_detection.study_test.scripts.subspace import LBP, LBP_one

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
                        im = cv2.imread(os.path.join(subject_path, filename))
                        # im = Image.open(os.path.join(subject_path, filename))
                        # im = im.convert("L")
                        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = self.cut_face(self.detect_faces(im),im)
                        if not faces:
                            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                            faces = cv2.resize(im,(150,150), fx=0, fy=0)
                        else:
                            faces = faces[0]
                        # resize to given size (if given)

                        if (sz is not None):
                            im = im.resize(sz, Image.ANTIALIAS)
                        # faces = LBP(faces)
                        X.append(np.asarray(faces, dtype=np.uint8))
                        y.append(c)
                    except IOError, (errno, strerror):
                        print "I/O error({0}): {1}".format(errno, strerror)
                    except:
                        print "Unexpected error:", sys.exc_info()[0]
                        raise
                c = c + 1
        X = LBP(X)
        return [X, y]

    def read_my_images(self,path):
        X, y = [], []
        for dirname, dirnames, filenames in os.walk(path):
            for subdirname in dirnames:
                if not "z" in subdirname and not "j" in subdirname:
                    continue

                subject_path = os.path.join(dirname, subdirname)
                for filename in os.listdir(subject_path):
                    try:
                        im = cv2.imread(os.path.join(subject_path, filename))
                        # im = Image.open(os.path.join(subject_path, filename))
                        # im = im.convert("L")
                        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = self.cut_face(self.detect_faces(im), im)
                        if not faces:
                            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                            # faces = cv2.resize(im, (110, 110), fx=0, fy=0)
                            continue
                        else:
                            faces = faces[0]
                        # resize to given size (if given)
                        # faces = LBP(faces)
                        X.append(np.asarray(faces, dtype=np.uint8))
                        y.append(subdirname)
                    except IOError, (errno, strerror):
                        print "I/O error({0}): {1}".format(errno, strerror)
                    except:
                        print "Unexpected error:", sys.exc_info()[0]
                        raise

        # X = LBP(X)
        return [X, y]


    def save(self, model):
        import shelve
        d = shelve.open('face_model.db', flag='c', protocol=2, writeback=True)
        d["W"] = model.W
        d["mu"] = model.mu
        d["y"] = model.y
        d["projections"] = model.projections
        d["X"] = model.X
        d.sync()
        d.close()


    def load(self):
        import shelve
        model_load = shelve.open("face_model.db")
        W =  model_load["W"]
        mu = model_load["mu"]
        y = model_load["y"]
        projections = model_load["projections"]
        X = model_load.X
        model_load.close()

        model = EigenfacesModel()
        model.mu = mu
        model.W = W
        model.y = y
        model.X = X
        model.projections = projections
        return model




    def get_image(self, path):

        # 读取图片
        image = cv2.imread(path)
        # 将彩色变成灰度的
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image


    def cut_face(self, faces, image):
        face_imgs = []
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        for x, y, width, height in faces:
            face_img = image[y:y + height, x:x + width]
            face_img = cv2.resize(face_img, (110, 110), fx=0, fy=0)
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
        self.model = EigenfacesModel(X, y)
        # self.model = FisherfacesModel(X, y)


    def recognition(self, need_rec_face):
        return self.model.predict(need_rec_face)




if __name__ == '__main__':
    util = RecognitionUtils()
    # util.train()
    # print "训练结束。。。"
    # video_capture = cv2.VideoCapture(0)
    # while True:
    #     # 输入的图片
    #     ret, image = video_capture.read()
    #     # 检测到的人脸
    #     faces = util.detect_faces(image)
    #
    #
    #     for (x, y, width, height) in faces:
    #         face_img = image[y:y + height, x:x + width]
    #         face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    #         face_img = cv2.resize(face_img, (150, 150), fx=0, fy=0)
    #         face_img = LBP_one(face_img)
    #         name = util.recognition(face_img)
    #         cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 1)
    #         cv2.putText(image, str(name), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    #
    #     # Display the resulting frame
    #
    #     cv2.imshow('Video', image)
    #
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    path = "D:\\working\\python\\python_study\\face_detection\\lfw"
    import time
    before = time.time()
    [X,y] = util.read_my_images(path)
    X = LBP(X)
    after = time.time()
    print after-before
    # model = EigenfacesModel(X, y)
    model = FisherfacesModel(X, y)
    util.save(model)

    video_capture = cv2.VideoCapture(0)
    while True:
        # 输入的图片
        ret, image = video_capture.read()
        # 检测到的人脸
        faces = util.detect_faces(image)


        for (x, y, width, height) in faces:
            face_img = image[y:y + height, x:x + width]
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            face_img = cv2.resize(face_img, (110, 110), fx=0, fy=0)
            face_img = LBP_one(face_img)
            name = model.predict(face_img)
            cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 1)
            cv2.putText(image, str(name), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

        # Display the resulting frame

        cv2.imshow('Video', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break





        


