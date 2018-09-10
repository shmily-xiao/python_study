#! /usr/bin/env python
# -*-coding:utf-8 -*-


"""
curl -F "image=@a.jpg" http://xxxx.cn:8000/rest/1.0/image/face-recog/face-recog\?method\=fr -H 'Authorization: Basic password=='
"""
import numpy as np
import requests
from requests.auth import HTTPBasicAuth

def get_face_from_video():
    face = ""

    return face


def face_detection():
    """
        检测和提取特征值
    :return:
    """
    url = "http://xxxxx:8000/rest/1.0/image/face-recog/face-recog?method=fr"

    method = "POST"

    file_path = "/Users/zaijunwang/workspace/python/python_study/face_detection/image/6.jpg"

    file_object=open(file_path,"rb")

    options={
        "files":{"image":file_object},
        "headers":{"Authorization":"Basic password=="}
    }

    # options={
    #     "files":{"image":file_object},
    #     "auth":HTTPBasicAuth('xxx', 'xxx')
    # }
    print options
    # r = requests.request(method,url,files={"image":file_object}, headers=headers)
    r = requests.request(method,url,**options)
    # print r.content
    # print r.text
    return r.json()

def face_recognition(face):
    """
        识别
    :return:
    """




    pass


if __name__ == '__main__':
    face = get_face_from_video()
    face_feature = face_detection()
    face_recognition(face_feature)