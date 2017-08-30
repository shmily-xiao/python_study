#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  人脸检测
"""
import cv2
import os

current_path = os.getcwd()
print current_path
photopath = current_path + '\\att_faces\\s10\\6.pgm'
# 效果最差 haarcascade_frontalface_alt_tree
# 效果适中 haarcascade_frontalface_alt2
# 效果容错率较高 haarcascade_frontalface_default
classifier = current_path +  '\\haarcascade_frontalface_alt2.xml'
# classifier = current_path +  '\\haarcascade_frontalface_default.xml'


#读取图片x
image = cv2.imread(photopath)
cv2.imshow("xx", image)
#灰度转换
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#获取人脸检测训练数据
face_casacade = cv2.CascadeClassifier(classifier)

#探测人脸
faces = face_casacade.detectMultiScale(image)

# 方框的颜色和粗细
color = (0,0,255)
strokeWeight = 1
#弹出框名字
windowName = "Object Detection"

while True:  #为了防止
    #人脸个数
    # print(len(faces))
    count = 0
    for x, y, width, height in faces:
        count = count + 1
        print  x, y, width, height
        cv2.rectangle(image, (x, y), (x + width, y + height), color, strokeWeight)
        face_img = image[y :y + height,x :x + width]
        cv2.imshow(str(count), face_img)

    #展示人脸识别效果
    cv2.imshow(windowName, image)

    #点击弹出的图片，按escape键，结束循环
    if cv2.waitKey(20) == 27:
        break

#循环结束后，退出程序。
exit()
