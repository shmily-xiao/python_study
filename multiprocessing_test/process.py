#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 多进程

from multiprocessing import Process, Pool
from pymongo import MongoClient

import os

def mongo():
    client = MongoClient('127.0.0.1', 27017)
    db = client.test
    return db

# 子进程要执行的代码
def run_proc(name):
    db = mongo()
    # db.process.find_and_modify(
    #     query={'_id': 2},
    #     update={'$inc': {'s1': 1}}
    # )
    db.process.update({"_id":2}, {'$inc': {'s1': 1}})

    print 'Run child process %s (%s)...' % (name, os.getpid())

def run_proc2(name):
    db = mongo()
    # db.process.find_and_modify(
    #     query={'_id': 2},
    #     update={'$inc': {'s2': 1}}
    # )
    db.process.update({"_id": 2}, {'$inc': {'s2': 1}})

    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()

    # p = Process(target=run_proc, args=('test',))
    # p2 = Process(target=run_proc, args=('test',))
    # print 'Process will start.'
    # p2.start()
    # p.start()
    # p2.join()
    # p.join()

    p = Pool()
    for i in range(500):
        p.apply_async(run_proc, args=(i,))
        p.apply_async(run_proc2, args=(i+1000,))

    p.close()
    p.join()
    print 'Process end.'