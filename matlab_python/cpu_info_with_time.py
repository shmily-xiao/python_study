#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    获取指定时间段的cpu信息和内存使用信息
"""

import psutil
import pylab as pl
import time

#function of Get CPU State
def getCPUStatue(interval=1):
    return psutil.cpu_percent(interval)


#function of Get Memory
def getMemoryStatue():
    phymem = psutil.virtual_memory()
    buffers = getattr(psutil, 'phymem_buffers', lambda: 0)()
    cached = getattr(psutil, 'cached_phymem', lambda: 0)()
    used = phymem.total - (phymem.free + buffers + cached)
    line = " Memory: %5s%% %6s/%s" % (
        phymem.percent,
        str(int(used / 1024 / 1024)) + "M",
        str(int(phymem.total / 1024 / 1024)) + "M"
    )
    return phymem.percent

def printTheWindow(filename):
    # 打开文件
    try:
        fo = open(filename + ".txt", "r+")
        cpu_info_str = fo.read()
        fo.close()
    except Exception as e:
        print e
        print "没有temp_cpu_info.txt 文件，请先选择 --》 1.监听CPU  操作"
        return

    cpu_info_list = cpu_info_str.split(",")
    cpu_info_list = map(lambda x:float(x), cpu_info_list)

    length = len(cpu_info_list)
    x = xrange(length)
    # 画图形
    pl.axis([0, length, 0, 100])
    pl.plot(x, cpu_info_list)  # use pylab to plot x and y
    pl.show()  # show the plot on the screen


    print cpu_info_list



if __name__ == '__main__':
    print "\n"
    print "* ************** ***************** *"
    print "** ************ ** ************* ***"
    print "**** ********* **** ********** *****"
    print "****** ****** ****** ******* *******"
    print "******* **** ******** **** *********"
    print "********* * ********** * ***********"
    print "\n"
    print "程序会在当前目录生成一个名为 temp_cpu_info.txt 的文件，其中记录了一段时间之内CPU的运行状态（百分比）\n"
    filename = "temp_cpu_info"
    oper_info = raw_input("请你选择操作 1. 监听CPU   2. 输出图表 :  ")
    if oper_info == "1":
        times = raw_input("请输入要监听CPU的时间长度（秒） :  ")
        cpu_info = []
        start = time.time()
        for i in xrange(int(times)):
            cpu_info.append(getCPUStatue())

        # 打开文件
        fo = open(filename+".txt", "wb")
        fo.write(cpu_info.__repr__()[1:-1])
        fo.close()

        end = time.time()

        print "监听完成！ 用时{0}秒\n".format(end - start)

    elif oper_info == "2":
        printTheWindow(filename)


