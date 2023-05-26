# list1 = [2, 5, 6, 15, 17, 34, 37, 66, 54]
# even = []
# odd = []
# for i in list1:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(odd, even, sep='\n')

"""using list comprehension"""
# list = [(i,"even" if i%2 == 0 else "odd") for i in list1]
# print(list)

# fruits = ["apple", "orange", "banana", "kiwi", "coconut"]
# newlist = [x for x in fruits if "a" not in x]
# print(newlist)


"""to make a list of prime numbers from a given list"""

# number = [1, 5, 7, 3, 4, 14, 9, 11]
# prime = [x for x in number if all(x % y != 0 for y in range(2,x)) and x > 1]
# print(prime)

# when we check primes we ony need to check if the number is divisible by any number from 2
# to the square root of that number. So, we can check till range(2, int(x**0.5)+1)

# prime = [x for x in number if all(x % y != 0 for y in range(2, int(x**0.5)+1)) and x > 1]

"""prime numbers between 0 and 100"""
# primes = [i for i in range(0, 100) if all(i % j != 0 for j in range(2, i)) and i > 1]
# print(primes)

"""all numbers from 1 to 1000 divisible by 7"""
# div_by_seven = [x for x in range(1, 1001) if x % 7 == 0]
# print(div_by_seven)

"""numbers from 1 to 1000 that have a 3 in them"""
# num_with_three = [x for x in range(1, 1000) if '3' in str(x)]
# print(num_with_three)

"""count number of spaces in a string"""
# sample_str = "The quick brown fox jumps over the lazy dog."
# spaces = [s for s in sample_str if s == " "]
# print(len(spaces))

"""Create a list of all the consonants in the string"""
# str1 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# consonant_list = [i for i in str1 if i not in ('a', 'e', 'i', 'o', 'u', ' ')]
# print(consonant_list)
# str2 = ''.join(consonant_list)
# print(str2)

"""Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
 Result would look like (index, value), (index, value)"""

# list_a = ["hi", 4, 8.99, 'apple', ('t,b', 'n')]
# new_list = enumerate([x for x in list_a])
# print(tuple(new_list))

# or

# new_list2 = [(index, item) for index, item in enumerate(list_a)]
# print(new_list2)

"""Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5"""
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# common_list = [x for x in list_a if x in list_b]
# print(common_list)

"""Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over
 1000 people attending’"""
# str1 = "In 1984 there were 13 instances of a protest with over 1000 people attending"
# numbers = [i for i in str1 if i.isnumeric()]
# print(numbers)

"""pgm to print all numbers which are divisible by 2 and 5 from 0 to 100"""
list_a = [x for x in range(101) if x % 2 == 0 and x % 5 == 0]
print(list_a)

