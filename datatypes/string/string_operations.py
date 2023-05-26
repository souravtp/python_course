x = "  Abc Def gh "

# indexing string[start:stop:step]
# print(x[1::])
# print(x[::1])
# print(x[::2])
# print(x[-2:-6])
#
# print(x.upper())
# print(x.lower())
# print(x.capitalize())
# print(x.find("Def"))
# print(x.strip())  # removes whitespace from start and end
# print(x.replace("b", "c"))

# a = "Hello, world"
# print(a.split(","))  # makes a list with elements
#                     # separated by the given argument.
# print(a.count("l"))
# print(a.count("Hello"))
# print(a.index("w"))  # same as find(). find returns -1 if
#                     # the value is not there.
#
# b = "Company12"
# print(b.isalnum())  # True if alphabet and string are there
# print(b.isalpha())
# print(b.isdecimal())

"""replace()"""
# c = "Helloo Woorld"
# d = ""
# print(c.replace("o", "a"))
# print(c.replace("o", "a", 1))
# print(c.replace("o", "a", 3))  # third argument gives the number of letters to be replaced.
# print(c.replace("Helloo", "Hello"))
# print(c.replace("", "a"))  # Here in the ends and in between objects the letter is got added.
# print(d.replace("", "a"))


# join()
# lst = ["apple", "orange", "banana"]
# x = " ".join(lst)
# print(x)
# type(x)
# y = "#".join(lst)
# print(y)


# split()
# str1 = "Hel.lowo.rld"
# lst1 = str1.split(".")
# print(lst1)
# str2 = "Hello world"
# lst2 = str2.split()
# print(lst2)
print("phi       chi\npsi".split())


# find()
# str1 = "kappa"
# str1.find('a')
"""
find() function returns the index position of searched value. Only single index will be returned.
if value repeats then the index of first value will be given out. if there is no value output will be -1.
"""
# print(str1.find('a', 2))
"""
the second argument is used to search from that index position. here search start from
index position 2. ie, str1[2]. the searched letter before that index will not be searched.
"""

# my_string = "hello world"
# substring = "o"
# start_index = 3
# end_index = 8

# result = my_string.find(substring, start_index, end_index)

# print(result)
"""The third index is the search end range. which is excluded from search.
Search start index is included in the search"""


# lstrip()
# print("pythoninstitute.org".lstrip(".org"))  # since there is no .org in left side of string, the output is same.
# print("www.cisco.com".lstrip("w."))  # this will remove all w's and .'s from left side of string.
# print("www.google.com".lstrip("w"))  # this will remove w's from left side.
# print("www.google.com".lstrip("."))  # this will do nothing. Just print the string. because the argument is not on
# the left side of the string.

# rstrip()
# print("[" + " upsilon ".rstrip() + "]")
# print("cisco.com".rstrip(".com"))


# rfind()
# print("tau tau tau".rfind("ta"))  # returns index of searched string. search starts from right side.
# print("tau tau tau".rfind("ta", 9))  # Second argument is index to start search from.
# print("tau tau tau".rfind("ta", 3, 9))  # here right search starts from index 3 to 8. returns rightmost index where
# searched value exists. Since index is till 8, the last 'a' will not be considered. so returns index of 'ta' in the
# middle tau which is 4.

# print("tau tau tau".rfind("ta", 3, 10))  # here rightmost 'a' is included. So, it returns index of last 'ta'. which
# is 8.


# starts_with()
# print("omega".starts_with("meg"))
# print("omega".starts_with("om"))
#
# print()


# swapcase()
# # swaps cases of all characters. All other characters remain untouched.
# print("I know that I know nothing.".swapcase())
#
# print()


# title()
# print("I know that I know nothing. Part 1.".title())
#
# print()
