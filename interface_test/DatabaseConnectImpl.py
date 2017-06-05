#!/usr/bin/env python
# -*- coding:utf-8 -*-

from IDatabaseConnect import IDatabaseConnect

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

print isinstance(db, IDatabaseConnect)