"""
function
--------
It is a block of code which is executed when it is called. There are 3 types of functions.
1. User defined
2. Built in
3. Lambda
"""


# def test_fun():
#     print("hello world")


# test_fun()

# c = 25  # these are called global variables
# d = 35


# def sum1():
#     a = 10  # these are called local variables
#     b = 15
#     print(a+b)
#     print(c+d)


# sum1()


# def sum2(x, y):  # variables giving at the time of definition are called parameters
#     print(x+y)


# sum2(50, 55)  # the values given at the time of function invocation is called arguments


# def sum3(p, q):
#     r = p+q
#     return r  # which returns to r


# print(sum3(10, 20))


# def sum4(f, g):
#     h = f+g  # if there is no return statement then output of function will be None value


# print(sum4(5, 6))


# def calc(m, n):
#     s = m+n
#     t = m*n
#     return s, t  # this gives output as a tuple


# print(calc(5, 10))


# Arbitrary arguments
# def say_hi(*names):  # If we put * before parameter, the function can accept any number of arguments
#     return f'Hi, {names}'
#
#
# print(say_hi('messi', 'ronaldo', 'neymar'))


# Keyword arguments
# def name_fun(elder, middle, younger):
#     return f'elder is {elder}, middle is {middle}, younger is {younger}'
#
#
# print(name_fun('ronaldo', 'messi', 'neymar'))  # this method of giving arguments is called positional arguments
# # the arguments are given in the order of parameters. these arguments are passed to corresponding parameters.
#
# print(name_fun(elder='ronaldo', middle='messi', younger='neymar'))  # this method of giving arguments is called
# # keyword arguments. in this method, parameters are mentioned at the time of invocation.
#
# print(name_fun('ronaldo', younger='messi', middle='neymar'))  # we can mix keyword and positional arguments.
# # one rule is that positional arguments should come first. Here ronaldo is given as positional argument.
#
# # print(name_fun(elder='ronaldo', 'messi', 'neymar'))  # here we have given keyword argument first.
# # It will give an error.


# arbitrary keyword arguments
# def function_1(**employee):  # this will take any number of keyword arguments. and is stored in dictionary format.
#     print("last name2 is "+employee["name2"])  # the dictionary is named 'employee'.
#
#
# function_1(name2='sourav', dept='python', id=52, salary=754000)


# default value
# def my_country(country = "Norway"):
#     return f'I am from {country}'
#
# print(my_country())
# print(my_country(Sweden))


# def food_items(food):
#     for i in food:
#         print(i)  # if we put return instead of print only first element will be printed.
#
#
# # food_items(['chapati', 'dosa', 'biriyani', 'rice'])
# beverages = ['tea', 'coffee', 'water', 'coke']
# food_items(beverages)
