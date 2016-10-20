#
# name = raw_input('my name is:')
# print name
#
print "Hello,World!"
print 'This is my First PythonProgram'


def print_params_2(title, *params):
    print title
    print params
# print_params_2('parpams:', 1,2,3)
print_params_2('Nothing:')


def print_params_3(x,y,z=3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar
print_params_3(1, 2, 3, 4, 5, 6, 7, foo=1, bar=2)
print_params_3(1,4)
