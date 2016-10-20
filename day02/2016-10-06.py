def story(**kwds):
    return 'Once upon a time, there is a '\
            '%(job)s called %(name)s. ' % kwds


def power(x, y, *other):
    if other:
        print 'Received redundant parameters:', other
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitate range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print story(job='King', name='HongShuai')

print power(2,2, 'Hello,World!')

print interval(10)
