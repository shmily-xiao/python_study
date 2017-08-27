#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  摄像头 人脸检测
"""
import cv2
import os

current_path = os.getcwd()
classifier = current_path +  '\\haarcascade_frontalface_alt2.xml'

# import sys
# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)

faceCascade = cv2.CascadeClassifier(classifier)


video_capture = cv2.VideoCapture(0)

count = 0

while True:

   # Capture frame-by-frame

   ret, frame = video_capture.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   # cv2.imshow('Video2', frame)
   if cv2.waitKey(1) & 0xFF == ord('p'):
       cv2.imwrite("zipai{0}.jpg".format(count),frame)
       print "success {0} !".format(count)
       count = count + 1
       # break


   faces = faceCascade.detectMultiScale(

       gray,

       scaleFactor=1.2,

       minNeighbors=5,

       minSize=(30, 30),

       flags=cv2.CASCADE_SCALE_IMAGE

   )

   # Draw a rectangle around the faces

   for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


   # Display the resulting frame

   cv2.imshow('Video', frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):

       break

# When everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()