"""
syntax:
lambda arguments: expression
it can contain any number of arguments but only one expression.
"""
import datetime

# x = lambda a: a + 10
# print(x(5))

# y = lambda x, y: x + y
# print(y(5, 6))

# z = lambda a, b, c: a+b+c
# print(z(10, 5, 20))

"""lambda inside another function"""
# def myfun(n):
#     return lambda a: a*n
#
#
# doubler = myfun(2)  # here myfun(2) is assigned to a variable. the variable 'doubler' is now equal to
# # lambda a:a*2. Now if we call doubler(5) the lambda function returns double of the number.
# print(doubler(11))

# tripler = myfun(3)
# print(tripler(10))

"""without arguments"""
# x = lambda: print("Hello, World!")
# x()

"""sorting list of tuples"""
# fruits = [("apple", 5), ("mango", 10), ("guava", 15), ("jackfruit", 20), ("kiwi", 25)]
# fruits.sort(key=lambda a: a[0])
# print(fruits)

"""sort a list of dictionaries using lambda"""
marks = [
    {"English": 75, "Maths": 65, "Science": 70},
    {"English": 85, "Maths": 65, "Science": 70},
    {"English": 60, "Maths": 65, "Science": 70}
]

sorted_eng_marks = sorted(marks, key=lambda x: x["English"])

print(sorted_eng_marks)

"""to extract month, date, time using lambda"""
now = datetime.datetime.now()

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()

print(year(now))
print(month(now))
print(day(now))
print(time(now))


def current_year(x):
    return x.year


print(current_year(now))

"""consider this example"""


def outer_adder(x):
    def inner_adder(y, z):
        return x + y + z

    return inner_adder


a = outer_adder(5)  # when we assign outer_adder to 'a', we are creating a function 'a', which is inner_adder().
print(a(10, 15))  # now we're calling 'a'. which indeed inner_adder.
# print(outer_adder(5))


"""to check if the given string is number or not"""
is_num = lambda q: q.replace('.', '', 1).isdigit()

print(is_num('5515'))
print(is_num('hello'))
print(is_num('5.1234'))
