#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    获取指定时间段的cpu信息和内存使用信息
"""

import psutil
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
        sys_info_str = fo.read()
        fo.close()
    except Exception as e:
        print e
        print "没有temp_cpu_info.txt 文件，请先选择 --》 1.监听CPU  操作"
        return

    cpu_info_list = sys_info_str.split("\n")[0].split(",")
    cpu_info_list = map(lambda x:float(x), cpu_info_list)

    memory_info_list = sys_info_str.split("\n")[1].split(",")
    memory_info_list = map(lambda x:float(x), memory_info_list)


    length = len(cpu_info_list)
    x = xrange(length)
    # 画图形
    import pylab as pl
    pl.axis([0, length, 0, 110])
    pl.plot(x, cpu_info_list, label='cpu', linewidth=2)  # use pylab to plot x and y
    pl.plot(x, memory_info_list, label='memory')  # use pylab to plot x and y
    pl.title('system information')
    pl.legend()
    pl.show()  # show the plot on the screen





if __name__ == '__main__':
    print "\n"
    print "* ************** ***************** *"
    print "** ************ ** ************* ***"
    print "**** ********* **** ********** *****"
    print "****** ****** ****** ******* *******"
    print "******* **** ******** **** *********"
    print "********* * ********** * ***********"
    print "\n"
    print "powered by wangzaijun \n"
    print "程序会在当前目录默认生成一个名为 temp_cpu_info.txt 的文件，\n其中记录了一段时间之内CPU的运行状态和内存的使用情况（百分比）\n"
    filename = "temp_cpu_info"
    need_name = raw_input("请你选择操作 1. 使用默认名称   2. 自定义名称   -》  ")
    if need_name == "2":
        filename = raw_input("请你输入名称   -》  ")
    oper_info = raw_input("请你选择操作 1. 监听CPU和内存使用情况   2. 输出图表   -》  ")
    if oper_info == "1":
        times = raw_input("请输入要监听CPU的时间长度（秒） :  ")
        print "监听开始了！请骚等..."
        cpu_info = []
        memory_info = []
        start = time.time()
        for i in xrange(int(times)):
            cpu_info.append(getCPUStatue())
            memory_info.append(getMemoryStatue())

        # 打开文件
        fo = open(filename+".txt", "wb")
        fo.write(cpu_info.__repr__()[1:-1]+"\n" + memory_info.__repr__()[1:-1])
        fo.close()

        end = time.time()

        print "监听完成！ 用时{0}秒\n".format(end - start)

    elif oper_info == "2":
        printTheWindow(filename)


