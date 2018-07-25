#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import re
import time



def visit_html():
    url = 'http://www.lmyouxuan.com/index?home=31'

    r = requests.get(url)
    html = r.text

    pattern = re.compile("/goods/detail/\d+")
    results = pattern.findall(html)

    if not results:
        return False

    result = results[0]
    key = long(result.split("/").pop())
    host_pattern = "http://www.lmyouxuan.com/goods/detail/{0}"
    for item in xrange(key):
        lemon_id = key - item
        try:
            requests.get(host_pattern.format(lemon_id))
        except Exception as e:
            pass

def visit_next(home=""):

    if home:
        nextpage = "http://www.lmyouxuan.com/nextPage?page={0}&size=20&home={1}&isSearch=false"
    else:
        nextpage = "http://www.lmyouxuan.com/nextPage?page={0}&size=20&isSearch=false"

    for item in xrange(500):
        if home:
            url = nextpage.format(item+1, home)
        else:
            url = nextpage.format(item + 1)
        requests.get(url)
        print url




if __name__ == '__main__':
    start = time.time()
    visit_html()
    end = time.time()

    print "use {0} second".format(end-start)

