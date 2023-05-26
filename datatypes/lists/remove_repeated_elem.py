list1 = ["apple", "orange", "banana", "pineapple", "orange", "banana", "coconut", "pear"]
new_list = []
for elem in list1:
    if elem not in new_list:
        new_list.append(elem)
print(new_list)
