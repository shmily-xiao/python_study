#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    做的事情:
        分析mongodb的查询性能
        我们从下面几个维度来分析
            1. 存储空间
            2. 时间
        怎么做：
            1. 生成数据
            2. 分两类来考察
                a. 冗余一定的数据来加快数据本身的子父级关系
                b. 建立索引的方式
            3. 统计数据库的空间成本，查询话费的时间成本
            
        举例：
            1. 数据结构如下：
                {"id"：1, "data":"adasdasd","parent":2}
                {"id"：2, "data":"adasdasd","parent":null}
            2. 数据结构如下：
                {"id":2 , "data":"asdasdasd","children":[2,3],"parent":null}
                {"id":2 , "data":"asdasdasd","children":[],"parent":2}
        
        我们要查询的数据是：将一条数据的子数据都查询出来
        
            第一种查询方式 
                db.test1.find({"parent":2})
            第二种查询方式:
                db.test2.find({"$in":{"_id":[2,3,4]}})
"""

import random


def get_id(db):
    key = db.seq.find_and_modify(
        query={'name': 'mongo_test'},
        update={'$inc': {'seq': 1}}
    )

    if not key:
        db.seq.insert({"name": "mongo_test", "seq": 1})
        return 1

    return key['seq']


def init_data(client):
    """ 构造数据 """

    db1 = client["mongo_test1"]
    db2 = client["mongo_test2"]

    for i in xrange(100000):
        key1 = get_id(db1)
        parent_id = None
        if random.random() > 0.2:
            parent_id = random.randint(1, i + 1)
        data = {"_id": key1, "data": "And loved your beauty with love false or true {0}".format(i),
                "parent_id": parent_id}

        db1.mongo_test.insert(data)

        # children_id = []
        # if random.random() > 0.5:
        #     for ii in xrange(random.randint(1,i+1)):
        #         children_id.append(random.randint(1,i+1))

        key2 = get_id(db2)
        data2 = {"_id": key2, "data": "And loved your beauty with love false or true {0}".format(i), "children_id": [],
                 "parent_id": parent_id}

        # print data
        db2.mongo_test.insert(data2)
        if parent_id:
            parent = db2.mongo_test.find_one({"_id": parent_id})
            if parent and parent.get("parent_id") is None:
                children = parent.get("children_id", [])
                children.append(key2)
                db2.mongo_test.save(parent)

        if i % 10000 == 0:
            print "{0}0 % ".format(i // 10000)


def test_db(client):
    """测试花费的时间"""
    db1 = client["mongo_test1"]
    import time

    start = time.time()
    parent = db1.mongo_test.find({"parent": None})

    for item in parent:
        children = db1.mongo_test.find({"parent_id": item.get("_id")})

    end = time.time()

    test_db1_time = end - start

    db2 = client["mongo_test2"]
    start = time.time()
    parent = db2.mongo_test.find({"parent": None})
    for item in parent:
        if item.get("children_id"):
            children = db2.mongo_test.find({"_id": {"$in": item.get("children_id")}})

    end = time.time()

    test_db2_time = end - start

    db3 = client["mongo_test3"]
    start = time.time()
    parent = db3.mongo_test.find({"parent": None})

    for item in parent:
        children = db3.mongo_test.find({"parent_id": item.get("_id")})

    end = time.time()

    test_db3_time = end - start

    print "第一种方式花费时间：{0} \n" \
          "第二种方式花费时间：{1} \n" \
          "第三种方式花费时间(parent建立索引)：{2}".format(test_db1_time, test_db2_time,
                                             test_db3_time)


if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient(host='127.0.0.1', port=27017)

    # init_data(client)
    test_db(client)