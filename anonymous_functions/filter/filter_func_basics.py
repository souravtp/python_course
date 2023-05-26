""" requires the function to return boolean values (true or false) and then passes each element in the
iterable through the function, "filtering" away those that are false.
syntax: filter(func, iterable)
The following points are to be noted regarding filter():

1. Unlike map(), only one iterable is required.
2. The func argument is required to return a boolean type. If it doesn't, filter simply returns
   the iterable passed to it. Also, as only one iterable is required, it's implicit that func must
   only take one argument.
3. filter passes each element in the iterable through func and returns only the ones that evaluate to true.
   I mean, it's right there in the name -- a "filter"."""

list1 = [1, 3, 5, 8, 9, 4, 2]


def func(x):
    if x > 3:
        return x


res = filter(func, list1)
print(list(res))

"""using lambda"""
res1 = filter(lambda x: x > 3, list1)
print(list(res1))


"""to print vowels in a string"""


def vowels(x):
    vow = 'aeiou'
    for i in x:
        if i in vow:
            return i


s = 'hello world'
res2 = filter(vowels, s)
print(list(res2))

vowl = 'aeiou'
res4 = list(filter(lambda x: x.lower() in vowl, s))
print(res4)

"""to find palindromes from a list"""

words = ["demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk", "malayalam"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)


