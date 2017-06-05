def A(max):
    n = 0
    while n < max:
        yield n
        # print n
        n = n+1

class B(object):
    max_num = 0
    n = 0

    def __init__(self, max_num):
        self.max_num = max_num

    def next(self):
        if self.n < self.max_num:
            temp = self.n
            self.n = self.n + 1
            return temp
        raise StopIteration()

def dict_for_map(dict):
    for (key, value) in dict:
        print (key, value)


if __name__ == '__main__':
    print A(3) # <generator object A at 0x0267A6E8>
    for i in A(3):
        print i
    # 0
    # 1
    # 2

    b = B(3)
    print b.next() # 0
    print b.next() # 1
    print b.next() # 2

    ddict={'11':'sss','22':'ggg'}
    dict_for_map(ddict.items())

    map(dict_for_map, ddict.items())


