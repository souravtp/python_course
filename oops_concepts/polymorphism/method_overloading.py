"""Method overloading allows a single class to have multiple methods with the same name2,
but with different parameters. This allows objects of the same class to be used in different contexts,
depending on the parameters passed to the method."""

"""Python does not support method overloading in the traditional sense as in other languages like Java.
 In Python, you can define multiple functions with the same name2 but with a different number of arguments
or argument types. This is known as function overloading.
However, only the latest defined function with that name2 will be used. So, it is not true overloading"""


class Math:

    def add(self, x, y):
        return x + y

    def add(self, x, y, z):  # here we have redefined the add function with three arguments. so the first add function
        # will not work when called. It will ask for three arguments.
        return x + y + z


obj = Math()
# print(obj.add(5, 10))  # this giving TypeError because we have given only two arguments.
print(obj.add(5, 10, 15))

"""we can make python support overloading by using default argument passing"""


class A:
    def find_sum(self, a, b, c=None):
        if c == None:
            return a + b
        else:
            return a + b + c


obj2 = A()
print(obj2.find_sum(5, 10))  # here c is takes the default value None.
print(obj2.find_sum(8, 12, 20))
