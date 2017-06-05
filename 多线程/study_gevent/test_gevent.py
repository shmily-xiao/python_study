#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /***************************************************/
# from gevent.monkey import patch_all
# patch_all()
# import time
# import gevent
#
# def compute(x,y):
#     print "Compute %s + %s ..." % (x, y)
#     # gevent.sleep(1)
#     time.sleep(1)
#     return x+y
#
# def print_sum(x,y):
#     result = compute(x, y)
#     print "%s + %s = %s" %(x, y, result)
#
# print_sum(2,9)
# /***************************************************/

# # /***************************************************/
# import gevent
#
# def foo():
#     print ('Running in foo')
#     gevent.sleep(0)
#     print ('Explicit context switch to foo again')
#
# def bar():
#     print ('Explicit context to bar')
#     gevent.sleep(0)
#     print ('Implicit context switch back to bar')
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar)
# ])
# # /***************************************************/

# # /***************************************************/
# import time
# import gevent
# from gevent import select
#
# start = time.time()
# tic = lambda: 'at %1.1f seconds' % (time.time() - start)
#
# def gr1():
#     # Busy waits for a second, but we don't want to stick around...
#     print ('Started Polling : %s' %tic())
#     select.select([],[],[],1)
#     print ('Ended Polling: %s '% tic())
#
# def gr2():
#     # Busy waits for a second, but we don't want to stick around...
#     print ('Started Polling :%s '% tic())
#     select.select([],[],[],2)
#     print ('Ended Polling: %s' % tic())
#
# def gr3():
#     print ("Hey lets do some stuff while the greenlets poll, %s" % tic())
#     gevent.sleep(1)
#
# gevent.joinall([
#     gevent.spawn(gr1),
#     gevent.spawn(gr2),
#     gevent.spawn(gr3)
# ])
# # /***************************************************/
#

# # /***************************************************/
# import gevent
# import random
# import time
#
# def task(pid):
#     """
#     Some non-deterministic task
#     """
#     # sleeptime = random.randint(0,5)*0.01
#     sleeptime = 1
#     gevent.sleep(sleeptime)
#     print('Task %s done and sleep %s ' % (pid, sleeptime))
#
# def synchronous():
#     for i in range(1,10):
#         task(i)
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in xrange(10)]
#     gevent.joinall(threads)
#
# print('Synchronous:')
# start = time.time()
# synchronous()
# end = time.time()
#
# print('Asynchronous:')
# start_a = time.time()
# asynchronous()
# end_a = time.time()
#
# print ("Synchronous use %s second" % (end-start))
# print ("Asynchronous use %s second" % (end_a-start_a))
# # /***************************************************/


# # /***************************************************/
# import gevent.monkey
# gevent.monkey.patch_socket()
#
# import gevent
# import urllib2
# import simplejson as json
# import time
#
# def fetch(pid):
#     response = urllib2.urlopen('http://json-time.appspot.com/time.json')
#     result = response.read()
#     json_result = json.loads(result)
#     datetime = json_result['datetime']
#
#     print ('Prcoess %s : %s' % (pid, datetime))
#     return json_result['datetime']
#
# def synchronous():
#     for i in range(1, 10):
#         fetch(i)
#
# def asynchronous():
#     threads = []
#     for i in range(1, 10):
#         threads.append(gevent.spawn(fetch, i))
#     gevent.joinall(threads)
#
# print('Synchronous:')
# start = time.time()
# synchronous()
# end = time.time()
#
# print('Asynchronous:')
# start_a = time.time()
# asynchronous()
# end_a = time.time()
#
# # /***************************************************/


