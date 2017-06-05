#!/usr/bin/env python
# -*- coding:utf-8 -*-


# class PrefixMetaclass(type):
#
#     def __new__(cls, name, bases, attrs):
#         _attrs = (('my_' + name, value) for name, value in attrs.items())
#
#         _attrs = dict((name, value) for name, value in _attrs)
#         _attrs['echo'] = lambda self, phrase: phrase # 增加了一个 echo 方法
#
#         return type.__new__(cls, name, bases, _attrs)
#
#
# class Foo(object):
#     __metaclass__ = PrefixMetaclass
#     name = 'foo'
#
#     def bar(self):
#         print 'bar'
#
# if __name__ == '__main__':
#
#     f = Foo()
#     # print f.name
#     print f.my_name
#
#     f.my_bar()
#
#     print f.echo('asdad')
#

#
# def __new__(cls, name, bases, attrs):
#     _attrs = (('my_' + name, value) for name, value in attrs.items())
#
#     _attrs = dict((name, value) for name, value in _attrs)
#     _attrs['echo'] = lambda self, phrase: phrase
#
#     return type.__new__(cls, name, bases, _attrs)
#
# class PP_test(type):
#     def __new__(cls, name, bases, attrs):
#         return type.__new__(cls, name, bases, attrs)
#
# class Foo(object):
#     __metaclass__ = PP_test
#     name = 'foo'
#
#     def bar(self):
#         print 'bar'
#
# f = Foo()
# print f.name
# print f.__metaclass__
#
# PP_test2 = type('PP_tes2',(type,object,),{'__new__':__new__})
# Foo.__metaclass__ = PP_test2
# print Foo.__metaclass__
# f.__metaclass__=PP_test2
# d=Foo()
# # print d.my_name
# print d.name
#
# Foo = type('Foo',(object,), {'__metaclass__':PP_test2,'name':'dfd'})
# c = Foo()
# print c.__metaclass__
# print c.name
# # print c.my_name


# from types import FunctionType
#
# # 登录装饰器
# def login_required(func):
#     print 'login check logic here'
#     def wrapper(*args, **kwargs):
#         print ("i get you",args, kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# class LoginDecorator(type):
#     def __new__(cls, name, bases, dct):
#         for name, value in dct.iteritems():
#             if name not in ('__metaclass__', '__init__', '__module__') and type(value) == FunctionType:
#                 #  除了这几个方法都需要登录的验证
#                 value = login_required(value)
#
#             dct[name] = value
#         return type.__new__(cls, name, bases, dct)
#
#
# class Operation(object):
#     __metaclass__ = LoginDecorator
#
#     def delete(self, x):
#         print 'deleted %s' % str(x)
#
#
# def main():
#     op = Operation()
#     op.delete('test')
#
# if __name__ == '__main__':
#     main()

def monkey_patch(name, bases, dct):
    assert len(bases) == 1
    base = bases[0]
    print "base name ", base
    for name, value in dct.iteritems():
        if name not in ('__module__', '__metaclass__'):
            setattr(base, name, value)
    return base

class A(object):
    def a(self):
        print 'i am A object'


class PatchA(A):
    __metaclass__ = monkey_patch

    def patcha_method(self):
        print 'this is a method patched for class A'

def main():
    pa = PatchA()
    pa.patcha_method()
    pa.a()
    print dir(pa)
    print dir(PatchA)

if __name__ == '__main__':
    main()


