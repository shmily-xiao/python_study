#!/usr/bin/env python
# -*- coding:utf-8 -*-

from IDatabaseConnect import IDatabaseConnect

# 使用继承的方式 实现接口里面的方法，如果没有完全实现，在实例化这个子类的时候会报错
class DatabaseConnectImpl(IDatabaseConnect):

    def dbConnect(self):
        print "db connect"


    def getGridFS(self, dbName='data'):
        print "db getGridFS"
        print dbName


# IDatabaseConnect.register(DatabaseConnectImpl)

db = DatabaseConnectImpl()
db.getGridFS()
DatabaseConnectImpl().getGridFS()
db.pst()

print isinstance(db, IDatabaseConnect)