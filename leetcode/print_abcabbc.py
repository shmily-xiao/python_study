#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    使用三个线程 依次打印 abc abc
"""
import threading
import time
num_flag = {"num" : 0}

def func1(num):
    # for i in range(num):
    #     # threading.currentThread()获取当前线程，getName()获取线程名字
    #     print 'I am %s.num:%s' % (threading.currentThread().getName(), i)
    while(True):
        if num_flag["num"] != num:
            # 相当于等待另一个线程跑，然后空转
            continue

        if num == 0:
            print 'I am %s.num:%s' % (threading.currentThread().getName(), num)
            print "a"
        elif num == 1:
            print 'I am %s.num:%s' % (threading.currentThread().getName(), num)
            print "b"
        else:
            print 'I am %s.num:%s' % (threading.currentThread().getName(), num)
            print "c"
        num_flag["num"] += 1
        num_flag["num"] = num_flag["num"] % 3

        time.sleep(2)


def main(thread_num):
    thread_list = []  # 定义一个线程列表

    for i in range(thread_num):
        thread_list.append(threading.Thread(target=func1, args=(i,)))

    for a in thread_list:
        # a.setDaemon(True)这个setDaemon默认为False 非守护线程
        # 表示主线程等所有子线程结束后，在结束
        # 设置为True的话 表示是个守护线程 子线程就会随着主线程的结束而结束
        # 听说服务监控工具生成的心跳线程 就是用的守护线程
        a.start()

    for a in thread_list:
        a.join()  # 表示等待直到线程运行完毕


# ---------------------------------------------------------------------
#  上面的实现方式有一些取巧了
# ---------------------------------------------------------------------
lock_a = threading.Lock()
lock_b = threading.Lock()
lock_c = threading.Lock()

def print_a():
    while(True):
        lock_a.acquire()
        print "a"
        lock_b.release()

def print_b():
    while(True):
        lock_b.acquire()
        print "b"
        lock_c.release()

def print_c():
    while(True):
        lock_c.acquire()
        print "c"
        lock_a.release()

def main2():

    lock_b.acquire()
    lock_c.acquire()

    threading.Thread(target=print_b).start()
    threading.Thread(target=print_c).start()
    threading.Thread(target=print_a).start()





if __name__ == '__main__':
    # main(3)
    main2()