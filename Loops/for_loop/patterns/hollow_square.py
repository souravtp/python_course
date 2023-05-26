rows = int(input("enter rows:"))
# for i in range(rows):
#     for j in range(rows):
#         if i == 0 or i == rows-1:
#             print("* ", end="")
#         elif j == 0 or j == rows-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


for i in range(0, rows):
    for j in range(0, rows):
        if i == 0 or i == rows-1 or j == 0 or j == rows-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
