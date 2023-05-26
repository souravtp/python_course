"""
syntax of a map function is
map(func, iterables)
"""


# def add(n):
#     return n+n
#
#
# nums = (2, 4, 5, 6)
#
# res = map(add, nums)
# print(list(res))


"""1.lambda function inside map function"""

nums1 = [1, 3, 4, 6, 20]
nums2 = [5, 2, 3, 8, 12]

res = map(lambda x, y: x+y, nums1, nums2)
print(list(res))
# if any iterable has extra elements, that element will be neglected.
res = map(lambda x, y: x*y, nums1, nums2)
print(list(res))


"""2.to convert list elements to upper case"""

my_pets = ['alfred', 'tabitha', 'william', 'arla']
upper_pets = []
for elem in my_pets:
    u_pet = elem.upper()
    upper_pets.append(u_pet)

print(upper_pets)

# using filter() function

upper_p = list(map(str.upper, my_pets))  # here str.upper function requires only one argument. So, we have passed one
# iterable to it. If function requires multiple arguments we have to provide that much iterables.
print(upper_p)


"""3.rounding list of elements"""

circle_areas = [3.45675, 1.0346879, 4.039863, 9.33588, 6.774586, 5.2198647]
rounded = list(map(round, circle_areas, range(1, 7)))
rounded2 = list(map(round, circle_areas, [2 for i in range(7)]))
print(rounded)
print(rounded2)


fruits = ['apple', 'orange', 'banana', 'pineapple', 'kiwi']
length = list(map(lambda x: len(x), fruits))
print(length)

