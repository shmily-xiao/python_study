#!/usr/bin/env python
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod
class IDatabaseConnect(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dbConnect(self):
       pass

    @abstractmethod
    def getGridFS(self, dbName='data'):
        pass

    def pst(self):
        """ 这个类可以被子类正常使用，子类可以不用去实现这个方法"""
        print "asdasedads"
