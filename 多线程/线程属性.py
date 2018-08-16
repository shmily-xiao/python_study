#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

def showthreadinfo():
    print('currentthread = {}'.format(threading.current_thread()))
    print('main thread = {}'.format(threading._MainThread()), '"主线程对象"')
    print('active count = {}'.format(threading.active_count()), '"alive"')

def worker():
    count = 1
    showthreadinfo()
    while True:
        if (count > 5):
            break

        time.sleep(1)
        count += 1
        print("work")


class MyThread(threading.Thread):
    """
    python2.7 有点问题
    t.run()分别执行start或者run方法。使用start方法启动线程，启动了一个新的线程，
    名字叫做worker running.但是使用run方法启动的线程，并没有启动新的线程，
    只是在主线程中调用了一个普通函数而已。
    
    """

    # 这两个调用方式在python2.7 有问题
    def start(self):
        print('start~~~~~~~~~~~~~')
        # super().start()

    def run(self):
        print('run~~~~~~~~~~~~~~~~~')
        # super().run()

    # def __init__(self, *args, **kwargs):
    #     threading.Thread.__init__(self, args, kwargs)



def main():

    # t = threading.Thread(target=worker, name='worker')  # 线程对象
    t = MyThread(target=worker, name='worker')  # 线程对象

    showthreadinfo()
    print t.is_alive()
    print "id   ====> ", t.ident
    # t.start()

    while(True):
        time.sleep(1)
        if t.is_alive():
            print "True--->"
        else:
            print "False--->"



if __name__ == '__main__':
    main()