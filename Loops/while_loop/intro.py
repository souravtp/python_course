"""
To repeat a block of code as long as the condition is true.
while condition:
    statement

"""

# num = int(input("enter the number:"))
# i = 1
# sum_1 = 0
# while i <= num:
#     sum_1 += i
#     i += 1
# print(sum_1)

# num = int(input("enter the number:"))
# i = 2
# while i <= num:
#     print(i)
#     i += 2

num = int(input("enter the number:"))
while num > 0 and num %2 == 0:
    print(num, "is even")
    break
else:
    print("odd")

