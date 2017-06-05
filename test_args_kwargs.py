def print_three_things(a,b,c):
    print 'a={0},b={1},c={2}'.format(a,b,c)

mylist=['aaa','ccc','sdfs']
print_three_things(*mylist)
