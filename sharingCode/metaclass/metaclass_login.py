#!/usr/bin/env python
# -*- coding:utf-8 -*-

from types import FunctionType

# 登录装饰器
def login_required(func):
    print 'login check logic here'

    def wrapper(*args, **kwargs):
        print ("i get you", args, kwargs)
        # 拿到这些值之后就可以去处理了return func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


class LoginDecorator(type):
    def __new__(cls, name, bases, dct):
        for name, value in dct.iteritems():
            if name not in ('__metaclass__', '__init__', '__module__') and type(value) == FunctionType:
                # 除了这几个方法都需要登录的验证
                value = login_required(value)
            dct[name] = value
        return type.__new__(cls, name, bases, dct)


class Operation(object):
    __metaclass__ = LoginDecorator

    # 需要登陆验证的方法
    def delete(self, x):
        print 'deleted %s' % str(x)

    def add(self, a):
        print 'add %s' % str(a)

def main():
    op = Operation()
    op.delete('test')
    print type(op)

if __name__ == '__main__':
    main()