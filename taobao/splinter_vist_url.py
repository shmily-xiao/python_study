#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re
import requests
import json
from splinter import Browser

coupon_pattern = re.compile("https://uland.taobao.com/?\w*/?\w*.*\">")
lemon_url_pattern = re.compile("/goods/detail/\d+")

def get_chorme():
    executable_path = {'executable_path': '/Users/zaijunwang/workspace/python/python_study/taobao/chromedriver'}

    browser = Browser('chrome', **executable_path)
    return browser



def inspect_available_coupon_url_by_splinter(url):
    """
        判断这个url是否有效

    :param url:
    :return:
    """
    if not url:
        return True

    browser = get_chorme()

    #login 126 email websize
    browser.visit(url)

    #wait web element loading
    # time.sleep(0.5)

    selector = '[class="coupons-price"]'
    div = browser.find_by_css(selector)
    try:
        print div.html
    except Exception as e:
        return False
    finally:
        browser.quit()

    # time.sleep(0.5)
    #close the window of brower

    return True




def get_coupon_url_by_splinter(url):
    """

       <p class="desc">有效期内领券下单，享受立减优惠！</p>
                           <a data-ga-event="折扣详情页:点击:领券按钮:1" need-ahc="1" target="_blank" class="buy-btn" href="https://uland.taobao.com/coupon/edetail?e=R%2Bmb2p3j4S4N%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuB83XxQcrqLlGYTNJBh1vVXz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPpdxre2qKEMA5kwz9ud4Fzggv7%2F1L7GqqX%2FolqzSPlG2KRVSb0PuALM%3D&amp;af=1&amp;pid=mm_128981071_39972563_150364908">
                               领券立减<em>5.00</em>元
                           </a>

    """
    if not url:
        return
    browser = get_chorme()

    # login 126 email websize
    browser.visit(url)

    # wait web element loading
    # time.sleep(0.5)

    selector = '[class="buy-area"]'
    div = browser.find_by_css(selector)

    try:
        text = div.html
        text = text.encode("utf-8")
        if not text:
            return None
        if "领券立减" not in text:
            return None
        result = coupon_pattern.findall(text)[0]
        return result[:-2]
    except Exception as e:
        print e
        return None
    finally:
        # close the window of brower
        browser.quit()

    # time.sleep(0.5)

def get_last_key():
    url = 'http://www.lmyouxuan.com/index?home=31'

    r = requests.get(url)
    html = r.text

    results = lemon_url_pattern.findall(html)

    if not results:
        return False

    return get_key_from_url(results[0])
    # return long(result.split("/").pop())


def get_key_from_url(url):
    return long(url.split("/").pop())


def get_keys_by_page(skip=0, home=""):

    if home:
        nextpage = "http://www.lmyouxuan.com/nextPage?page={0}&size=40&home={1}&isSearch=false"
    else:
        nextpage = "http://www.lmyouxuan.com/nextPage?page={0}&size=40&isSearch=false"

    for item in xrange(625):
        item = item + skip
        if home:
            url = nextpage.format(item + 1, home)
        else:
            url = nextpage.format(item + 1)
        r = requests.get(url)
        print url
        html = r.json()
        page_data = json.loads(html.get("data",""))
        # for item in page_data:
        #     print item.get("couponUrl")

        yield [item.get("couponUrl") for item in page_data]
        # print lemon_url_pattern.findall(html)




def others():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome('/Users/zaijunwang/workspace/python/python_study/taobao/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/xhtml')
    time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()




if __name__ == '__main__':
    # websize3 ='https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532513807601&sign=820a8c3eee1dc0ef8b93536a33d4df4b&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22e%22%3A%2270j3Bx7OhTEN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDutNTUrfdfC1CbTDaeY22YE3z%2F5lYwoL5IC0DytI6FkgR2pj%2BrIzI8SMweCqqdVU5pfOdaPeFJvj2RMjz%2FiQJRwmSLnIuvFTVk%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D'
    websize3 ='https://uland.taobao.com/coupon/edetail?e=8enoEyP1lB8N%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuKXH4Dp204Jn8UJYok44yznz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPporNYNlJ3NzEHNKdtmA%2FPZaEEz%2FJ22qjhezg1wrFfY3FlDJQsv%2B1e4%3D&af=1&pid=mm_128981071_39972563_150364908'
    # websize3 ='https://uland.taobao.com/coupon/edetail?e=54PS3TEfQTAN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDujHFe%2Fji3MW0QcvtLoqPS4Xz%2F5lYwoL5IC0DytI6FkgQtgMf7FUs3ubfxsi1c%2FlbUd3dYRnWQnO%2Bbg%2FMkcTHCkTNe5EyezcrR&af=1&pid=mm_128981071_39972563_150364908'

    # splinter_coupon(websize3)

    skips = [0, 626, 625*2+1, 625*3+1]
    pages = get_keys_by_page(home=31)
    print pages
    # keys = map(get_key_from_url, pages)

    # print keys
    #
    # key = get_last_key()
    # print "last key{0}".format(key)
    #
    # lemon_url = "http://www.lmyouxuan.com/goods/detail/{0}".format(key)
    # print lemon_url
    #
    # ali_coupon_url = get_coupon_url_by_splinter(lemon_url)
    #
    # print inspect_available_coupon_url_by_splinter(ali_coupon_url)




    # others()