"""reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting
with an initial argument. It has the following syntax:
reduce(func, iterable[, initial])

the 'reduce function' will cumulatively apply the elements of iterable into the function that we have provided
as argument. If a function defined f(x, y) = x+y, when we add this function into reduce, along with an iterable,
reduce takes first and second element of iterable and give it to x and y respectively. after finding the result, 'x+y'
this result is provided as first argument(x) and the third element taken as second argument(y). If the optional
argument 'initial' is provided
"""


from functools import reduce


"""factorial of numbers"""


def fact(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(fact(5))
fact(1)  # here the range is [1]. in this case the reduce function will not apply the value to lambda function
# because there is only a single value which is not sufficient for lambda arguments. So, it returns that range value 1.
nums = [1, 2, 3, 4, 5, 6]
factorials = list(map(fact, nums))
print(factorials)


