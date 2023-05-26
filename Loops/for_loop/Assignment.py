# python program to print numbers from 0 to 6 except 3 and 6

# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# fibonacci series between 0 and 50

a = 0
b = 1
for i in range(10):
    print(a)
    a, b = b, a + b

# program to print multiplication table of given number

# n = int(input("enter number:"))
# for i in range(1, 11):
#     print(i, "*", n, "=", i*n)

# Display numbers from -10 to -1 using for loop

# for i in range(-10, 0):
#     print(i, end=" ")

# prime numbers within a range

# start = int(input("enter starting number:"))
# end = int(input("enter the ending number:"))
# for j in range(start, end+1):
#     if j > 1:
#         for i in range(2, j):
#             if j % i == 0:
#                 break
#         else:
#             print(j, end=" ")


"""fibonacci sequence"""
x = int(input('enter the number:'))

first = 0
second = 1

for i in range(x):
    print(first)
    sum_ = first + second
    first, second = second, sum_
