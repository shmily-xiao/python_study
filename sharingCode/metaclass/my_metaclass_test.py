#!/usr/bin/env python
# -*- coding:utf-8 -*-

class PrefixMetaclass(type):

    # 可以通过重载元类的 __new__ 方法，修改 类定义 的行为
    # cls 和 self 的区别
    # cls是type的实例，self是cls的实例
    # self 主要去代表类的实例
    # cls 主要去代表这个类
    def __new__(cls, name, bases, attrs):
        _attrs = (('my_' + name, value) for name, value in attrs.items())
        _attrs = dict((name, value) for name, value in _attrs)
        _attrs['echo'] = lambda self, phrase: phrase # 增加了一个 echo 方法

        return type.__new__(cls, name, bases, _attrs)


class Foo(object):
    __metaclass__ = PrefixMetaclass
    name = 'foo'

    def bar(self):
        print 'bar'

class B(Foo):
  prop = 'B-func'

if __name__ == '__main__':

    f = Foo()
    # print f.name
    print f.my_name
    f.my_bar()
    print f.echo('asdad')
    b = B()
    # print b.prop
    print b.my_prop

# class Foo:
#   __metaclass__ = PrefixMetaclass
# 就会等价于
# Foo = PrefixMetaclass（'Foo', (object,), {}） 的语法糖
