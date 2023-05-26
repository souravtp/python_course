num = int(input("enter the number:"))
for i in range(0, num):
    for j in range(num-i, 0, -1):
        print(j, end=" ")
    print()


rows = int(input("enter the number:"))
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
