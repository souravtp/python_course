num = int(input("enter the number:"))
for i in range(0, num//2):
    if i < num//5:
        continue
    else:
        for j in range(num//2-i-1):
            print("  ", end="")
        for k in range(0, 2*i+1):
            print("* ", end="")
        for l in range(num-2*i-1):
            print("  ", end="")
        for m in range(0, 2*i+1):
            print("* ", end="")
        print()
for p in range(num, 0, -1):
    for q in range(num-p):
        print("  ", end="")
    for r in range(2*p-1):
        print("* ", end="")
    print()
