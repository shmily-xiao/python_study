#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re
import requests
import json
import os
from multiprocessing import Pool
from splinter import Browser

def get_chorme():
    # 驱动存放的地方记得修改
    # todo
    executable_path = {'executable_path': '/Users/zaijunwang/workspace/python/python_study/taobao/chromedriver'}

    browser = Browser('chrome', **executable_path)
    return browser


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

    # browser.find_by_id("a2107.1.0.0").click()
    # browser.get_iframe("taobaoLoginIfr")

    # print  browser
    #
    # browser.driver.switch_to.frame(browser.driver.find_elements_by_tag_name("iframe")[0])
    #
    # print browser

    # with browser.driver.find_elements_by_tag_name("iframe")[0] as iframe:
    # with browser.get_iframe("iframe") as iframe:
    with browser.get_iframe("taobaoLoginIfr") as iframe:
        print iframe
        iframe.do_stuff()
        # # browser.evaluate_script('document.getElementById("J_LoginBox").style="login-box no-longlogin module-static"')
        # browser.evaluate_scri('(function(x){x&&(x.className+=" loading")})(document.getElementById("J_LoginBox"))')
        # # browser.evaluate_script('document.getElementById("batch_quto").contentEditable = true')
        # # browser.find_by_id('batch_quto').fill("120")
        # time.sleep(10)
        # iframe.fill("TPL_username", "w淘金者1234")
        # iframe.fill("TPL_password", "w19920924")
        # button = iframe.find_by_id('J_SubmitStatic')
        # button.click()

        # iframe.find_by_name('email').fill('yourName')
        # iframe.find_by_name('password').fill('yourPassWord')
        # iframe.find_by_id('dologin').click()
        # iframe.find_by_text('继续登录').click()

    # # move into the iframe
    # iframe = browser.get_iframe('taobaoLoginIfr')
    # # browser.switch_to_frame(iframe)
    #
    # # interact with your element inside the iframe
    # iframe.find_by_id('TPL_username').send_keys("w淘金者1234")
    # iframe.find_by_id('TPL_password').send_keys("w19920924")
    #
    # # move out of iframe
    # iframe.switch_to_default_content()
    #
    # # interact with normal elements outside the iframe
    # find_button = iframe.find_by_id('J_SubmitStatic')
    # find_button.click()



        # form={
    #     "TPL_username":"w淘金者1234",
    #     "TPL_password":"w19920924"
    # }
    #
    # browser.fill_form(form,form_id="J_Form")


    # cookie = 'JSESSIONID' + '=' + b.cookies['JSESSIONID']  # cookie的构成

    # try:
    #     text = div.html
    #     text = text.encode("utf-8")
    #     if not text:
    #         return None
    #     if "领券立减" not in text:
    #         return None
    #     # result = coupon_pattern.findall(text)[0]
    #     # return result[:-2]
    # except Exception as e:
    #     print e
    #     return None
    # finally:
    #     # close the window of brower
    browser.quit()

if __name__ == '__main__':

    url = "https://ad.alimama.com/index.htm"
    get_coupon_url_by_splinter(url)
