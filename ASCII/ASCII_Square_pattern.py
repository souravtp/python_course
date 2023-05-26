rows = int(input("enter rows:"))
num = 65
for i in range(0, rows):
    for j in range(0, rows):
        print(chr(num), end=" ")
        num += 1
    print()
