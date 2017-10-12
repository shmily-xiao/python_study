#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CUW&purpose_codes=ADULT"

class SearchTicket(object):
    def get_ticket(self):
        self.request_debug()

        host = "kyfw.12306.cn"
        url = "https://kyfw.12306.cn/otn/leftTicket/query"
        api = "/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CUW&purpose_codes=ADULT"

        params = {"leftTicketDTO.train_date": "2017-10-12",
                  "leftTicketDTO.from_station": "BJP",
                  "leftTicketDTO.to_station": "CUW",
                  "purpose_codes": "ADULT"}

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3637.220 Safari/537.36",
            "Cookie":"JSESSIONID=D2BF2BC7DB247A8A41AF920E53D72CF4; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=149946890.64545.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u91CD%u5E86%u5317%2CCUW; _jc_save_fromDate=2017-10-12; _jc_save_toDate=2017-10-11; _jc_save_wfdc_flag=dc",
            "Host":"kyfw.12306.cn",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",

            }
        kwargs = {"params": params,
                  "verify": False,
                  "headers":headers

                  }

        response = requests.request("GET",url, **kwargs)
        #
        print response.text

        # import http.client
        # conn = http.client.HTTPSConnection(host, 443)
        # conn.request('GET', api)
        # # conn.endheaders()  # <---
        # r = conn.getresponse()
        # print(r.read())


    def request_debug(self):
        import logging

        # These two lines enable debugging at httplib level (requests->urllib3->http.client)
        # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
        # The only thing missing will be the response.body which is not logged.
        try:
            import http.client as http_client
        except ImportError:
            # Python 2
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1

        # You must initialize logging, otherwise you'll not see debug output.
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True


if __name__ == '__main__':
    import PyV8

    ctxt2 = PyV8.JSContext(SearchTicket())  # create another context with the global object
    ctxt2.enter()
    ctxt2.eval("get_ticket()")

