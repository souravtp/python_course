# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner  # if we put 'inner' only without parenthesis it returns a function, which can be assigned
#     # to any other variable,and that variable can be used as a function. 'refer nested_functions.py'
#     # for more details. Here we called the argument as func(). So the argument can only be a function. Otherwise,
#     # it will give error. If we give integer as argument the line 4 will not be valid.

# we are defining the function to be called as an argument of above function


# def ordinary():
#     print("I am ordinary")
#
#
# # decorating ordinary function
#
# decorated_func = make_pretty(ordinary)  # we should not type 'ordinary()' here. then the result of the 'ordinary'
# # function('I am ordinary') will be passed as argument for make_pretty function. which is a string, Which results in
# # error in line 4, because we are trying to call a function there. Instead, we got a string.
#
# # calling decorated function
#
# decorated_func()


# @make_pretty
# def ordinary():
#     print("I am ordinary")


# ordinary()  # this calls the 'inner' function of decorator.


# # Another example
#
# def upper_decor(fun):
#     def wrapper(name2):
#         result = fun(name2)
#         return result.upper()
#     return wrapper
#
#
# @upper_decor
# def hello_name(name2):
#     return 'hello '+name2
#
#
# print(hello_name("messi"))


def add(x, y):
    return x+y


def calculate(fun, x, y):
    return fun(x, y)


result = calculate(add, 4, 8)
print(result)
