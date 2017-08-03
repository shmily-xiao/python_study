#!/usr/bin/env python  
#  
# $Id: iotop.py 1160 2011-10-14 18:50:36Z g.rodola@gmail.com $  
#  
# Copyright (c) 2009, Jay Loden, Giampaolo Rodola'. All rights reserved.  
# Use of this source code is governed by a BSD-style license that can be  
# found in the LICENSE file.  
# Transplant to NT system by hui.wang, 2012-11-28  
# Add function of get cpu state and get memory state by hui.wang,2012-11-29  
  
""" 
Shows real-time network statistics. 
Author: Giampaolo Rodola' <g.rodola@gmail.com> 
"""  
  
import sys  
import os  
  
import atexit  
import time  
  
import psutil  
  
print "Welcome,current system is",os.name," 3 seconds late start to get data..."  
time.sleep(3)  
   
line_num = 1  
  
def print_line(str):  
    print str  
      
#function of Get CPU State  
def getCPUstate(interval=1):  
    return (" CPU: " + str(psutil.cpu_percent(interval)) + "%")

#function of Get Memory  
def getMemorystate():  
    phymem = psutil.virtual_memory()
    buffers = getattr(psutil, 'phymem_buffers', lambda: 0)()  
    cached = getattr(psutil, 'cached_phymem', lambda: 0)()  
    used = phymem.total - (phymem.free + buffers + cached)  
    line = " Memory: %5s%% %6s/%s" % (  
        phymem.percent,  
        str(int(used / 1024 / 1024)) + "M",  
        str(int(phymem.total / 1024 / 1024)) + "M"  
    )     
    return line

def bytes2human(n):  
    """ 
    >>> bytes2human(10000) 
    '9.8 K' 
    >>> bytes2human(100001221) 
    '95.4 M' 
    """  
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')  
    prefix = {}  
    for i, s in enumerate(symbols):  
        prefix[s] = 1 << (i+1)*10  
    for s in reversed(symbols):  
        if n >= prefix[s]:  
            value = float(n) / prefix[s]  
            return '%.2f %s' % (value, s)  
    return '%.2f B' % (n)  
  
  
def poll(interval):  
    """Retrieve raw stats within an interval window."""  
    tot_before = psutil.net_io_counters()
    pnic_before = psutil.net_io_counters(pernic=True)
    # sleep some time  
    time.sleep(interval)  
    tot_after = psutil.net_io_counters()
    pnic_after = psutil.net_io_counters(pernic=True)
    # get cpu state  
    cpu_state = getCPUstate(interval)  
    # get memory  
    memory_state = getMemorystate()  
    return (tot_before, tot_after, pnic_before, pnic_after,cpu_state,memory_state)  
  
  
  
  
def refresh_window(tot_before, tot_after, pnic_before, pnic_after,cpu_state,memory_state):  
    os.system("cls")  
    """Print stats on screen."""  
  
  
    #print current time #cpu state #memory  
    print_line(time.asctime()+" | "+cpu_state+" | "+memory_state)  
      
    # totals  
    print_line(" NetStates:")  
    print_line("total bytes:           sent: %-10s   received: %s"  % (bytes2human(tot_after.bytes_sent), bytes2human(tot_after.bytes_recv)) )  
    print_line("total packets:         sent: %-10s   received: %s"   % (tot_after.packets_sent, tot_after.packets_recv)   )  
  
  
  
  
    # per-network interface details: let's sort network interfaces so  
    # that the ones which generated more traffic are shown first  
    print_line("")  
    nic_names = pnic_after.keys()  
    nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)  
    for name in nic_names:  
        stats_before = pnic_before[name]  
        stats_after = pnic_after[name]  
        templ = "%-15s %15s %15s"  
        print_line(templ % (name, "TOTAL", "PER-SEC"))  
        print_line(templ % (  
            "bytes-sent",  
            bytes2human(stats_after.bytes_sent),  
            bytes2human(stats_after.bytes_sent - stats_before.bytes_sent) + '/s',  
        ))  
        print_line(templ % (  
            "bytes-recv",  
            bytes2human(stats_after.bytes_recv),  
            bytes2human(stats_after.bytes_recv - stats_before.bytes_recv) + '/s',  
        ))  
        print_line(templ % (  
            "pkts-sent",  
            stats_after.packets_sent,  
            stats_after.packets_sent - stats_before.packets_sent,  
        ))  
        print_line(templ % (  
            "pkts-recv",  
            stats_after.packets_recv,  
            stats_after.packets_recv - stats_before.packets_recv,  
        ))  
        print_line("")  
  
  
  
  
try:  
    interval = 0  
    while 1:  
        args = poll(interval)  
        refresh_window(*args)  
        interval = 1  
except (KeyboardInterrupt, SystemExit):  
    pass  
