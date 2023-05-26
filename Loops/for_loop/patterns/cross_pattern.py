num = int(input("enter number:"))
for i in range(num):
    for j in range(0, i):
        print(" ", end="")
    for k in range(0, num):
        if k == 0 or k == num - i - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
for p in range(0, num - 1):
    for q in range(num - p - 2):
        print(" ", end="")
    for r in range(0, num + 2):
        if r == 0 or r == p + 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()


# num = int(input("enter the number:"))
# for i in range(0, num):
#     for j in range(0, num):
#             if i == j or i + j == num-1:
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#     print()
