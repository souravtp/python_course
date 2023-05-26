import random

"""pgm to print a random color hex"""

# list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
# hex_code = ""
# for i in range(6):
#     x = random.choice(list1)
#     hex_code += x
# print("#" + hex_code)

# or
n = random.randrange(0, 16777215)
x = str(hex(n))
hex_code = "#" + x[2:]
print(hex_code)


"""a random alphabetical string"""
# s = "python"
# str1 = ""
# for i in s*2:
#     str1 = str1+random.choice(s)
# print(str1)

"""multiple of 7 between 0 and 70"""
# print(random.randint(0, 10)*7)

"""random value between two strings"""
