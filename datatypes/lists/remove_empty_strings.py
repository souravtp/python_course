list1 = ["John", " ", "Jack", "Emma", " ", "Jins", "Lina"]
for i in list1:
    if i.isspace():
        list1.remove(i)
print(list1)
