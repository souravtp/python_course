# alphabets

"""
A=65
Z=90
chr() to convert num to alphabets

a=97
z=122
"""

# for i in range(65, 90):
#     print(chr(i), end=" ")

# for j in range(97, 123):
#     print(chr(j), end=" ")

# rows = int(input("enter the rows:"))
# A = 65
# for i in range(0, rows):
#     for j in range(0, i+1):
#         print(chr(A), end=" ")
#         A += 1
#     print()

import string
for i in string.ascii_uppercase:
    print(i, end="")

for i in string.ascii_lowercase:
    print(i, end="")