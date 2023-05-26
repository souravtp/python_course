"""

1. Mutable and Immutable
2. Multiple datatypes
3. Unordered
4. Not indexed
5. No duplicates allowed

"""

set1 = {1, 2, 3, "apple", 4, 5}
print(set1)
print(3 in set1)


# empty set
set2 = set()
set3 = {}  # this will create an empty dictionary


# add()
set1.add("Hello")
print(set1)


# update()
set4 = {10, 25, 33, "orange"}
set4.update(set1)
print(set4)
set5 = {"bmw", "vw", "nissan"}
list1 = ["car", "scooter", "jeep", 4, 12, 25]
set5.update(list1)
print(set5)


# remove()
set6 = {"hello", 1, 2, 3, 4, "car", "bus", "lorry"}
set6.remove(1)
# set6.remove("python")  # this method will give 'key error' if an element which is not in set is entered.
print(set6)


# discard()
set6.discard("car")
print(set6)
set6.discard("python")  # discard will not raise error when the element is not present in the set.


#  pop()
print(set6.pop())  # this removes a random item from the set. this gives the removed item


# clear()
set7 = {1, 3, 5, 7, 9}
set7.clear()  # remove all elements from the set. Empty set remains
print(set7)


# del()
set8 = {5, 10, 15, 20, 25}
del set8  # deletes entire set
# print(set8)  # this will give error

# frozenset()
# list1 = [1, 2, 3, 4]
# fl = frozenset(list1)
# print(fl)
#
# dict1 = {"a": 1, "b": 2}
# fd = frozenset(dict1)  # here only keys will be added to frozenset
# print(fd)
#
# str1 = "Hello"
# fs = frozenset(str1)
# print(fs)
#
# for i in fl:
#     print(i)