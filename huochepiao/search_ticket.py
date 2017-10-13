#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


# 从北京到成都应该特别关注 G309 车次
class StockInfo(object):

    def function(self):
        pass



# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CUW&purpose_codes=ADULT"

class SearchTicket(object):
    def get_ticket(self, params):
        # self.request_debug()

        url = "https://kyfw.12306.cn/otn/leftTicket/query?"

        sorted_map = {1: "leftTicketDTO.train_date",
                      2: "leftTicketDTO.from_station",
                      3: "leftTicketDTO.to_station",
                      4: "purpose_codes"}

        query = ""
        for item in sorted_map.keys():
            value = sorted_map.get(item)
            query = query + value + "=" + params.get(value) + "&"

        query = query[0:len(query) - 1]

        url = url + query
        print url

        # response = requests.get(url,verify=False)
        json = {u'status': True, u'validateMessagesShowId': u'_validatorMessage', u'messages': [], u'httpstatus': 200,
                u'validateMessages': {}, u'data': {
                u'map': {u'CUW': u'\u91cd\u5e86\u5317', u'BXP': u'\u5317\u4eac\u897f', u'CQW': u'\u91cd\u5e86',
                         u'BPW': u'\u5317\u789a'}, u'flag': u'1', u'result': [
                    u'1kgBUWH%2Bi2I8%2BEvsVqbrzOXj16fzyuXeDnyF372TEDcDMTeMb62uIOUnxzqB18ff%2FMaSdUZxfnh%2B%0AWaHZEmIa16aAtcn4RTnfgYlw9q7RQ3xDxzUQ%2FXZVzfoMULfvs0NJQYZC84N%2Bfi520Jj68ncoZEk4%0AAbckv4bZUTpf8kUHk%2FA7wnTN9ws04amY4ClhnXhtsX4fwi5yI%2BIg9sYCwIKz1Pp6JwhbtysydRYy%0A3kZchvks2mZvL88XGiLICbQ%3D|\u9884\u8ba2|240000K8190J|K819|BXP|CUW|BXP|CUW|07:12|09:17|26:05|Y|DG6WFnOgc6hiK2Xbeqlb3dmBjWR6iR1LeHugaRw%2FuB2izVMg%2FpzeOEswRfs%3D|20171013|3|PB|01|20|0|0||||6|||\u6709||\u6709|\u65e0|||||10401030|1413',
                    u'0cxhRrFO6oIwW%2BJbzd8Zohxi1VeDJff3CEjNZdtwQqaf16Jz0AT1Ne9Uuiy%2FxvVhQwPTPWQ3WSNm%0ALm%2B31lgirhxjBNa6YnzUdXWmSOL3S62u7%2Fs42mvjbG9igt1wBiCqA5dH41r8eepOER%2B%2FNwEO8%2Fex%0Az3dD7TmoydU5jvI2kQkwRE%2BtdTChL%2B35R2toEK%2FpOWLl1xo8qqr33mq5Ohb6p0Ob9j5QP%2ByiBE87%0AaXUpDs4%3D|\u9884\u8ba2|240000G30908|G309|BXP|ICW|BXP|CUW|08:23|20:35|12:12|Y|amm8oFXJSpKNSZB2K7eXMHTujNZhliMcdySqWnduVnfmmmXt|20171013|3|P4|01|18|0|0|||||||||||\u6709|\u65e0|\u65e0||O0M090|OM9',
                    u'UmfOL3EzuIInLDzF9UjXuAJBDGmr5%2FCEAEqnLDhm%2FxFHSTUjx95NR%2F9hDuRy4SMZjorWoLWGFIon%0A5HBe6riNtSuTMleRiFNTVp%2F7eNKEIDJczfATDPOkj%2BcSbIMYaWLAoQ8i%2BdqZShOlUvCNJp0cB7%2Fy%0AnVInbHkwEpGy5ddrb8BfStH9S4oVvHoN7AwUQu43SRYo17cs2Ra1C5mGDkAc7sD60sSwrQnt3Jdj%0Act8s6L2IZcyViA3ISA%3D%3D|\u9884\u8ba2|240000K5890X|K589|BXP|CQW|BXP|BPW|10:30|14:40|28:10|Y|2eMOC2QLeXPZW77kvgNkjzUn0BNJpO27eakGKkiJBN%2B5Sud9NnIxU963cqY%3D|20171013|3|PB|01|22|0|0||||18|||\u6709||\u6709|\u6709|||||10403010|1431',
                    u'%2FKxiBeS%2FPUYNCVAdu3VgFOL%2FM2oqMWx8KDDvfmlKr3lMsPNAye0oh8Lhyz1abYT0cQ8KnygBDzwB%0AYVS4HbR0vFl7XALCwXP095R4VBMDVsISFBZgnf6j5xnZIBsq9MCVyzY9dCOqmTSrcfO9j34yYokx%0A5CkLugwvXZUS7MiUwhsi9FOmjLjvbq%2FZyATmkz7ymNJv5pxRM1yW6njKD5AIHEuQ2iNSgnwkGxU%2B%0ARCRjS9in6CTRppVa3gnjgao%3D|\u9884\u8ba2|2400000Z490E|Z49|BXP|CDW|BXP|CUW|11:28|05:32|18:04|Y|nDV7HvvMwoIK38fvo4%2FejxTK9l%2Fo5Yu4YItSBT92KozFwHLdO9K6KyDrems%3D|20171013|3|P4|01|08|0|0||||3|||\u6709||\u65e0|\u65e0|||||10401030|1413',
                    u'7tDh4evKSl2o%2B4kSQ4et6FIS1zsYodFXu9jiB23%2FOAEllOECdxC4pVj2UbVp3qhz4Z8444go9Pjc%0AiOIDsWf3yEdDO%2BSmtKM0N99AhL0kGI%2BHAm4XyChxopEiIyig%2FSNMTBQ4TkDztXRRNxF0IgdLUz%2B3%0AnOrlR20hYbWwawvSdiDs72xHk%2Fg3%2BN7aO7TYRstCF3p%2FoT6ErtrCNUNTyg9pKQBIVAyuchqGTFbv%0A%2FXyV87OQzZ%2BJXanvKQ%3D%3D|\u9884\u8ba2|24000000T90U|T9|BXP|CUW|BXP|CUW|15:05|16:19|25:14|Y|qI%2BVhK2b4GdmiwhujhYWOth2cuJ9Gg6sLlOFdhLXmaSlogVFLXk0UvvPk2I%3D|20171013|3|P4|01|14|0|0||||1|||\u6709||1|\u65e0|||||10401030|1413',
                    u'1O6KFymOthN%2BMmkGxaXmdiFcW5ASoMHYUGpxiSCcqPxOz6bBkgueMyQYUh9Tsn3DVFR3Lc4ci2rn%0A2LyT4CCoT7LyKAB1icSFg4GT8p3uqK93ZJsOQ%2Bnp%2FQi1Sdej14EC9UqDPc1oQasG5fKuprHSkmLW%0Accr990FETNwuj3STHuVyTP7cauBU1bIBKP4ZF7dQCP2d%2Fz4yMk72jTofFF%2FfrL7iKBvG2BG5nM8y%0ArAV2TVM1sHodp1sVwA%3D%3D|\u9884\u8ba2|24000000Z30I|Z3|BXP|CUW|BXP|CUW|17:48|11:56|18:08|Y|1959222raWx5k4ziPuWrEWy7UuNuhSbypS%2BPTeHplwOn5q7mLWEU5FTlC5g%3D|20171013|3|P3|01|07|0|0||||\u65e0|||\u6709||\u65e0|\u6709|||||10401030|1413',
                    u'WISA%2FyRc1SI15PshltIlkz4IR680YpWSep7HtUT6pEJ8Lep6Nn2DG6CdwqMFJTIPXEMTm%2Fy3eD5e%0AnLfYl%2FSkwoGg%2FtBb6WfLYACp7wdMilqoIYkgp6xNIoYlGw353cvOjIQLHYF%2FmX9IcIBKov721jNG%0AJCB1GrVT8CVbfCI4QBTroI1EuVTrLtGFRZLQWrVSSUDHJzGkpIV3cydt8dhR2BwjuBLoJpX%2FD4GB%0ALGoN3UIIzWnHbVJ4PbyHgT4%3D|\u9884\u8ba2|2400000Z9502|Z95|BXP|CUW|BXP|CUW|18:06|16:47|22:41|Y|AHjQM%2FlOfneMK3ZbUY62pJb2NBNMUuko8LRrWARfRFiL5gwBHdbuvjzkwEk%3D|20171013|3|P4|01|11|0|0||||1|||\u6709||\u65e0|\u6709|||||10401030|1413',
                    u'tY%2FOKrvYPQLA%2B4mytupT5vhop60AvzTKCoBTOnkjL%2BgDbIkx8tvby7Ybnil0r5Tp8L4MLnb8UZAK%0Aht3pUGFAr%2FheeFOSn6zn9Ex71AsehWXO5CJIwvSk%2FlzLzEYvO063LDhXBJRmpjlm05DiSH3AVN5X%0Ac%2FFkCzPYnfMDVyiwcEGAYo6XQX8hny1rwpTxkTHygoUdl7iq8O20W%2FvG5G2QJo8fFxgtkubTHFxG%0AUTEaZNXOw8sH%2BfeT8Q%3D%3D|\u9884\u8ba2|240000K5072A|K507|BXP|GIW|BXP|CQW|21:23|02:17|28:54|Y|WoM60rm2DR18qaw0BnAyHdWnnrAeLdyE4xAGasQie6PYX%2Bv0yen8EXCbbyk%3D|20171013|3|PB|01|25|0|0||||\u65e0|||\u6709||\u65e0|\u6709|||||10401030|1413']}}
        # print response.json()

        results = json.get("data").get("result")
        # for result in results:
        #     store_list = result.split("|")

        data = self.data_converter(results,  json.get("data").get("map"))
        for item in data:
            print item


    def data_converter(self, result, data_map):

        cp = []
        if not result:
            return cp
        for co in xrange(len(result)):
            ct = StockInfo()
            cn = result[co].split("|")
            ct.secretStr = cn[0]
            ct.buttonTextInfo = cn[1]

            cr = StockInfo()

            cr.train_no = cn[2]  # 火车编号
            cr.station_train_code = cn[3]  # 火车站的火车编号 ?
            cr.start_station_telecode = cn[4]   # 始发站火车站的电话代码 ? 还是远程代码 ?
            cr.end_station_telecode = cn[5]
            cr.from_station_telecode = cn[6]
            cr.to_station_telecode = cn[7]
            cr.start_time = cn[8]    # 开车时间
            cr.arrive_time = cn[9]    # 到达时间
            cr.lishi = cn[10]    # 历时 就是要经过多少时间
            cr.canWebBuy = cn[11]    # 我们能不能买 ?
            cr.yp_info = cn[12]      # # 余票数据？
            cr.start_train_date = cn[13]
            cr.train_seat_feature = cn[14]
            cr.location_code = cn[15]
            cr.from_station_no = cn[16]   # 乘客上车的站的编号(估计是在这个城市的编号 , 因为要考虑到一个城市多个站的情况) ?
            cr.to_station_no = cn[17]   # 乘客下车的站的编号
            cr.is_support_card = cn[18]    # 是否支持刷卡 ?
            cr.controlled_train_flag = cn[19]
            cr.gg_num = cn[20] if cn[20] else "--"
            cr.gr_num = cn[21] if cn[21] else "--"
            cr.qt_num = cn[22] if cn[22] else "--"
            cr.rw_num = cn[23] if cn[23] else "--"
            cr.rz_num = cn[24] if cn[24] else "--"
            cr.tz_num = cn[25] if cn[25] else "--"
            cr.wz_num = cn[26] if cn[26] else "--"
            cr.yb_num = cn[27] if cn[27] else "--"
            cr.yw_num = cn[28] if cn[28] else "--"
            cr.yz_num = cn[29] if cn[29] else "--"
            cr.ze_num = cn[30] if cn[30] else "--"
            cr.zy_num = cn[31] if cn[31] else "--"
            cr.swz_num = cn[32] if cn[32] else "--"
            cr.srrb_num = cn[33] if cn[33] else "--"
            cr.yp_ex = cn[34]
            cr.seat_types = cn[35]   # 座位类型
            cr.from_station_name = data_map[cn[6]]  # 始发站火车站名
            cr.to_station_name = data_map[cn[7]]   # 终点站火车站名

            ct.queryLeftNewDTO = cr.__dict__
            co += 1

            cp.append(ct.__dict__)

        return cp

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
    # import PyV8

    # ctxt2 = PyV8.JSContext(SearchTicket())  # create another context with the global object
    # ctxt2.enter()
    # ctxt2.eval("get_ticket()")
    t = SearchTicket()

    params = {"leftTicketDTO.train_date": "2017-10-13",
              "leftTicketDTO.from_station": "BJP",
              "leftTicketDTO.to_station": "CUW",
              "purpose_codes": "ADULT"}

    t.get_ticket(params)
