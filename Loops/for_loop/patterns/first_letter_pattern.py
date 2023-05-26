rows = int(input("enter rows:"))
for i in range(rows):
    if i == 0 or i == rows//2 or i == rows-1:
        for j in range(1):
            print(" ", end="")
        for k in range(rows-2):
            print("* ", end="")
        print()
    elif i < rows//2:
        print("*")
    else:
        for l in range(rows-2):
            print("  ", end="")
        print("*", end="")
        print()
