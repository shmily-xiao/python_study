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
