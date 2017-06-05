class My_Singleton(object):
    da = 'fd'

    def __init__(self, a):
        self.da = a

    def foo(self):
        print "asdad"

my_singleton = My_Singleton(23)