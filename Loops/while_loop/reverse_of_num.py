# num = int(input("enter the number:"))
# num_str = str(num)
# i = 1
# while i <= len(num_str):
#     print(num_str[-i], end="")
#     i += 1


num = int(input("enter the number:"))
num_str = str(num)
i = 1
while i <= len(num_str):
    r = num % (10**i)
    s = r // (10**(i-1))
    print(s, end="")
    i += 1
