#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import MySQLdb
import re
import time

from GoodsItem import GoodsItem


class Taobao(object):


    HEADERS = {
        'Host': 'pub.alimama.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'Cookie': ''
    }

    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = "3306"
    MYSQL_PWD = "1234"
    MYSQL_DATABASE = "test"
    MYSQL_USER = "root"

    # 如果更换了推荐的id，请更换这个id
    ADZONE_ID = 150364908
    SITE_ID = 39972563
    # adzoneid = 150364908
    # siteid = 39972563

    def __init__(self):
        # 打开数据库连接
        self.db = MySQLdb.connect(host=self.MYSQL_HOST, user=self.MYSQL_USER, passwd=self.MYSQL_PWD, db=self.MYSQL_DATABASE, charset="utf8")
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def __del__(self):
        print '我被关闭了～'
        # 销毁对象的时候关闭链接
        # 关闭数据库连接
        self.db.close()


    def get_my_share_url(self, goods_id):
        """
            adzoneid: 150364908 这是我的一站到底的推广id
        :return:
            "data": {
                "taoToken": "￥5bKU09rhT0D￥",
                "couponShortLinkUrl": null,
                "qrCodeUrl": "//gqrcode.alicdn.com/img?type=hv&text=https%3A%2F%2Fs.click.taobao.com%2FXri4TVw%3Faf%3D3&h=300&w=300",
                "clickUrl": "https://s.click.taobao.com/t?e=m%3D2%26s%3D1eGfPsF7EBEcQipKwQzePOeEDrYVVa64K7Vc7tFgwiG3bLqV5UHdqTFxzYbfMadJHGUKWrwhgPmS9CyLfa8rKFVNnn93UwPWLJMtQW%2FCoqYDKhu7g%2FMIQ%2BSsj%2FiWuXJU7g8%2F2dfxKGqf9dPb5ep78TvlVOO1cB5UVxv5pEBodVrAMw8nFiE3SeGQ8vapW7cmGjry1d39tEqIwU8FX%2BGrS8YOae24fhW0&pvid=19_123.112.83.195_3510_1514901720351",
                "couponLink": "",
                "type": "auction",
                "shortLinkUrl": "https://s.click.taobao.com/Xri4TVw"
            }
        """
        now = long(time.time())
        # goods_id = 561912091456

        # http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=548524058949&adzoneid=150364908&siteid=39972563&scenes=1&channel=tk_9k9&t=1514896734365&_tb_token_=e365655409b3e&pvid=16_123.112.83.195_507_1514896704333
        url = "http://pub.alimama.com/common/code/getAuctionCode.json?auctionid={0}&adzoneid={1}" \
              "&siteid={2}&scenes=1&channel=group&t={3}&_tb_token_=e365655409b3e&pvid=12_221.217.219.133_568_1514901809663"

        get_url = url.format(goods_id, self.ADZONE_ID, self.SITE_ID, now)

        r = requests.get(get_url, headers=self.HEADERS)

        data = ""
        if r.status_code == 200:
            try:
                data = json.loads(r.text)
            except Exception as e:
                print e
                print get_url
                return ""


        return data.get("data")

    def get_goods_by_taobao(self):
        """
            获取淘宝自己排序的商品
        :return:
        """
        goods_type = "9k9.json"
        toPage = 1
        perPageSize = 50

        # url = "http://pub.alimama.com/items/channel/9k9.json?channel=9k9&perPageSize=50&shopTag=&t=1514471985823&_tb_token_=e365655409b3e&pvid=19_114.244.66.195_577_1514471782073"
        # url = "https://tds.alicdn.com/json/item_imgs.htm?cb=jsonp_image_info&id=562144271394"
        # url = "https://tds.alicdn.com/json/item_imgs.htm?cb=jsonp_image_info&t=TB13WplgL2H8KJjy0FcXXaDlFXa&sid=11516132&id=562671602952&s=8c044083a1d11d28d94339fd726a1646&v=2&m=1"
        # http://pub.alimama.com/items/channel/9k9.json?channel=9k9&toPage=2&perPageSize=50&shopTag=&t=1514476176708&_tb_token_=e365655409b3e&pvid=16_114.244.66.195_536_1514471985950
        url = 'https://s.click.taobao.com/jaA44Vw'
        r = requests.get(url,headers = self.HEADERS)

        # request('get', url, params=params, **kwargs)

        # if r.status_code != 200:
        #     print r.text
        #     return
        #
        print "@@@@@@"
        print r
        print r.text
        # response = r.text
        response={}


        # data = json.loads(response).get("data", {})
        data = response.get("data", {})
        # print data

        pageList = data.get("pageList", [])

        # print len(pageList)

        pass


    def do_actions(self):
        group_ids = self.get_my_groups()
        for item in group_ids:
            goods_list = self.get_goods_by_group_id(item)
            map(self.handler_goods, goods_list)


    def handler_goods(self, goods):
        """
        处理商品
        从阿里妈妈的group中获取名字，然后根据组的名字在我们的数据中找goodsType中的类型，
        名字这个数据必须是一一对应的
        :param goods:
        :return:
        """
        if goods.get("status") == -1:
            # 如果这个商品被置为失败，那么就删掉这个商品
            self._delete_goods_by_taoboId(goods.get("auctionId"))
            return
        goods_type = goods.get("lemon_group_title").split("-")
        item_goods_type = goods_type.pop() # 最具体的那一层
        type_goods_type = goods_type.pop() # 第二级
        home_goods_type = goods_type.pop() # 第一级



        self.cursor.execute("select id from goods_type WHERE name='{0}' AND level={1}".format(home_goods_type.encode('utf-8'), 1))
        results = self.cursor.fetchall()
        if not results:
            return
        home_id = results[0][0]

        self.cursor.execute("select id from goods_type WHERE name='{0}' AND level={1} AND parent_id={2}".format(type_goods_type.encode('utf-8'), 2, int(home_id)))
        results = self.cursor.fetchall()
        if not results:
            return
        type_id = results[0][0]

        self.cursor.execute("select id from goods_type WHERE name='{0}' AND level={1} AND parent_id={2}".format(item_goods_type.encode('utf-8'), 3, int(type_id)))
        results = self.cursor.fetchall()
        item_id = results[0][0]

        if not item_id:
            return

        share_url_data = self.get_my_share_url(goods.get("auctionId"))
        if not share_url_data:
            print "skip", goods.get("auctionId")
            return
        try:
            db_goods = GoodsItem(share_url_data, self.get_goods_detail_urls(goods.get("auctionId")), item_id, goods)
            # map(self.goods_2_db, db_goods)
            self.goods_2_db(db_goods)
        except Exception as e:
            print e.message
        time.sleep(0.7)

    def _delete_goods_by_taoboId(self, taobaoId):
        """
            通过淘宝ID 删除数据库里面的数据
        :param taobaoId:
        :return:
        """
        if not taobaoId:
            return
        select_sql_count = """select count(*) from goods WHERE taobao_id={0}""".format(taobaoId)
        self.cursor.execute(select_sql_count)
        count = self.cursor.fetchall()
        if not count[0][0]:
            return taobaoId

        delete_sql_count = """delete from goods WHERE taobao_id={0}""".format(taobaoId)
        self.cursor.execute(delete_sql_count)
        delete_count = self.cursor.fetchall()
        print "delete taobaoId : {0}, count : {1}".format(taobaoId, delete_count)
        return taobaoId


    def get_my_groups(self):

        """
            得到我淘宝账号中的groups 中的id
        :return:
        """

        # url
        # http://pub.alimama.com/favorites/group/newList.json?toPage=1&perPageSize=40&keyword=&t=1514726684042&_tb_token_=e13547ee573e3&pvid=11_221.217.219.133_2548_1514726683977


        get_url = "http://pub.alimama.com/favorites/group/newList.json?toPage=1&perPageSize={0}&keyword=&t=1514726684042&_tb_token_=e13547ee573e3&pvid=11_221.217.219.133_2548_1514726683977"

        url = get_url.format(40)

        r = requests.get(url,headers=self.HEADERS, verify=False)

        data = ""
        if r.status_code == 200:
            data = json.loads(r.text)

        if not data:
            return ""

        total_count = data.get("data",{}).get("totalCount",1)

        url = get_url.format(total_count)
        r = requests.get(url,headers=self.HEADERS)
        data = json.loads(r.text)
        result = data.get("data",{}).get("result",[])

        group_ids = []
        for item in result:
            group_ids.append(item.get("id"))

        # print group_ids
        return group_ids



        # 数据结构
        # data  = {"data":{"eventNum":0,"normalNum":1,"maxGroupNum":200,"groupCountReachLimit":false,"maxItemNumPerGroup":200,"result":[{"id":15323662,"createTime":"2017-12-27","groupType":1,"title":"创建于 2017-12-27 23:12:15","pubId":128981071,"itemNum":5,"updateTime":"2017-12-28","pictUrlList":["//gtms04.alicdn.com/tps/i4/108657717/TB1dX2ikjnD8KJjSspbXXbbEXXa_!!0-item_pic.jpg","//gtms04.alicdn.com/tps/i3/870515235/TB1t3FEdqzB9uJjSZFMXXXq4XXa_!!0-item_pic.jpg","//gtms04.alicdn.com/tps/i4/2458031621/TB1bn9RcRLN8KJjSZFPXXXoLXXa_!!0-item_pic.jpg","//gtms04.alicdn.com/tps/i1/1710444360/TB1RfQEkbYI8KJjy0FaXXbAiVXa_!!0-item_pic.jpg"]}],"nextPage":1,"pageNo":1,"pageSize":40,"totalCount":1,"totalPages":1,"hasNext":false,"hasPre":false,"prePage":1},"info":{"message":null,"pvid":"11_221.217.219.133_533_1514726684158","ok":true},"ok":true,"invalidKey":null}
        pass

    def get_goods_by_group_id(self, group_id):
        """
        从group中获取我优选的商品
        :return:
        """
        #url
        get_url= "http://pub.alimama.com/favorites/item/list.json?groupId={0}&toPage=1&perPageSize=40&t=1514725889741&_tb_token_=e13547ee573e3&pvid=12_221.217.219.133_8009_1514725889618"

        url = get_url.format(group_id)

        r = requests.get(url, headers=self.HEADERS)
        data = json.loads(r.text)

        item_list = data.get("data",{}).get("itemList",[])
        title = data.get("data",{}).get("title","")
        for item in item_list:
            # 用一个取用一个
            item["lemon_group_title"] = title
            yield item


    def goods_2_db_data(self):

        pass

    def goods_2_db(self, gscn):
        """
        更新goods 和 goodsCoupon
        :return:
        """
        select_sql_count = """select count(*) from goods WHERE taobao_id={0}""".format(gscn.taobaoId)
        self.cursor.execute(select_sql_count)
        count = self.cursor.fetchall()
        if count[0][0]:
            print "skipped", gscn.taobaoId
            # coupon_id = None
            # if gscn.couponAmount:
            #     count_id =
            # sql_goods = """update goods set create_time, update_time, disable, description, detail_imgs,
            #                             goods_url, primary_photos, real_price, refer_price, source, title, type_id, brokerage,
            #                             sold_count, online, goods_coupon_id)
            #                             VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15}) WHERE taobao_id = {16}""". \
            #     format(gscn.createTime, gscn.updateTime, gscn.disable, gscn.description.encode('utf-8'),
            #            gscn.detailImgs, gscn.goodsUrl, gscn.primaryPhotos,
            #            gscn.referPrice - int(float(gscn.couponAmount) * 100), gscn.referPrice, gscn.source,
            #            gscn.title.encode('utf-8'),
            #            gscn.type_id, gscn.brokerage, gscn.soldCount, gscn.online, coupon_id, gscn.taobaoId)

            return

        try:
            coupon_id = "null"
            if gscn.couponAmount:
                # SQL 插入语句
                sql_coupon = """INSERT INTO goods_coupon(create_time, update_time, disable, available_time, expiration_time, coupon_price, name, online, url, total_Count)
                         VALUES ("{0}","{1}","{2}","{3}","{4}",{5},"{6}","{7}","{8}",{9})""".\
                    format(gscn.createTime, gscn.updateTime, 'T' if gscn.disable else 'F', gscn.couponEffectiveStartTime,
                           gscn.couponEffectiveEndTime, int(float(gscn.couponAmount)), gscn.couponInfo.encode('utf-8'),
                           'T' if gscn.online else 'F', gscn.couponUrl, gscn.couponTotalCount)

                self.cursor.execute(sql_coupon)
                coupon_id = self.cursor.lastrowid

            sql_goods = """INSERT INTO goods(create_time, update_time, disable, description, detail_imgs, 
                            goods_url, primary_photos, refer_price, source, title, type_id, brokerage, 
                            sold_count, online, goods_coupon_id, taobao_id)
                            VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}",{7},"{8}","{9}",{10},{11},{12},"{13}",{14},{15})""". \
                format(gscn.createTime, gscn.updateTime, 'T' if gscn.disable else 'F', gscn.description.encode('utf-8'),gscn.detailImgs,gscn.goodsUrl, gscn.primaryPhotos,
                        gscn.referPrice, gscn.source, gscn.title.encode('utf-8'),
                       gscn.type_id, gscn.brokerage, gscn.soldCount, 'T' if gscn.online else 'F', coupon_id, gscn.taobaoId)
            print sql_goods
            # 执行sql语句
            self.cursor.execute(sql_goods)

            # 提交到数据库执行
            self.db.commit()
            print 'commit success'
            # self.db.autocommit(True)
        except Exception as e:
            # Rollback in case there is any error
            print e
            self.db.rollback()





    def get_goods_detail_url(self):

        # 说明
        # 这个i20 后面的20 可以根据图片的index来决定
        # 后面的id、是链接的上面的最后的数字
        # https://img.alicdn.com/imgextra/i20/11516132/TB2Wb.wff2H8KJjy0FcXXaDlFXa_!!11516132.jpg

        pass

    def get_goods_detail_urls(self, goods_id):
        """
            通过商品的ID来获取详情图片
        :param goods_id:   562144271394
        :return:
        """

        url = "https://item.taobao.com/item.htm?id={0}".format(goods_id)

        r = requests.get(url)

        pattern = re.compile('//\w*\.alicdn\.com/\w*/i\d/\d*/\w*[\.]*[-]*\w*!*\w*-?\w*\.jpg*|//\w*\.alicdn\.com/\w*/i\d/\w*[\.]*[-]*\w*!*\w*-?\w*\.SS2*')
        html = r.text
        res = pattern.findall(html)
        res = list(set(res))
        return ",".join(res)


if __name__ == '__main__':
    # get_goods_by_taobao()

    tao = Taobao()
    # tao.get_goods_detail_urls(562144271394)
    # tao.do_actions()
    print tao.get_goods_detail_urls(562224396958)
    # print tao.get_goods_detail_urls(558660616304)

