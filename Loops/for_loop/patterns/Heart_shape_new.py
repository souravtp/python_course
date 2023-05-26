rows = int(input("enter the number:"))
# for i in range(1, rows+1):
#     for j in range(rows-i):
#         print("  ", end="")
#     for k in range(0, 2*i-1):
#         print("* ", end="")
#     print()


for p in range(rows//2 - 1, -1, -1):
    if p > rows//5:
        continue
    else:
        for q in range(p):
            print("  ", end="")
        for r in range(1, rows-2*p):
            print("* ", end="")
        for s in range(2*p+1):
            print("  ", end="")
        for t in range(1, rows-2*p):
            print("* ", end="")
        print()
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print("  ", end="")
    for k in range(0, 2 * i - 1):
        print("* ", end="")
    print()
