import PyV8


class Test():
    def js(self):
        ctxt = PyV8.JSContext()
        ctxt.enter()

        func = ctxt.eval("(function(){return '###'})")
        print func()
        print 'sdad'


if __name__ == '__main__':
    crawler = Test()

    crawler.js()
