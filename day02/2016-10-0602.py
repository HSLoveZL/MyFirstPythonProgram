def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print fac(5)


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


def power_1(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

print power(3, 4)
print power_1(3, 3)

