#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. 输入目的地和出发地和时间
2. 自动搜索该线路下的所有的座位，只显示有座位的数据


解决的问题：我可以知道哪一段是没有座位的，我可以想办法上车再买票
"""

import requests
import time

from location import create_location_name_map, get_location_code


# 从北京到成都应该特别关注 G309 车次
class StockInfo(object):
    def function(self):
        pass


SEAT_TYPE_MAP = {
    "tz": "特等座",
    "swz": "商务座",
    "zy": "一等座",
    "ze": "二等座",
    "gr": "高级软卧",
    "rw": "软卧",
    "yw": "硬卧",
    "srrb": "动卧",
    "yyrw": "高级动卧",
    "rz": "软座",
    "yz": "硬座",
    "wz": "无座",
    "qt": "其他"
}


# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CUW&purpose_codes=ADULT"


class SearchTicket(object):
    def do(self):
        date_time = "2017-10-19"

        params = {"leftTicketDTO.train_date": date_time,
                  "leftTicketDTO.from_station": "BJP",
                  "leftTicketDTO.to_station": "CUW",
                  "purpose_codes": "ADULT"}

        ticket_list = self.get_ticket(params)

        result = []
        for ticket in ticket_list:
            result.append(self.get_all_location_stock(ticket, date_time))

        return result

    def get_all_location_stock(self, ticket, date_time):
        """
        针对跨天的列车区间查询日期说明：
            有的列车是需要跨天的，但是在分段查询的时候没有对查询的时间进行加一天操作，原因是因为，
            你可能只会关心当天的那一段的区间是否有座位。
            比如： 
               今天出发的车在明天凌晨的时候才到达某一个站点B，但是对于这个B站点的人来说只有在今天去买明天的那个车次的票，才会
               和你在同一辆车上。如果B站点的人要买今天的那个车次的票，其实这辆车是昨天就出发了的。
               所以你在查询某个车次某个区间的车票的时候只用去关心你输入的日期的余票就可以了。
               所以你在查询车票的时候应该估算好到达B站点的时间，决定查询今天的车票还是后一天（明天）的车票。
               
               我的宗旨是让你能够上车，到时候补票回家都可以。回家自然才是最重要的。
               
        :param ticket: 
        :return: 
        """
        queryLeftNewDTO = ticket.get("queryLeftNewDTO")
        train_no = queryLeftNewDTO.get("train_no")

        params = {"train_no": train_no,
                  "from_station_telecode": queryLeftNewDTO.get("from_station_telecode"),
                  "to_station_telecode": queryLeftNewDTO.get("to_station_telecode"),
                  "depart_date": date_time}

        locations = self.get_locations(params)

        result_location = []

        for index, location in enumerate(locations):
            if not location.get("isEnabled"):
                continue
            if index == len(locations) - 1:
                continue
            from_location = location.get("station_name")

            to_location = locations[index + 1].get("station_name")

            params = {"leftTicketDTO.train_date": date_time,
                      "leftTicketDTO.from_station": get_location_code(from_location),
                      "leftTicketDTO.to_station": get_location_code(to_location),
                      "purpose_codes": "ADULT"}

            ticket_list = self.get_ticket(params)

            for ticket in ticket_list:
                if ticket.get("queryLeftNewDTO").get("train_no") == train_no:
                    temp = {"from_station": from_location, "to_station": to_location,
                            "left_ticket": self.count_left_ticket(ticket)}
                    result_location.append(temp)
                    break

        data = {"train_no": train_no, "real_name": ticket.get("queryLeftNewDTO").get("station_train_code"), "data": result_location}

        return data

    def count_left_ticket(self, ticket):

        """
        {'secretStr': u'1kgBUWH%2Bi2I8%2BEvsVqbrzOXj16fzyuXeDnyF372TEDcDMTeMb62uIOUnxzqB18ff%2FMaSdUZxfnh%2B%0AWaHZEmIa16aAtcn4RTnfgYlw9q7RQ3xDxzUQ%2FXZVzfoMULfvs0NJQYZC84N%2Bfi520Jj68ncoZEk4%0AAbckv4bZUTpf8kUHk%2FA7wnTN9ws04amY4ClhnXhtsX4fwi5yI%2BIg9sYCwIKz1Pp6JwhbtysydRYy%0A3kZchvks2mZvL88XGiLICbQ%3D', 
        'queryLeftNewDTO': {'start_station_telecode': u'BXP', 'tz_num': '--', 'yz_num': u'\u65e0', 'controlled_train_flag': u'0', 'train_no': u'240000K8190J', 
        'yp_info': {'start_station_telecode': u'BXP', 'tz_num': '--', 'yz_num': u'\u65e0', 'controlled_train_flag': u'0', 
        'train_no': u'240000K8190J', 'yp_info': u'DG6WFnOgc6hiK2Xbeqlb3dmBjWR6iR1LeHugaRw%2FuB2izVMg%2FpzeOEswRfs%3D', 
        'yb_num': '--', 'end_station_telecode': u'CUW', 'rw_num': u'6', 'swz_num': '--', 'ze_num': '--', 'canWebBuy': u'Y', 
        'from_station_telecode': u'BXP', 'lishi': u'26:05', 'location_code': u'PB', 'rz_num': '--', 'from_station_no': u'01', 
        'is_support_card': u'0', 'start_train_date': u'20171013', 'seat_types': u'1413', 'gr_num': '--', 'start_time': u'07:12', 
        'wz_num': u'\u6709', 'to_station_telecode': u'CUW', 'train_seat_feature': u'3', 'yp_ex': u'10401030', 'zy_num': '--', 
        'to_station_no': u'20', 'yw_num': u'\u6709', 'qt_num': '--', 'from_station_name': u'\u5317\u4eac\u897f', 
        'srrb_num': '--', 'arrive_time': u'09:17', 'station_train_code': u'K819', 'gg_num': '--', 
        'to_station_name': u'\u91cd\u5e86\u5317'}, 'buttonTextInfo': u'\u9884\u8ba2'}
        :param ticket: 
        :return: 
        """
        stockInfo = StockInfo()

        for item in ticket.get("queryLeftNewDTO").keys():
            if "num" in item:
                value = ticket.get("queryLeftNewDTO").get(item)
                # 无
                if value == "--" or value == "\u65e0":
                    continue
                # 有   \u6709
                stockInfo.hasSeat = True
                stockInfo.__setattr__(SEAT_TYPE_MAP.get(item.split("_").pop(0)), value)

        return stockInfo.__dict__

    def __create_query_url(self, sorted_map, params):
        query = ""
        for item in sorted_map.keys():
            value = sorted_map.get(item)
            query = query + value + "=" + params.get(value) + "&"

        query = query[0:len(query) - 1]
        return query

    def get_locations(self, params):

        # params = {"train_no": "240000K8170P",
        #           "from_station_telecode": "BXP",
        #           "to_station_telecode": "CDW",
        #           "depart_date": "2017-10-17"}

        host = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo?"

        sorted_map = {1: "train_no",
                      2: "from_station_telecode",
                      3: "to_station_telecode",
                      4: "depart_date"}

        query = self.__create_query_url(sorted_map, params)

        url = host + query

        time.sleep(1)
        response = requests.get(url, verify=False).json()

        # return response
        # response = {"validateMessagesShowId": "_validatorMessage", "status": True, "httpstatus": 200, "data": {"data": [
        #     {"start_station_name": "北京西", "arrive_time": "----", "station_train_code": "K817", "station_name": "北京西",
        #      "train_class_name": "快速", "service_type": "1", "start_time": "08:00", "stopover_time": "----",
        #      "end_station_name": "成都", "station_no": "01", "isEnabled": True},
        #     {"arrive_time": "09:30", "station_name": "保定", "start_time": "09:33", "stopover_time": "3分钟",
        #      "station_no": "02", "isEnabled": True},
        #     {"arrive_time": "10:10", "station_name": "定州", "start_time": "10:13", "stopover_time": "3分钟",
        #      "station_no": "03", "isEnabled": True},
        #     {"arrive_time": "11:05", "station_name": "石家庄", "start_time": "11:22", "stopover_time": "17分钟",
        #      "station_no": "04", "isEnabled": True},
        #     {"arrive_time": "12:25", "station_name": "邢台", "start_time": "12:27", "stopover_time": "2分钟",
        #      "station_no": "05", "isEnabled": True},
        #     {"arrive_time": "13:25", "station_name": "邯郸", "start_time": "13:29", "stopover_time": "4分钟",
        #      "station_no": "06", "isEnabled": True},
        #     {"arrive_time": "14:23", "station_name": "安阳", "start_time": "14:32", "stopover_time": "9分钟",
        #      "station_no": "07", "isEnabled": True},
        #     {"arrive_time": "15:01", "station_name": "鹤壁", "start_time": "15:33", "stopover_time": "32分钟",
        #      "station_no": "08", "isEnabled": True},
        #     {"arrive_time": "16:12", "station_name": "新乡", "start_time": "16:15", "stopover_time": "3分钟",
        #      "station_no": "09", "isEnabled": True},
        #     {"arrive_time": "17:16", "station_name": "郑州", "start_time": "17:32", "stopover_time": "16分钟",
        #      "station_no": "10", "isEnabled": True},
        #     {"arrive_time": "19:00", "station_name": "洛阳东", "start_time": "19:04", "stopover_time": "4分钟",
        #      "station_no": "11", "isEnabled": True},
        #     {"arrive_time": "19:12", "station_name": "洛阳", "start_time": "19:15", "stopover_time": "3分钟",
        #      "station_no": "12", "isEnabled": True},
        #     {"arrive_time": "21:01", "station_name": "三门峡", "start_time": "21:04", "stopover_time": "3分钟",
        #      "station_no": "13", "isEnabled": True},
        #     {"arrive_time": "03:52", "station_name": "安康", "start_time": "04:03", "stopover_time": "11分钟",
        #      "station_no": "14", "isEnabled": True},
        #     {"arrive_time": "06:47", "station_name": "宣汉", "start_time": "06:49", "stopover_time": "2分钟",
        #      "station_no": "15", "isEnabled": True},
        #     {"arrive_time": "07:36", "station_name": "达州", "start_time": "07:47", "stopover_time": "11分钟",
        #      "station_no": "16", "isEnabled": True},
        #     {"arrive_time": "08:51", "station_name": "营山", "start_time": "08:54", "stopover_time": "3分钟",
        #      "station_no": "17", "isEnabled": True},
        #     {"arrive_time": "09:07", "station_name": "蓬安", "start_time": "09:10", "stopover_time": "3分钟",
        #      "station_no": "18", "isEnabled": True},
        #     {"arrive_time": "09:37", "station_name": "南充", "start_time": "09:41", "stopover_time": "4分钟",
        #      "station_no": "19", "isEnabled": True},
        #     {"arrive_time": "10:22", "station_name": "遂宁", "start_time": "10:28", "stopover_time": "6分钟",
        #      "station_no": "20", "isEnabled": True},
        #     {"arrive_time": "10:49", "station_name": "大英东", "start_time": "11:25", "stopover_time": "36分钟",
        #      "station_no": "21", "isEnabled": True},
        #     {"arrive_time": "12:41", "station_name": "成都", "start_time": "12:41", "stopover_time": "----",
        #      "station_no": "22", "isEnabled": True}]}, "messages": [], "validateMessages": {}}

        if not response.get("status"):
            return []

        return response.get("data").get("data")

    def get_ticket(self, params):
        # self.request_debug()

        url = "https://kyfw.12306.cn/otn/leftTicket/query?"

        sorted_map = {1: "leftTicketDTO.train_date",
                      2: "leftTicketDTO.from_station",
                      3: "leftTicketDTO.to_station",
                      4: "purpose_codes"}

        query = self.__create_query_url(sorted_map, params)
        url = url + query
        print url

        time.sleep(1)
        response = requests.get(url, verify=False).json()



        # response = {u'status': True, u'validateMessagesShowId': u'_validatorMessage', u'messages': [],
        #             u'httpstatus': 200,
        #             u'validateMessages': {}, u'data': {
        #         u'map': {u'CUW': u'\u91cd\u5e86\u5317', u'BXP': u'\u5317\u4eac\u897f', u'CQW': u'\u91cd\u5e86',
        #                  u'BPW': u'\u5317\u789a'},
        #         u'flag': u'1',
        #         u'result': [
        #             u'1kgBUWH%2Bi2I8%2BEvsVqbrzOXj16fzyuXeDnyF372TEDcDMTeMb62uIOUnxzqB18ff%2FMaSdUZxfnh%2B%0AWaHZEmIa16aAtcn4RTnfgYlw9q7RQ3xDxzUQ%2FXZVzfoMULfvs0NJQYZC84N%2Bfi520Jj68ncoZEk4%0AAbckv4bZUTpf8kUHk%2FA7wnTN9ws04amY4ClhnXhtsX4fwi5yI%2BIg9sYCwIKz1Pp6JwhbtysydRYy%0A3kZchvks2mZvL88XGiLICbQ%3D|\u9884\u8ba2|240000K8190J|K819|BXP|CUW|BXP|CUW|07:12|09:17|26:05|Y|DG6WFnOgc6hiK2Xbeqlb3dmBjWR6iR1LeHugaRw%2FuB2izVMg%2FpzeOEswRfs%3D|20171013|3|PB|01|20|0|0||||6|||\u6709||\u6709|\u65e0|||||10401030|1413',
        #             u'0cxhRrFO6oIwW%2BJbzd8Zohxi1VeDJff3CEjNZdtwQqaf16Jz0AT1Ne9Uuiy%2FxvVhQwPTPWQ3WSNm%0ALm%2B31lgirhxjBNa6YnzUdXWmSOL3S62u7%2Fs42mvjbG9igt1wBiCqA5dH41r8eepOER%2B%2FNwEO8%2Fex%0Az3dD7TmoydU5jvI2kQkwRE%2BtdTChL%2B35R2toEK%2FpOWLl1xo8qqr33mq5Ohb6p0Ob9j5QP%2ByiBE87%0AaXUpDs4%3D|\u9884\u8ba2|240000G30908|G309|BXP|ICW|BXP|CUW|08:23|20:35|12:12|Y|amm8oFXJSpKNSZB2K7eXMHTujNZhliMcdySqWnduVnfmmmXt|20171013|3|P4|01|18|0|0|||||||||||\u6709|\u65e0|\u65e0||O0M090|OM9',
        #             u'UmfOL3EzuIInLDzF9UjXuAJBDGmr5%2FCEAEqnLDhm%2FxFHSTUjx95NR%2F9hDuRy4SMZjorWoLWGFIon%0A5HBe6riNtSuTMleRiFNTVp%2F7eNKEIDJczfATDPOkj%2BcSbIMYaWLAoQ8i%2BdqZShOlUvCNJp0cB7%2Fy%0AnVInbHkwEpGy5ddrb8BfStH9S4oVvHoN7AwUQu43SRYo17cs2Ra1C5mGDkAc7sD60sSwrQnt3Jdj%0Act8s6L2IZcyViA3ISA%3D%3D|\u9884\u8ba2|240000K5890X|K589|BXP|CQW|BXP|BPW|10:30|14:40|28:10|Y|2eMOC2QLeXPZW77kvgNkjzUn0BNJpO27eakGKkiJBN%2B5Sud9NnIxU963cqY%3D|20171013|3|PB|01|22|0|0||||18|||\u6709||\u6709|\u6709|||||10403010|1431',
        #             u'%2FKxiBeS%2FPUYNCVAdu3VgFOL%2FM2oqMWx8KDDvfmlKr3lMsPNAye0oh8Lhyz1abYT0cQ8KnygBDzwB%0AYVS4HbR0vFl7XALCwXP095R4VBMDVsISFBZgnf6j5xnZIBsq9MCVyzY9dCOqmTSrcfO9j34yYokx%0A5CkLugwvXZUS7MiUwhsi9FOmjLjvbq%2FZyATmkz7ymNJv5pxRM1yW6njKD5AIHEuQ2iNSgnwkGxU%2B%0ARCRjS9in6CTRppVa3gnjgao%3D|\u9884\u8ba2|2400000Z490E|Z49|BXP|CDW|BXP|CUW|11:28|05:32|18:04|Y|nDV7HvvMwoIK38fvo4%2FejxTK9l%2Fo5Yu4YItSBT92KozFwHLdO9K6KyDrems%3D|20171013|3|P4|01|08|0|0||||3|||\u6709||\u65e0|\u65e0|||||10401030|1413',
        #             u'7tDh4evKSl2o%2B4kSQ4et6FIS1zsYodFXu9jiB23%2FOAEllOECdxC4pVj2UbVp3qhz4Z8444go9Pjc%0AiOIDsWf3yEdDO%2BSmtKM0N99AhL0kGI%2BHAm4XyChxopEiIyig%2FSNMTBQ4TkDztXRRNxF0IgdLUz%2B3%0AnOrlR20hYbWwawvSdiDs72xHk%2Fg3%2BN7aO7TYRstCF3p%2FoT6ErtrCNUNTyg9pKQBIVAyuchqGTFbv%0A%2FXyV87OQzZ%2BJXanvKQ%3D%3D|\u9884\u8ba2|24000000T90U|T9|BXP|CUW|BXP|CUW|15:05|16:19|25:14|Y|qI%2BVhK2b4GdmiwhujhYWOth2cuJ9Gg6sLlOFdhLXmaSlogVFLXk0UvvPk2I%3D|20171013|3|P4|01|14|0|0||||1|||\u6709||1|\u65e0|||||10401030|1413',
        #             u'1O6KFymOthN%2BMmkGxaXmdiFcW5ASoMHYUGpxiSCcqPxOz6bBkgueMyQYUh9Tsn3DVFR3Lc4ci2rn%0A2LyT4CCoT7LyKAB1icSFg4GT8p3uqK93ZJsOQ%2Bnp%2FQi1Sdej14EC9UqDPc1oQasG5fKuprHSkmLW%0Accr990FETNwuj3STHuVyTP7cauBU1bIBKP4ZF7dQCP2d%2Fz4yMk72jTofFF%2FfrL7iKBvG2BG5nM8y%0ArAV2TVM1sHodp1sVwA%3D%3D|\u9884\u8ba2|24000000Z30I|Z3|BXP|CUW|BXP|CUW|17:48|11:56|18:08|Y|1959222raWx5k4ziPuWrEWy7UuNuhSbypS%2BPTeHplwOn5q7mLWEU5FTlC5g%3D|20171013|3|P3|01|07|0|0||||\u65e0|||\u6709||\u65e0|\u6709|||||10401030|1413',
        #             u'WISA%2FyRc1SI15PshltIlkz4IR680YpWSep7HtUT6pEJ8Lep6Nn2DG6CdwqMFJTIPXEMTm%2Fy3eD5e%0AnLfYl%2FSkwoGg%2FtBb6WfLYACp7wdMilqoIYkgp6xNIoYlGw353cvOjIQLHYF%2FmX9IcIBKov721jNG%0AJCB1GrVT8CVbfCI4QBTroI1EuVTrLtGFRZLQWrVSSUDHJzGkpIV3cydt8dhR2BwjuBLoJpX%2FD4GB%0ALGoN3UIIzWnHbVJ4PbyHgT4%3D|\u9884\u8ba2|2400000Z9502|Z95|BXP|CUW|BXP|CUW|18:06|16:47|22:41|Y|AHjQM%2FlOfneMK3ZbUY62pJb2NBNMUuko8LRrWARfRFiL5gwBHdbuvjzkwEk%3D|20171013|3|P4|01|11|0|0||||1|||\u6709||\u65e0|\u6709|||||10401030|1413',
        #             u'tY%2FOKrvYPQLA%2B4mytupT5vhop60AvzTKCoBTOnkjL%2BgDbIkx8tvby7Ybnil0r5Tp8L4MLnb8UZAK%0Aht3pUGFAr%2FheeFOSn6zn9Ex71AsehWXO5CJIwvSk%2FlzLzEYvO063LDhXBJRmpjlm05DiSH3AVN5X%0Ac%2FFkCzPYnfMDVyiwcEGAYo6XQX8hny1rwpTxkTHygoUdl7iq8O20W%2FvG5G2QJo8fFxgtkubTHFxG%0AUTEaZNXOw8sH%2BfeT8Q%3D%3D|\u9884\u8ba2|240000K5072A|K507|BXP|GIW|BXP|CQW|21:23|02:17|28:54|Y|WoM60rm2DR18qaw0BnAyHdWnnrAeLdyE4xAGasQie6PYX%2Bv0yen8EXCbbyk%3D|20171013|3|PB|01|25|0|0||||\u65e0|||\u6709||\u65e0|\u6709|||||10401030|1413']}}
        # print response.json()

        # results = json.get("data").get("result")
        # return json

        if not response.get("status") or response.get("httpstatus") != 200:
            return "no data: {0}".format(response)

        ticket_list = self.data_converter(response.get("data").get("result"), response.get("data").get("map"))
        return ticket_list

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
            cr.start_station_telecode = cn[4]  # 始发站火车站的电话代码 ? 还是远程代码 ?
            cr.end_station_telecode = cn[5]
            cr.from_station_telecode = cn[6]  # 开始车站编号
            cr.to_station_telecode = cn[7]  # 到达站编号
            cr.start_time = cn[8]  # 开车时间
            cr.arrive_time = cn[9]  # 到达时间
            cr.lishi = cn[10]  # 历时 就是要经过多少时间
            cr.canWebBuy = cn[11]  # 我们能不能买 ?
            cr.yp_info = cn[12]  # # 余票数据？
            cr.start_train_date = cn[13]
            cr.train_seat_feature = cn[14]
            cr.location_code = cn[15]
            cr.from_station_no = cn[16]  # 乘客上车的站的编号(估计是在这个城市的编号 , 因为要考虑到一个城市多个站的情况) ?
            cr.to_station_no = cn[17]  # 乘客下车的站的编号
            cr.is_support_card = cn[18]  # 是否支持刷卡 ?
            cr.controlled_train_flag = cn[19]
            cr.gg_num = cn[20] if cn[20] else "--"  #
            cr.gr_num = cn[21] if cn[21] else "--"  # 高级软卧
            cr.qt_num = cn[22] if cn[22] else "--"  # 其他
            cr.rw_num = cn[23] if cn[23] else "--"  # 软卧
            cr.rz_num = cn[24] if cn[24] else "--"  # 软座
            cr.tz_num = cn[25] if cn[25] else "--"  # 特等座
            cr.wz_num = cn[26] if cn[26] else "--"  # 无座
            cr.yb_num = cn[27] if cn[27] else "--"  #
            cr.yw_num = cn[28] if cn[28] else "--"  # 硬卧
            cr.yz_num = cn[29] if cn[29] else "--"  # 硬座
            cr.ze_num = cn[30] if cn[30] else "--"  # 二等
            cr.zy_num = cn[31] if cn[31] else "--"  # 一等
            cr.swz_num = cn[32] if cn[32] else "--"  # 商务座
            cr.srrb_num = cn[33] if cn[33] else "--"  # 动卧
            cr.yp_ex = cn[34]
            cr.seat_types = cn[35]  # 座位类型
            cr.from_station_name = data_map[cn[6]]  # 始发站火车站名
            cr.to_station_name = data_map[cn[7]]  # 终点站火车站名

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

    # params = {"leftTicketDTO.train_date": "2017-10-13",
    #           "leftTicketDTO.from_station": "BJP",
    #           "leftTicketDTO.to_station": "CUW",
    #           "purpose_codes": "ADULT"}
    #
    # t.get_ticket(params)

    data = t.do()
    import json
    print json.dumps(data)
