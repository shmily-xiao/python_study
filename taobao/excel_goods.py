# coding:utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')


import xlwt
import MySQLdb
import xlrd
import datetime
import re
import requests
from decimal import Decimal

db_host = "localhost"
db_user = "root"
db_passwd = "qazwsx1234"
# https://pub.alimama.com/coupon/qq/export.json?adzoneId=150364908&siteId=39972563
db_name = "lemon_youxuan"

excel_file_paths = [r"/lemon/2018-04-10.xls"]


def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:root, 密码:123456,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = MySQLdb.connect(db_host,db_user,db_passwd,db_name, charset="utf-8")
    print('连接上了!')
    return db

def readExcel(file_path):
    xlsfile = file_path  # 打开指定路径中的xls文件

    book = xlrd.open_workbook(xlsfile)  # 得到Excel文件的book对象，实例化对象

    sheet_name = book.sheet_names()[0]  # 获得指定索引的sheet表名字
    print "2、", sheet_name
    return book.sheet_by_name(sheet_name)  # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定


def insertGoodsAndCoupons(db, path_list):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    nowtime = datetime.datetime.now()

    sheet = readExcel(path_list)

    nrows = sheet.nrows  # 获取行总数
    ncols = sheet.ncols  # 获取列总数

    # matrix = [[0 for i in range(ncols)] for i in range(nrows)]

    # 循环打印每一行的内容
    for i in range(nrows):
        if i == 0:
            continue

        if find_goods_by_taobaoid(db, sheet.cell_value(i, 0)):
            delete_one_goods(db,sheet.cell_value(i, 0))
            # continue

        # for j in range(ncols):
        print sheet.cell_value(i, 17)
        if '减' in sheet.cell_value(i, 17):
            coupon_price = int(re.findall("\\d+", sheet.cell_value(i, 17).split('减')[1]).__getitem__(0).__str__())
        else:
            coupon_price = int(re.findall("\\d+", sheet.cell_value(i, 17)).__getitem__(0).__str__())
        print "coupon_price:",coupon_price

        sql = "INSERT INTO goods_coupon(create_time,disable,update_time,available_time,coupon_price,expiration_time,name,online,url,total_count) \
               VALUES ('%s','%s','%s','%s','%d','%s','%s','%s','%s','%d')" % \
              (nowtime,'F',nowtime,sheet.cell_value(i, 18),coupon_price*100,sheet.cell_value(i, 19),sheet.cell_value(i, 17),'T',MySQLdb.escape_string(sheet.cell_value(i, 21)),int(sheet.cell_value(i, 15)))
        try:
            # 执行sql语句
            cursor.execute(sql)
            cursor.execute("select max(id) from lemon_youxuan.goods_coupon;")

            # 提交到数据库执行
            # temp_coupon = db.commit()
            temp_coupon_id = cursor.fetchall()[0][0]
            # 通过优惠券的url查询优惠券的主键
            # data = selectCoupon(db,sheet.cell_value(i, 17))

            print "insert new coupon_id:",temp_coupon_id

            # print "row1:",data[0]

            insertGoods(db,temp_coupon_id,sheet,i,nowtime)


        except Exception,e:
            print repr(e)
            # Rollback in case there is any error
            print 'insert failed!'
            db.rollback()


def find_goods_by_taobaoid(db,taobaoId):
    select_sql_count = """select count(*) from goods WHERE taobao_id={0}""".format(taobaoId)
    # select_sql_count = """select id from goods WHERE taobao_id={0}""".format(taobaoId)
    cursor = db.cursor()
    cursor.execute(select_sql_count)
    count = cursor.fetchall()
    if count[0][0]:
        print "overwrite ", taobaoId
        return taobaoId
    return None


def selectCoupon(db,name):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    selectSql = "SELECT * from goods_coupon WHERE name = '%s'" % (name)

    try:
        # 执行sql语句
        cursor.execute(selectSql)
        # 使用 fetchone() 方法获取一条数据
        return cursor.fetchone()

    except Exception,e:
        print repr(e)
        # Rollback in case there is any error
        print 'query failed!=%s' % (name)


