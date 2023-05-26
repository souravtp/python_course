n = int(input("enter required number of elements in the list:"))
list1 = []
for i in range(n):
    x = int(input(f'enter the list element {i+1}:'))
    list1.append(x)
neg_list = []
pos_list = []
for j in list1:
    if j < 0:
        neg_list.append(j)
    elif j == 0:
        continue
    else:
        pos_list.append(j)
print(neg_list)
print(pos_list)


# str1 = input("enter numbers separated with commas:")
# list1 = str1.split(",")
# num_list = [int(i) for i in list1]
# neg_list = []
# pos_list = []
# for j in num_list:
#     if j < 0:
#         neg_list.append(j)
#     elif j == 0:
#         continue
#     else:
#         pos_list.append(j)
# print(neg_list)
# print(pos_list)
