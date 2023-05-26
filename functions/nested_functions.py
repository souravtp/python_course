def outer_fun(num):
    def inner_fun():
        return num+1
    return inner_fun()


print(outer_fun(5))


def outer_fun(num):
    def inner_fun():
        def innermost_fun():
            return num+1
        return innermost_fun()
    return inner_fun()


print(outer_fun(5))


def outer(name):
    def inner():
        return "hello " + name
    return inner  # here we have returned the function itself. not its result. we can now assign this function to
# a variable and use that variable as a function.


x = outer('sourav')
print(x())


# If we put return inner(), it will return the result of the function. which we cannot pass to another variable and
# use it as a function
def out(name):
    def inn():
        return "Hello " + name
    return inn()


x = out('john')  #Here x is assigned with the string output of the function. Not the function itself. So we cannot
# call x().
print(out('john'))