#! -*- coding:utf-8 -*-
import threading
import time
maxs = 10
threadLimiter=threading.BoundedSemaphore(maxs)
# def run(i):
#     print i

# start = time.time()
# for i in range(10):
#     t = threading.Thread(target=run, args=(i,))
#     t.start()
# end = time.time()
# print "the time is %s" %(end -start)

class test(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        threadLimiter.acquire()
        try:
            for j in range(1000):
                j = j + 1
                print "j is %d" %j
            self.i = 12
            print "code one ,my code, the num is %d" % self.i
        except:
            pass
        finally:
            threadLimiter.release()

    def get_result(self):
        if self.i == 12:
            return True
        else:
            return False
# # 1
# for i in range(100):
#     cur = test(i)
#     cur.start()
#
# # 2
#     for j in range(100):
#         # cur = test(i)
#         # cur.start()
#         cur.join(j)

# 3
# f =test(1)
# f.start()
# while f.is_alive():
#     continue
# print f.get_result()

# 4
# for i in range(1000):
#     cur = test(i)
#     cur.start()
#     for j in range(100):
#         cur.join()
#

# 线程池
import threadpool
def ThreadFun(arg1,arg2):
    print "args1 and args2 {0} {1}".format(arg1, arg2)
    pass
def main():
    device_list=["sdfsf","sfsf","sdfsfs","qeqwe"]#需要处理的设备个数
    task_pool=threadpool.ThreadPool(8)#8是线程池中线程的个数
    request_list=[]#存放任务列表
    #首先构造任务列表
    for device in device_list:
        request_list.append(threadpool.makeRequests(ThreadFun,[((device, ), {})])[0])
    #将每个任务放到线程池中，等待线程池中线程各自读取任务，然后进行处理，使用了map函数，不了解的可以去了解一下。
    map(task_pool.putRequest,request_list)
    #等待所有任务处理完成，则返回，如果没有处理完，则一直阻塞
    task_pool.poll()

def pft(args):
    print "args is %s" % args

def testMap():
    request=[]
    for i in range(10):
        request.append(i)
    map(pft,request)

if __name__=="__main__":
    main()
    # testMap()

