#! /usr/bin/env python
# -*-coding:utf-8 -*-


"""
curl -F "image=@a.jpg" http://zzxzz:8000/rest/1.0/image/face-recog/face-recog\?method\=fr -H 'Authorization: Basic Y2xvdWRhaz='
"""
import os
import sys
import cv2
import time
import copy
import numpy as np
import requests
from pymongo import MongoClient
from requests.auth import HTTPBasicAuth


class FaceRecognition(object):
    def __init__(self):
        client = MongoClient(host='127.0.0.1', port=27017)
        # 数据库
        self.db = client["face_db"]
        # 存放image的文件夹地址
        self.path = "D:/working/faces"
        self.test_path = "D:/working/faces_test"
        # 第三方特征提取地址
        self.face_feature_url = "http://zzzz:8000/rest/1.0/image/face-recog/face-recog?method=fr"
        # 阈值
        self.thred = 0.566
        # 历史的比对数据
        self.faces = []
        # self._init_cv2_()


    def face__init__(self):
        """
            将所有的可用的人的脸都记录下来
            就是事先将所有要识别的用户的数据先做一次特征抽取，存放在mongo中或者是redis中
        :return: 
        """
        for image_path in self.__read_my_images(self.path):
            image_path = image_path.replace("\\", "/")
            print image_path
            face_features = self.__face_feature(image_path)
            # 可能一个图有多张脸，接口是这么设计的
            for face in face_features:
                filename = face.get("img").split(".").pop(0)
                self.db.faces.insert({"data": {filename: face.get("face_info")[0]}})

    def get_face_from_video(self, image):
        # face = "D:/working/faces_test/wangzaijun.jpg"
        face = self.test_path+"/test.jpg"
        start = time.time()
        cv2.imwrite(face, image)
        print "save : ", time.time() - start
        url = self.face_feature_url
        method = "POST"

        file_object = open(face, "rb")
        print " read image : ", time.time() - start
        options = {
            "files": {"image": file_object},
            "headers": {"Authorization": "Basic sdssssdA=="}
        }

        # options={
        #     "files":{"image":file_object},
        #     "auth":HTTPBasicAuth('xxx', 'xxx')
        # }
        # r = requests.request(method,url,files={"image":file_object}, headers=headers)

        print "send to cloud  ----"
        r = requests.request(method, url, **options)

        print " get feature : ", time.time() - start

        print "get data from cloud  ++++"

        return r.json().get("res")[0]
        # return self.__face_feature(face)[0]

        # return face

    def face_recognition(self, face):
        """
            识别
        :return:
        """
        print "start recognition --------"
        if not self.faces:
            for item in self.db.faces.find({}):
                self.faces.append({"data":item.get("data",{})})

        new_feature = face.get("face_info")[0].get("feature")

        for face_item in self.faces:
            for k, v in face_item.get("data").items():
                old_feature = v.get("feature")
                score = np.dot(new_feature, old_feature)
                if score > self.thred:
                    print "end recognition --------"
                    return k
        print "end recognition --------"
        return "unkown"

    def __face_feature(self, path):
        """
            检测和提取特征值
        :return:
        """
        url = self.face_feature_url
        method = "POST"

        file_object = open(path, "rb")
        options = {
            "files": {"image": file_object},
            "headers": {"Authorization": "Basic ssssA=="}
        }

        # options={
        #     "files":{"image":file_object},
        #     "auth":HTTPBasicAuth('xxx', 'xxx')
        # }
        # r = requests.request(method,url,files={"image":file_object}, headers=headers)
        r = requests.request(method, url, **options)
        return r.json().get("res")

    def __read_my_images(self, path):
        """
            获取image的路径
        :param path: 
        :return: 
        """
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                yield os.path.join(dirname, filename)

    def wrapper_length(self, x, y, w, h, alph=0.3):
        x_l = x - alph * w
        x_r = x + alph * w + w
        y_l = y - alph * h
        y_r = y + alph * h + h

        return x_l, x_r, y_l, y_r


if __name__ == '__main__':
    fr = FaceRecognition()
    # fr.face__init__()

    current_path = os.getcwd()
    classifier = current_path + '\\..\\haarcascade_frontalface_alt2.xml'
    # classifier = "D:/Python/python_study/face_detection/haarcascade_frontalface_alt2.xml"
    print classifier

    # 获取人脸检测训练数据
    face_casacade = cv2.CascadeClassifier(classifier)
    video_capture = cv2.VideoCapture(0)

    start_time = time.time()
    name = ""

    while (True):
        end_time = time.time()

        ret, image = video_capture.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_casacade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # print end_time-start_time
        if int(end_time-start_time) % 5 == 0 or name=="unkown":
            start_time = time.time()
            name = ""


        # Draw a rectangle around the faces
        # try:
        for (x, y, w, h) in faces:
            x_l, x_r, y_l, y_r = fr.wrapper_length(x, y, w, h)
            face_img = image[int(y_l):int(y_r), int(x_l):int(x_r)]

            if not name:
                # 人脸抓取
                test_face = fr.get_face_from_video(face_img)
                # 人脸识别
                name = fr.face_recognition(test_face)
            # print name

            # 人脸标记
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)

            # 输出文字
            cv2.putText(image, name, (int(x), int(y)), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)

        # except Exception as e:
        #     print e
        #     continue
        # Display the resulting frame

        cv2.imshow('Video', image)

        # time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # face = fr.get_face_from_video().get("face_info", [])
    # print fr.face_recognition(face)

    video_capture.release()
    cv2.destroyAllWindows()
