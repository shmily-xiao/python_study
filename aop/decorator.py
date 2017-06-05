def method_friendly_decorator(method_to_decorate):
    def wrapper(*args, **kwargs):
        args[1] = args[1] - 3
        return method_to_decorate(args, kwargs)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)

l = Lucy()
l.sayYourAge(-3)