# # /***************************************************/
# import time
#
# def echo(i):
#     time.sleep(0.001)
#     return i
#
# from multiprocessing.pool import Pool
#
# if __name__ == '__main__':
#     p = Pool(10)
#     run1 = [a for a in p.imap_unordered(echo, xrange(10))]
#     run2 = [a for a in p.imap_unordered(echo, xrange(10))]
#     run3 = [a for a in p.imap_unordered(echo, xrange(10))]
#     run4 = [a for a in p.imap_unordered(echo, xrange(10))]
#
#     print(run1 == run2 == run3 == run4)
#
#     from gevent.pool import Pool
#
#     p = Pool(10)
#     run1 = [a for a in p.imap_unordered(echo, xrange(10))]
#     run2 = [a for a in p.imap_unordered(echo, xrange(10))]
#     run3 = [a for a in p.imap_unordered(echo, xrange(10))]
#     run4 = [a for a in p.imap_unordered(echo, xrange(10))]
#
#     print(run1 == run2 == run3 == run4)
# # /***************************************************/


# # /***************************************************/
# import gevent
# from gevent import Greenlet
#
# def foo(message, n):
#     """
#     Each thread will be passed the message, and n arguments in its initialization
#
#     :param message:
#     :param n:
#     :return:
#     """
#     gevent.sleep(n)
#     print(message)
#
# # Initialize a new Greenlet instance running the named function foo
# thread1 = Greenlet.spawn(foo, "Hello", 1)
#
# # Wrapper for creating and running a new Greenlet form the named function foo,
# # with the passed arguments
# thread2 = gevent.spawn(foo, "I live!", 2)
#
# # Lambda expressions
# thread3 = gevent.spawn(lambda x:(x+1),2)
#
# threads = [thread1, thread2, thread3]
#
# # Block until all threads complete
# gevent.joinall(threads)
# # /***************************************************/

#
# # /***************************************************/
# import gevent
# from gevent import Greenlet
# class MyGreenlet(Greenlet):
#     def __init__(self, message, n):
#         Greenlet.__init__(self)
#         self.message = message
#         self.n = n
#
#     # 重载 run方法
#     def _run(self):
#         print (self.message)
#         gevent.sleep(self.n)
#
# g = MyGreenlet("Hi there !", 10)
# g.start()
# g.join()
# print g.started
# print g.ready()
# print g.successful()
# print g.value
# print g.exception
# # /***************************************************/

#
# # /***************************************************/
# import gevent
# def win():
#     return 'You Win!'
#
# def fail():
#     raise Exception('You fail at failing')
#
# winner = gevent.spawn(win)
# loser = gevent.spawn(fail)
#
# print (winner.started)
# print (loser.started)
#
# try:
#     gevent.joinall([winner, loser])
# except Exception as e:
#     print ('This will never be reached')
#
# print (winner.value)
# print (loser.value)
#
# print (winner.ready())
# print (loser.ready())
#
# print (winner.successful())
# print (loser.successful())
#
# print (winner.exception)
# print (loser.exception)
# # /***************************************************/


# # /***************************************************/
# import gevent
# import signal
#
# def run_forever():
#     gevent.sleep(10)
#
# if __name__ == '__main__':
#     gevent.signal(signal.SIGBREAK, gevent.kill)
#     thread = gevent.spawn(run_forever)
#     thread.join()
#
# # /***************************************************/


# # /***************************************************/
# # 超时
# import gevent
# from gevent import Timeout
#
# seconds = 3
#
# timeout = Timeout(seconds)
# timeout.start()
#
# def wait():
#     print ('You will be sleep')
#     gevent.sleep(11)
#
# try:
#     gevent.spawn(wait).join()
#     # 如果 try 块中的执行的时间超过了TimeOut的时间限制，就会触发exception
# except Timeout:
#     print('Could not complete')
#
# time_to_wait = 5
#
# class TooLong(Exception):
#     pass
#
# # 如果超过了 time_to_wait 的时间，就会调用TooLong方法
# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(3)
#
# try:
#     gevent.with_timeout(12, wait)
# except Timeout:
#     print ('You are time out')
# # /***************************************************/

# /***************************************************/
# monkey patching 猴子补丁
import socket
print(socket.socket)
print ('After monkey patch')
from gevent import monkey
monkey.patch_socket()
print (socket.socket)

import select
print (select.select)
monkey.patch_select()
print ('After monkey patch')
print (select.select)
# /***************************************************/



# /***************************************************/

