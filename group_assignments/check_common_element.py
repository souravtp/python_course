# True if at least one common element
lst1 = [1, "apple", "orange", 24, "honda", "bmw"]
lst2 = ["banana", "pineapple", 55, 41, "mercedes", "honda"]
condition = False
for i in lst1:
    if i in lst2:
        condition = True
print(condition)

