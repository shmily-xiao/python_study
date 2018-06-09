#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_coupon(url):

    r = requests.get(url)

    # request('get', url, params=params, **kwargs)

    # if r.status_code != 200:
    #     print r.text
    #     return
    #
    print "@@@@@@"
    print r
    print r.text
    # response = r.text
    # response = {}


if __name__ == '__main__':
    url = "https://uland.taobao.com/coupon/edetail?e=34PzbL4zo7MN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuMQodiVQVXIh8wvfZDEc54Xz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPndSGf9fPWx9GBnyjvWaTjWHq9kebrdqTVaWzADq5SXuu%2FPDf6TAeNg%3D&af=1&pid=mm_128981071_39972563_150364908"
    # url = "https://uland.taobao.com/coupon/edetail?e=Fi8rBGeJnZIN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDudmx5v8Dmn2EHb7blVzn%2Fv3z%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPmaHwx9VNOriWp2ldIFoxIzm3%2FT758P4L%2BNULdsex8qnUVHuuSmScos%3D&af=1&pid=mm_128981071_39972563_150364908"
    get_coupon(url)