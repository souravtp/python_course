"""
Lists
-----
Mutable, ordered, indexed, allow duplicates

items = ["apple", 5.4, "Orange", 10, True]
"""

items = ["apple", 5.4, "Orange", 10, True]
# str1 = "World"
# lst1 = list(str1)
# print(lst1)
#
# print(items[:2])
# print(items[1:4:-1])
# print(items[4:1:-1])
# print(items[4:1])
# print(items[::-1])
# print(items[-4:-1])  # in negative indexing values should be given in left to right order
# print(items[-4:-1:1])
# print(items[-4:-1:-1])
# print(items[-1:-4])
# print(items[-1:-4:1])
# print(items[-1:-4:-1])

# append
# items.append("mango")
# print(items)
# items.append([9.6, "banana"])
# print(items)

# extend
# lst2 = ["suzuki", "hyundai", "honda"]
# items.extend(lst2)
# print(items)

# pop()
# lst2 = ["messi", "neymar", "ronaldo", "haaland", "mbappe"]
# lst2.insert(1, "pele")
# print(lst2)
# lst2.pop(3)  # pops out 3rd element
# print(lst2)
# lst2.pop()  # pops out last element
# print(lst2)

# lst2.sort()
# print(lst2)
# lst2.sort(reverse=True)
# print(lst2)

# lst3 = [3, 5, 7, 2, 1, 6, 4]
# lst3.sort()
# print(lst3)

x = "1,3,5,6,8"
list1 = x.split(",")
print(list1)
