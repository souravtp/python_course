num = int(input("enter number:"))
for i in range(0, num):#3
    for j in range(num-i-1):#5-1-1
        print(" ", end="")
    for k in range(0, i+1):#0,3
        if k == 0 or k == i:#1
            print("* ", end="")
        else:
            print("  ", end="")
    print()
for p in range(0, num-1):#0,4
    for q in range(0, p+1):#0,1
        print(" ", end="")
    for r in range(0, num-p):#0,5
        if r == 0 or r == num-p-2:#
            print("* ",  end="")
        else:
            print("  ", end="")
    print()
