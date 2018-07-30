#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re
import requests
import json
import os
from multiprocessing import Pool
from splinter import Browser

coupon_pattern = re.compile("https://uland.taobao.com/?\w*/?\w*.*\">")
lemon_url_pattern = re.compile("/goods/detail/\d+")

def get_chorme():
    # 驱动存放的地方记得修改
    # todo
    executable_path = {'executable_path': 'python/python_study/taobao/chromedriver'}

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

        yield [{item.get("id"):item.get("couponUrl")} for item in page_data]
        # print lemon_url_pattern.findall(html)

def delete_goods(key):

    # 删除链接
    # todo 记得修改
    url = "http://www.lmyouxuan.com/goods/delete/{0}".format(key)
    r = requests.get(url)
    print r
    print "----->>>>>>>>> {0}".format(key)


def do_actions(range_item=0):

    print "------- task {0} is run ------".format(os.getpid())
    time.sleep(1)
    skips = [0, 626, 625 * 2 + 1, 625 * 3 + 1]
    pages = get_keys_by_page(skip=skips[range_item%4], home=31)

    for item in pages:

        # [{k:v},{k:v}]
        for coupon_item in item:

            # 其实只有一个{k:v}
            for k, v in coupon_item.items():
                print k
                is_available = inspect_available_coupon_url_by_splinter(v)
                print is_available
                if is_available:
                    break
                delete_goods(k)


    print "------ task {0} is over -------".format(os.getpid())


def others():
    import time
    from selenium import webdriver
    # driver 存放的地方
    #todo
    driver = webdriver.Chrome('python_study/taobao/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/xhtml')
    time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()




if __name__ == '__main__':

    # 如果你要创建大量的进程可以使用这个
    p = Pool()

    p.apply_async(do_actions, args=(1,))
    p.apply_async(do_actions, args=(2,))
    p.apply_async(do_actions, args=(3,))
    p.apply_async(do_actions, args=(4,))

    p.close()
    p.join()

