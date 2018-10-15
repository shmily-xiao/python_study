#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  摄像头 人脸检测 按P拍照
"""
import cv2
import os

current_path = os.getcwd()
classifier = current_path +  '/haarcascade_frontalface_alt2.xml'

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
       cv2.imwrite(current_path+"\\image\\zipai{0}.jpg".format(count),frame)
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
       cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
       cv2.putText(frame, "wangzaijun", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1)


   # Display the resulting frame

   cv2.imshow('Video', frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):

       break


# def draw_text(self, frame, text, x, y, color=BGR_COMMON['green'], thickness=1.3, size=0.3, ):
#    if x is not None and y is not None:
#        cv2.putText(
#            frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)
# When everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()