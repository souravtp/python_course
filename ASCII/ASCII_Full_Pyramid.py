rows = int(input("enter rows:"))
A = 65
for i in range(0, rows):
    for j in range(0, rows-i-1):
        print(" ", end="")
    for k in range(0, i+1):
        print(chr(A), end=" ")
        A += 1
    print()
