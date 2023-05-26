num = int(input("enter the number:"))
for i in range(1, 2*num):
    for j in range(1, 2*num):
        if (i == j and i <= num):
            print(i, end="")
        elif i + j == 2*num and i <= num:
            print(i, end="")
        elif i == j and i > num:
            print(2*num-j, end="")
        elif i + j == 2*num and i > num:
            print(j, end="")
        else:
            print(" ", end="")
    print()
