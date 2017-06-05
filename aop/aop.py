#!/usr/bin/env python
# -*- coding: utf-8 -*-
# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
# def makeitalic(fn):
#     # def wrapped():
#     return "<i>" + fn() + "</i>"
#     # return wrapped
#
# # @makeitalic
# # @makebold
# def hello():
#     return "hello world"

# print makeitalic(hello)
# print hello()

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # 包装器接受所有参数
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print "Do I have args?:"
        print args
        print kwargs
        # 现在把*args,**kwargs解包
        # 如果你不明白什么是解包的话,请查阅:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print "Python is cool, no argument here."

function_with_no_argument()
#输出
#Do I have args?:
#()
#{}
#Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print a, b, c

function_with_arguments(1,2,3)
#输出
#Do I have args?:
#(1, 2, 3)
#{}
#1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print "Do %s, %s and %s like platypus? %s" %(a, b, c, platypus)

function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
#输出
#Do I have args ? :
#('Bill', 'Linus', 'Steve')
#{'platypus': 'Indeed!'}
#Do Bill, Linus and Steve like platypus? Indeed!

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # 可以加入一个默认值
        print "I am %s, what did you think ?" % (self.age + lie)

m = Mary()
m.sayYourAge()
m.sayYourAge(lie=-1)
#输出
# Do I have args?:
#(<__main__.Mary object at 0xb7d303ac>,)
#{}
#I am 28, what did you think?

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print "I make decorators! And I accept arguments:", decorator_arg1, decorator_arg2

    def my_decorator(func):
        # 这里传递参数的能力是借鉴了 closures.
        # 如果对closures感到困惑可以看看下面这个:
        # http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print "I am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2

        # 不要忘了装饰器参数和函数参数!
        def wrapped(function_arg1, function_arg2) :
            print ("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments("Rajesh", "Howard")


def decorator_with_args(decorator_to_enhance):
    print "/************** 1 ************/"
    """
    这个函数将被用来作为装饰器.
    它必须去装饰要成为装饰器的函数.
    休息一下.
    它将允许所有的装饰器可以接收任意数量的参数,所以以后你不必为每次都要做这个头疼了.
    saving you the headache to remember how to do that every time.
    """

    # 我们用传递参数的同样技巧.
    def decorator_maker(*args, **kwargs):
        print "/************** 2 ************/"
        print args
        print kwargs

        # 我们动态的建立一个只接收一个函数的装饰器,
        # 但是他能接收来自maker的参数
        def decorator_wrapper(func):
            print "/************** 3 ************/"
            print func
            # 最后我们返回原始的装饰器,毕竟它只是'平常'的函数
            # 唯一的陷阱:装饰器必须有这个特殊的,否则将不会奏效.
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper
    return decorator_maker


# 下面的函数是你建来当装饰器用的,然后把装饰器加到上面:-)
# 不要忘了这个 "decorator(func, *args, **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    print "/************** 4 ************/"
    print func
    def wrapper(function_arg1, function_arg2):
        print "/************** 5 ************/"
        print "Decorated with", args, kwargs
        return func(function_arg1, function_arg2)
    return wrapper

# 现在你用你自己的装饰装饰器来装饰你的函数(汗~~~)


@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print "/************** 6 ************/"
    print "Hello", function_arg1, function_arg2

decorated_function("Universe and", "everything")
#输出:
#Decorated with (42, 404, 1024) {}
#Hello Universe and everything

print "*******************************************"

#为了debug,堆栈跟踪将会返回函数的 __name__
def foo():
    print "foo0"

print foo.__name__
#输出: foo

# 如果加上装饰器,将变得有点复杂
def bar(func):
    def wrapper3():
        print "bar"
        return func()
    return wrapper3

@bar
def foo():
    print "foo1"

print foo.__name__
#输出: wrapper

# "functools" 将有所帮助
print "******************************************"
import functools

def bar(func):
    # 我们所说的"wrapper",正在包装 "func",
    # 好戏开始了
    # wrapper2 = functools.wraps(func)(wrapper2)
    @functools.wraps(func)
    def wrapper2():
        print "bar"
        print "2111"+func.__name__
        return func()
    print "dfdg"
    print func.__name__
    print func
    print wrapper2.__name__
    return wrapper2

@bar
def foo2():
    print "foo3"

print foo2.__name__
print foo2()
#输出:
# foo2
# bar
# foo2
# None

def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print "---------------------------------------------"
print reverse_string("Able was I ere I saw Elba")
print "---------------------------------------------"
print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!")
print "---------------------------------------------"
print reverse_string("safsf")

print "****************2017-4-27*******************"
import sys
def propget(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(func, doc=func.__doc__)
    else:
          doc = prop.__doc__ or func.__doc__
          prop = property(func, prop.fset, prop.fdel, doc)
    return prop

def propset(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(prop.fget, func, prop.fdel, doc)
    return prop

class Example(object):
    #_half = 5
    @property
    def myattr(self):
        return self._half * 2

    @myattr.setter
    def myattr(self, value):
        self._half = value / 2

    @myattr.deleter
    def myattr(self):
        del self._half


e = Example()
e.myattr = 9
print e.myattr
e.myattr = 3
print e.myattr
e = Example()
e.myattr = 9
print e.myattr
e.myattr = 3
print e.__delattr__("_half")


import math


class Vector(object):
    def __init__(self, angle_rad):
        self.set_angle_rad(angle_rad)

    def get_angle_rad(self):
        return math.radians(self._angle_deg)

    def set_angle_rad(self, angle_rad):
        self._angle_deg = math.degrees(angle_rad)

    angle = property(get_angle_rad, set_angle_rad)

    @property
    def angle_deg(self):
        return self._angle_deg

    @angle_deg.setter
    def angle_deg(self, angle_deg):
        self._angle_deg = angle_deg

    # angle_deg = property(get_angle_deg, set_angle_deg)


v = Vector(2*math.pi)
print v.angle
print v.angle_deg

v.angle = math.pi
print v.angle
print v.angle_deg