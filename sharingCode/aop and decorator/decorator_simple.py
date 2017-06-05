#!/usr/bin/env python
# -*- coding:utf-8 -*-

def makebold(fn):
    def wrapped():
        try:
            return "< b >" + fn() + "< / b >"
        except:
            return "some error"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "< i >" + fn() + "< / i >"
    return wrapped


@makebold
@makeitalic
def hello_one():
    raise Exception
    return "hello world"


print hello_one()  ## returns < b >< i >hello world< / i >< / b >


# 交换一下位置
@makeitalic
@makebold
def hello_two():
    return "hello world"

print hello_two()

# 解封有惊喜
print "/*******************装饰器的原理********************/"


def hello_three():
    return "i am hello three"

print makeitalic(hello_three)()
print makebold(makeitalic(hello_three))()
hello_three = makebold(makeitalic(hello_three))
print hello_three()