"""1.program to create a lambda function that adds 15 with the entered number"""

# y = lambda x: x+15
# print(y(6))

"""2.lambda function to multiply two numbers given as arguments"""

# z = lambda a, b: a*b
# print(z(5, 4))

"""3.pgm to create a function that takes one argument and that argument id multiplied with ab unknown given number"""


def adder(n):
    return lambda x: x*n


a = adder(5)
print(a(7))


"""4.python program to sort a list of tuples using lambda"""

fruits = [("mango", 5), ("apple", 8), ('orange', 12), ("banana", 7), ("grapes", 17)]
fruits.sort(key=lambda x: x[1])  # sort based on x, here x is the tuple inside the list.
print(fruits)

"""5. separate even numbers from a list"""
nums = [2, 15, 14, 98, 75, 32, 45, 65, 73, 59, 44, 68]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

"""pgm to square and cube every number in a given list of integers"""
nums2 = [1, 2, 3, 4, 5, 6]

sqr = list(map(lambda x: x**2, nums2))
cubes = list(map(lambda x: x**3, nums2))

print(sqr)
print(cubes)

"""pgm to find whether the given string starts with the given character"""

starts_with = lambda x: True if x.startswith('P') else False

print(starts_with('Python'))
print(starts_with('Java'))


"""to find intersection of two arrays"""

arr1 = [1, 5, 8, 7, 12, 35, 78, 42]
arr2 = [5, 65, 42, 69, 75, 7, 13, 55]

result = list(filter(lambda x: x in arr2, arr1))
print(result)


"""pgm to rearrange positive and negative numbers in a given array using lambda"""
lst = [5, -6, 9, 13, -78, 47, 59, 33, -96, -51]
result = sorted(lst, key=lambda x: 0 if x == 0 else -1*x)
print(result)

"""pgm to filter given list whether the values in the list are having length of 6 using lambda"""

my_list = ['apple', 'orange', 'mango', 'grapes', 'pineapple', 'kiwi', 'jackfruit']

# filtered_list = list(filter(lambda x: x if len(x)==6, my_list))
# filtered_list = list(filter(lambda x: x if len(x) == 6 else False, my_list))
filtered_list = list(filter(lambda x: len(x) == 6, my_list))
print(filtered_list)


"""pgm to find palindromes from a given list of strings"""
test_lst = ['apple', 'malayalam', 'racecar', 'elephant', 'abcba', 'water']

palindromes = list(filter(lambda s: s == s[::-1], test_lst))
print(palindromes)
