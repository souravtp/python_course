# count unique values inside a list
lst1 = ["apple", "orange", "banana", "banana", "grapes", "orange"]
new_lst = []
for elem in lst1:
    if elem not in new_lst:
        new_lst.append(elem)
print(len(new_lst))
