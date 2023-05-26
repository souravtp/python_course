"""
to store multiple items in a single datatype

1. Immutable
2. Ordered
3. Indexed
4. Allows multiple datatypes

"""

tup1 = ("cars", "fruits", 1, 5, True, ["bmw", "vw", "suzuki", 9], ("mango", "apple", "orange"))

# print(tup1)
# print(tup1[1:4])
# print(len(tup1))
# print(type(tup1))
# print(tup1[-1])
# print(tup1[5][3])

list1 = list(tup1)
# print(list1)
# list1.remove("fruits")
# print(list1)
# tup2 = tuple(list1)
# print(tup2)
# print(tup2.count("cars"))

# print(list1[5][2])

# reverse
tup2 = ("suzuki", "honda", "toyota", "bmw", "vw")
# list2 = list(tup2)
# list2.reverse()
# tup3 = tuple(list2)
# print(tup3)
#
# tup4 = tup2[::-1]
# print(tup4)
#
# tuple1 = ("apple", [10, 20, 30], (5, 12, 25))
# print(tuple1[1][1])
#
# tuple2 = (11, 22)
# tuple3 = (10, 40)
# tuple2, tuple3 = tuple3, tuple2
# print(tuple2, tuple3, sep="\n")
