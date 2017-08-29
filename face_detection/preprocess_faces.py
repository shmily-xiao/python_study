#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  从照片中获取人脸，并将其设置成为92x112的大小
"""
import cv2
import os

current_path = os.getcwd()
print current_path
for index in xrange(10):
    photopath = current_path + '\\image\\{0}.jpg'.format(index+1)
    # 效果最差 haarcascade_frontalface_alt_tree
    # 效果适中 haarcascade_frontalface_alt2
    # 效果容错率较高 haarcascade_frontalface_default
    classifier = current_path +  '\\haarcascade_frontalface_alt2.xml'

    #读取图片
    image = cv2.imread(photopath)

    #灰度转换
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #获取人脸检测训练数据
    face_casacade = cv2.CascadeClassifier(classifier)

    #探测人脸
    faces = face_casacade.detectMultiScale(image)

    # 方框的颜色和粗细
    color = (0, 0, 255)
    strokeWeight = 1
    # while True:
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color, strokeWeight)
        face_img = image[y:y + height, x:x + width]
        face_img = cv2.resize(face_img,(92,112),fx=0,fy=0)
        path = current_path+"\\att_faces\\s41\\{0}.pgm".format(index+1)
        print path
        cv2.imwrite(path,face_img)
        cv2.imshow("1", face_img)
        cv2.waitKey(1)


# When everything is done, release the capture
cv2.destroyAllWindows()