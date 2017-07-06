#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Simple(object):
    def __init__(self):
        self.df="wqe"
        print( "constructor called, id={0}".format( id( self )))

    def __del__(self):
        print( "destructor called, id={0}".format( id( self )))

    def __new__(self):
        print( "new called, id={0}".format( id( self )))
        # 如果有这个方法，它将控制这个类的创建，如果不调用父类的__new__()
        # 这个类将不会被创建
        # return super( Simple, self ).__new__( self )

if __name__ == '__main__':
    ss = Simple()

    print ss.df
