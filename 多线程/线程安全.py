#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import threading
import time

"""
线程安全：线程执行一段代码，不会产生不确定的结果，那这段代码就是线程安全的。

主线程是第一个启动的线程。
"""
logging.basicConfig(level=logging.INFO)  # 警告级别

def worker():
    for x in range(5):
        print("{} is running\n".format(threading.current_thread().name))
def main():
    for x in range(1, 5):
        name = 'worker{}'.format(x)
        t = threading.Thread(name=name, target=worker)
        t.start()


def worker_1():
    for x in range(100):
        logging.warning('{} is running'.format(threading.current_thread().name))


def main_1():
    for x in range(1, 5):
        name = 'work{}'.format(x)
        t = threading.Thread(name=name, target=worker_1)
        t.start()






def worker_2():
    for x in range(10):
        time.sleep(1)
        msg = ("{} is running".format(threading.current_thread()))
        logging.info(msg)

        t = threading.Thread(target=worker_3, name="worker1-{}".format(x))
        t.setDaemon(False)
        t.start()

        # t.join()

def worker_3():
    for x in range(10):
        time.sleep(0.3)
        msg = ("{} is running".format(threading.current_thread()))
        logging.info(msg)


def main_3():
    """
        第一被创建的进程叫做主线程
        
        线程具有一个daemon属性，可以显示设置为True或False，也可以不设置则取默认值None。
        如果不设置daemon，就取当前线程的daemon来设置它。子子线程继承子线程的daemon值，和设置None一样。
        
        主线程是non-daemon线程，即daemon=False。
        
        从主线程创建的所有线程不设置daemon属性，则默认都是daemon=False，也就是non-daemon线程。
        
        python程序在没有活着的non-daemon线程运行时退出，也就是剩下的只能是daemon线程，主线程才能退出，否则只能等待。

    :return: 
    """
    # 这是主
    # worker_2 不是主
    t = threading.Thread(target=worker_2,name='worker-{}'.format(0))
    # t.setDaemon(True)
    t.start()
    # t.join()
    time.sleep(0.3)
    print('ending')



def bar():
    time.sleep(1)
    print('bar')

def foo():
    for i in range(20):
        print(i)
    t = threading.Thread(target=bar)
    t.setDaemon(False)
    t.start()


def main_4():
    # 主线程是non-daemon线程
    t = threading.Thread(target=foo)
    t.setDaemon(True)
    t.start()
    # 加上 sleep 和去掉 sleep 的区别很大，一个输出一个没有输出 bar
    # 加上 sleep 是输出的
    time.sleep(1)

    print('Main Threading Exiting')


def foo_1(n):
    for i in range(n):
        print(i)
        time.sleep(1)

def main_5():

    """
        如果有非守护（non-daemon）线程的时候，主线程退出时，也不会杀掉所有守护（daemon）线程，直到所有非守护（non-daemon）线程全部结束
        如果还有非守护（daemon）线程，主线程需要退出，会结束所有守护（daemon）线程，退出。
        
        意思就是说 非守护线程 没有结束，程序还会继续；如果只剩下守护，主线程结束，程序也就结束了
    :return: 
    """
    t1 = threading.Thread(target=foo_1, args=(20,))
    t1.setDaemon(True) # True 说明是守护线程
    t1.start()

    print "t1 start"

    t2 = threading.Thread(target=foo_1, args=(10,))
    t2.setDaemon(False) # False 说明是非守护线程
    t2.start()

    # 使用了join方法后，daemon线程执行完了，主线程才退出。
    # join(timeout=None),是线程的标准方法之一。
    # 一个线程中调用另一个线程的join方法，调用者将被阻塞，直到被调用线程终止。
    # 一个线程可以被join多次。
    # timeout参数指定调用者等待多久，没有设置超时，就一直等待被调用线程结束。
    # 调用谁的join方法，就是join谁，就要等谁。

    t1.join()

    print('Main Threading Exiting')


a_list = []

def add_list():
    global a_list
    for i in xrange(1000):
        a_list.append(i)

def main_6():
    t1 = threading.Thread(target=add_list, args=())
    # t1.setDaemon(True)  # True 说明是守护线程


    print "t1 start"

    t2 = threading.Thread(target=add_list, args=())
    # t2.setDaemon(False)  # False 说明是非守护线程

    t2.start()
    t1.start()

    print a_list


if __name__ == '__main__':
    main_6()
    pass