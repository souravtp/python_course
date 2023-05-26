name = "John"
age = 32
print("%s is %d years old" % (name, age))  # here we cannot interchange the arguments.
# %s denotes string and %d denotes integers.
print("{} is {} years old".format(name, age))  # here we can interchange the arguments.
# arguments are printed according to the order.
print(f'{name} is {age} years old')  # fstring

baskets = 10
apples_in_basket = 12
print(f'there are {apples_in_basket * baskets} apples')
