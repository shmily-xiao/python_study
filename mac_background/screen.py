#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import redis
import re
import os
import urllib
from appscript import app, mactypes


def change_background(path):
    """
        path = '/Users/zaijunwang/Pictures/screen/BulgariaPerseids.jpg'
    :param path:
    :return:
    """
    app('Finder').desktop_picture.set(mactypes.File(path))


def get_img_and_save():
    host = "http://www.bing.com"
    r = requests.get(host)
    html = r.text
    # html = 'body;g_img={url: "/az/hprichbg/rb/SkylineparkRoller_ZH-CN8492771279_1920x1080.jpg",id:'
    # print html
    # my_compile = re.compile("/az/")
    my_compile = re.compile("/az/*.*\.jpg")

    # print my_compile.search(html).string
    # print my_compile.match(html)
    path = my_compile.findall(html)[0]
    # print re.findall("/az/(\w*/?)*.*\.jpg", html)
    if not path:
        return
    if not save_redis(path):
        return
    url = "http://www.bing.com" + path
    filename = path.split("/").pop()
    filename = os.path.join("/Users/zaijunwang/Pictures/screen", filename)
    urllib.urlretrieve(url, filename)
    change_background(filename)


def save_redis(path):
    r = redis.Redis(host='localhost', port=6380, decode_responses=True, password='lemonyouxuan')

    old = r.get('screen_background')
    if old == path:
        return None

    r.set('screen_background', path)  # key是"foo" value是"bar" 将键值对存入redis缓存

    # print(r['screen_background'])
    # print(r.get('screen_background'))  # 取出键name对应的值
    # print(type(r.get('screen_background')))

    return True


if __name__ == '__main__':
    get_img_and_save()