def insertGoods(db,id,sheet,i,nowtime):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    if sheet.cell_value(i, 13) == '天猫':
        source = 'TMALL'
    else:
        source = 'TAOBAO'

    print "source:",source

    price = int(Decimal(sheet.cell_value(i, 6)).quantize(Decimal('0.00')) * 100)

    print "price:",price

    brokerage = int(Decimal(sheet.cell_value(i, 9)).quantize(Decimal('0.00')) * 100)

    print "brokerage:",brokerage

    detail_imgs = get_goods_detail_urls(int(sheet.cell_value(i, 0)))

    sql = "INSERT INTO goods(create_time,disable,update_time,brokerage,type_id,function_type,goods_url,online,primary_photos,refer_price,sold_count,source,taobao_id,title,goods_coupon_id, detail_imgs) \
               VALUES ('%s','%s','%s','%d',%d, '%s','%s','%s','%s','%d','%d','%s','%d','%s','%d', '%s')" % \
              (nowtime,'F',nowtime,brokerage,33,'DAILY_RECOMMEND',
               MySQLdb.escape_string(sheet.cell_value(i, 5)),'T',MySQLdb.escape_string(sheet.cell_value(i, 2)),price,int(sheet.cell_value(i, 7)),
               source,int(sheet.cell_value(i, 0)),sheet.cell_value(i, 1),id, detail_imgs)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

    except Exception, e:
        print repr(e)
        # Rollback in case there is any error
        print 'insert failed!'
        db.rollback()

def get_goods_detail_urls(goods_id):
    """
        通过商品的ID来获取详情图片
    :param goods_id:   562144271394
    :return:
    """

    url = "https://item.taobao.com/item.htm?id={0}".format(goods_id)

    try:


        r = requests.get(url)
        # r = requests.get(url, timeout=30)

        pattern = re.compile('//\w*\.alicdn\.com/\w*/i\d/\d*/\w*[\.]*[-]*\w*!*\w*-?\w*\.jpg*|//\w*\.alicdn\.com/\w*/i\d/\w*[\.]*[-]*\w*!*\w*-?\w*\.SS2*')
        html = r.text
        res = pattern.findall(html)
        res = list(set(res))
        return ",".join(res)
    except Exception as e:
        print e.message
        print url
        return ""

def closedb(db):
    db.close()

def delete_goods_and_coupon(db):

    now = datetime.datetime.now().strftime("%Y-%m-%d")
    now = now + " 0:0:0"
    select_sql_string = """ select id from goods_coupon WHERE expiration_time < '{0}'""".format(now)

    delete_goods_coupon_string = """delete from lemon_youxuan.goods_coupon WHERE id={0}"""
    delete_goods_string = """delete from lemon_youxuan.goods WHERE goods_coupon_id={0}"""

    cursor = db.cursor()

    print select_sql_string
    cursor.execute(select_sql_string)
    coupons = cursor.fetchall()
    if not coupons:
        return

    for item in coupons:
        print "coupon_id:" , item[0]
        cursor.execute(delete_goods_string.format(item[0]))
        cursor.execute(delete_goods_coupon_string.format(item[0]))
        cursor.fetchall()

    db.commit()


def delete_one_goods(db, key):

    select_sql_string = """ select goods_coupon_id from goods WHERE taobao_id={0}""".format(key)

    delete_goods_coupon_string = """delete from lemon_youxuan.goods_coupon WHERE id={0}"""
    delete_goods_string = """delete from lemon_youxuan.goods WHERE goods_coupon_id={0}"""

    cursor = db.cursor()

    # print select_sql_string
    cursor.execute(select_sql_string)
    coupons = cursor.fetchall()
    if not coupons:
        return

    for item in coupons:
        print "delete coupon_id:", item[0]
        cursor.execute(delete_goods_string.format(item[0]))
        cursor.execute(delete_goods_coupon_string.format(item[0]))
        cursor.fetchall()

    db.commit()


def main():
    db = connectdb()  # 连接MySQL数据库

    for excel_file_path in excel_file_paths:
        insertGoodsAndCoupons(db, excel_file_path)  # 插入数据

    print 'insert success'

    delete_goods_and_coupon(db)  # 删除过期的优惠券和相应的商品
    # delete_one_goods(db,1)

    print "delete success"

    closedb(db)  # 关闭数据库


if __name__ == '__main__':
    main()