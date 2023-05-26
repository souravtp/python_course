# largest number in a list
lst1 = [1, 5, 81, 4, 12, 47, 52, 31, 84, 17, 19]
largest = 0
for i in lst1:
    if i > largest:
        largest = i
print(largest)
