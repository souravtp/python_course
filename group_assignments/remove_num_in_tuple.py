T1 = (1, 14, 18, 24, 23, 35, 40, 56, 77, 65, 98)
print(T1)
x = int(input("enter the number to be removed from tuple:"))
L1 = list(T1)
if x in L1:
    L1.remove(x)
else:
    print("The number is not in the list")
print(tuple(L1))