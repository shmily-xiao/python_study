#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class GoodsItem(object):

    """
                "eventCreatorId": 0,
                "rootCatId": 50008090,
                "leafCatId": 150708,
                "debugInfo": null,
                "rootCatScore": 0,
                "nick": "松乡数码旗舰店",
                "userType": 1,
                "title": "松乡 懒人手机支架床头桌面手机支架 创意多功能通用挂脖手机夹子",
                "sellerId": 2250855887,
                "shopTitle": "松乡数码旗舰店",
                "pictUrl": "//img.alicdn.com/bao/uploaded/i4/2250855887/TB10hg.X2DH8KJjy1XcXXcpdXXa_!!0-item_pic.jpg",
                "auctionId": 530433250579,
                "auctionUrl": "http://item.taobao.com/item.htm?id=530433250579",
                "biz30day": 20646,
                "tkMktStatus": null,
                "couponActivityId": null,
                "reservePrice": 8.9,
                "tkRate": 20.3,
                "tkCommFee": 1.38,
                "totalNum": 4950,
                "totalFee": 12710.9,
                "rlRate": 23.59,
                "hasRecommended": null,
                "hasSame": null,
                "zkPrice": 6.8,
                "tk3rdRate": null,
                "sameItemPid": "9223372036854775807",
                "couponTotalCount": 0,
                "couponLeftCount": 0,
                "dayLeft": -17528,
                "couponAmount": 0,
                "couponLink": "",
                "couponLinkTaoToken": "",
                "includeDxjh": 1,
                "auctionTag": "203 843 907 1163 1478 1483 2049 2059 3974 4166 4491 4555 5323 7883 11083 11339 16395 21442 25282 28353 28802 37569 40897 51585 51969 67521 74369 74433 82306 101762 119298 143746 151362 212546 243906",
                "couponStartFee": 0,
                "couponEffectiveStartTime": "",
                "couponEffectiveEndTime": "",
                "hasUmpBonus": null,
                "umpBonus": null,
                "isBizActivity": null,
                "couponShortLink": null,
                "couponInfo": "无",
                "eventRate": null,
                "rootCategoryName": null,
                "couponOriLink": null,
                "userTypeName": null
    """

    def __init__(self, detail_img_urls, type_id, ob):


        # 类似与外键 关系
        self.taobaoId = ob.get("auctionId")  # 淘宝的唯一ID，这个让我在更新的时候知道这个数据对应我们数据库里面的哪条记

        self.title = ob.get("title")  # 商品的标题或者是描述
        self.primaryPhotos = ob.get("pictUrl") # 商品首图的图片
        self.soldCount = ob.get("biz30day")  # 30天的销售
        # 数据库中没有
        self.tkRate = ob.get("tkRate")   # 佣金比率
        self.brokerage = int(float(ob.get("tkCommFee"))*100) # 最后的得到的佣金
        self.referPrice = int(float(ob.get("zkPrice"))*100) # 商品的价格，原价，不使用优惠卷的价格
        self.source = "TMALL" if ob.get("userType",0) else "TAOBAO" # 标示是天猫还是普通的  1 是天猫  0 是淘宝
        self.online = True
        self.disable = False
        self.createTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type_id = type_id  # 系统中的类型的id
        self.detailImgs = detail_img_urls # 详情中的图片链接

        #todo
        self.description = "" #暂时没有得自己后台运营写
        self.shipFree = False # 默认不包邮，现在拿不到数据
        self.goodsUrl = ""



        # 优惠券
        self.couponEffectiveStartTime = ob.get("couponEffectiveStartTime") #优惠券的开始时间
        self.couponEffectiveEndTime = ob.get("couponEffectiveEndTime") # 优惠券的结束使用时间
        self.couponTotalCount = ob.get("couponTotalCount") # 总共有多少优惠卷
        self.couponLeftCount = ob.get("couponLeftCount") # 剩余多少优惠券
        self.couponAmount = ob.get("couponAmount") # 优惠的金额
        self.couponInfo = ob.get("couponInfo") # 优惠券的描述
        # todo
        self.couponUrl = ""






