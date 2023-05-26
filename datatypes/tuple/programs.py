"""
WAP to check whether an element exist within a tuple
tuple1 = ("apple", "orange", (10, 20, 30), ["car", "bus", "lorry"], 50, 45)

"""

# tuple1 = ("apple", "orange", (10, 20, 30), ["car", "bus", "lorry"], 50)
# x = input("enter the value:")
# if x in tuple1:
#     print(True)

# convert tuple to string
tuple2 = ("p", "y", "t", "h", "o", "n")
# tuple3 = "".join(tuple2)
# print(tuple3)
# T = ()
# for elem in tuple2:
#     x = (tuple2.index(elem), elem)
#     T += (x,)
# print(T)

# enumerate() function

# y = enumerate(tuple2)
# print(y)
# print(list(y))
# print(tuple(y))

# T2 = (("A", "B"), ("a", "b"))
# for i, elem in enumerate(T2):
#     print(i, elem)
#
# print(type(enumerate(T2)))


# all() function
# T3 = (0, 1, "Hello")
# print(all(T3))
# T4 = (False, "Apple", 15, 20)
# print(all(T4))


# any() function
# T5 = ("orange", "kiwi", "cherry")
# print(any(T5))
# T6 = (0, False, 00)
# print(any(T6))
# T7 = (0, False, 00, 1)
# print(any(T7))


# max() and min()
T8 = ("banana", "coconut", "onion", "tomato", "Tomato")
print(max(T8))  # based on the ascii values of the first letter
print(min(T8))

T9 = (1, 5, 45, 17, 64, 27)
print(max(T9))
print(min(T9))
