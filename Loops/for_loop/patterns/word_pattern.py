name = input("enter name2:")
l = len(name)
for i in range(l+1):
    for j in range(0, i):
        print(name[j], end=" ")
    print()
