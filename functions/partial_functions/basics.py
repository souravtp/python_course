from functools import partial


def multiply(x, y):
    return x * y


dbl = partial(multiply, 2)
print(dbl(5))
trp = partial(multiply, 3)
print(trp(5))


def ran(y):
    return lambda x: x+10


ran(5)