#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import PyV8
#
#
# class Test():
#     def js(self):
#         ctxt = PyV8.JSContext()
#         ctxt.enter()
#
#         func = ctxt.eval("(function(){return '###'})")
#         print func()
#         print 'sdad'
#
#
# if __name__ == '__main__':
#     crawler = Test()
#
#     crawler.js()

# b2(cr.data.result, cr.data.map)

# function b2(cq, cs) {
# 		var cp = [];
# 		for (var co = 0; co < cq.length; co++) {
# 			var ct = [];
# 			var cn = cq[co].split("|");
# 			ct.secretStr = cn[0];
# 			ct.buttonTextInfo = cn[1];
# 			var cr = [];
# 			cr.train_no = cn[2];
# 			cr.station_train_code = cn[3];
# 			cr.start_station_telecode = cn[4];
# 			cr.end_station_telecode = cn[5];
# 			cr.from_station_telecode = cn[6];
# 			cr.to_station_telecode = cn[7];
# 			cr.start_time = cn[8];
# 			cr.arrive_time = cn[9];
# 			cr.lishi = cn[10];
# 			cr.canWebBuy = cn[11];
# 			cr.yp_info = cn[12];
# 			cr.start_train_date = cn[13];
# 			cr.train_seat_feature = cn[14];
# 			cr.location_code = cn[15];
# 			cr.from_station_no = cn[16];
# 			cr.to_station_no = cn[17];
# 			cr.is_support_card = cn[18];
# 			cr.controlled_train_flag = cn[19];
# 			cr.gg_num = cn[20] ? cn[20] : "--";
# 			cr.gr_num = cn[21] ? cn[21] : "--";
# 			cr.qt_num = cn[22] ? cn[22] : "--";
# 			cr.rw_num = cn[23] ? cn[23] : "--";
# 			cr.rz_num = cn[24] ? cn[24] : "--";
# 			cr.tz_num = cn[25] ? cn[25] : "--";
# 			cr.wz_num = cn[26] ? cn[26] : "--";
# 			cr.yb_num = cn[27] ? cn[27] : "--";
# 			cr.yw_num = cn[28] ? cn[28] : "--";
# 			cr.yz_num = cn[29] ? cn[29] : "--";
# 			cr.ze_num = cn[30] ? cn[30] : "--";
# 			cr.zy_num = cn[31] ? cn[31] : "--";
# 			cr.swz_num = cn[32] ? cn[32] : "--";
# 			cr.srrb_num = cn[33] ? cn[33] : "--";
# 			cr.yp_ex = cn[34];
# 			cr.seat_types = cn[35];
# 			cr.from_station_name = cs[cn[6]];
# 			cr.to_station_name = cs[cn[7]];
# 			ct.queryLeftNewDTO = cr;
# 			cp.push(ct)
# 		}
# 		return cp
# 	}

if __name__ == '__main__':
    import os
    import scrapy
    os.system("cd chepiao")
    os.system("scrapy crawl ticket")
