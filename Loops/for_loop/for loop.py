"""
for loop
--------
Used to iterate over a sequence

syntax
------
for value in sequence:
    print(sequence(value))

"""

# for i in "hello":
#     print(i)
#
# fruits = ["apple", "orange", "banana", "pineapple"]
# for i in fruits[0]:
#     print(i)

# for i in range(2, 11, 2):
#     print(i)

# for reverse order

# for i in range(10,0,-2):
#     print(i, end=",")

# for i in range(9, 0, -2):
#     print(i, end=",")

# to calculate the sum of n natural numbers

# n = int(input("enter your number:"))
# if n > 0:
#     sum_ = n*(n+1)/2
#     print("the sum of first", n, "natural numbers is", sum_)
# else:
#     print("no value")

#sum of natural numbers

# num = int(input("enter number:"))
# sum = 0
# for i in range(1,num+1):
#     sum += i
# print(sum)

# break continue and pass

# for i in range(2, 3):
#     print(i)
#     if i == 5:
#         continue


# n=int(input("enter num:"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c==2:
#     print("prime")
# else:
#     print("not prime")


# num=int(input("enter number:"))
# OP = num % 10
# for i in range(1,len(str(num))):
#    NP=num//10*i
#    OP*=NP
# print(OP)