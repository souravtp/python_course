list1 = [1, 4, 13, 75, 14, 28, 46, 52, 19]
list2 = [3, 14, 25, 47, 38, 52, 19, 77, 95]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)