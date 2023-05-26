from numpy import *

arr = array('i', [1, 2, 3, 4, 5])

# traverse of array
for i in arr:
    print(i)

# inserting an element in array
arr.insert(2, 10)
print(arr)

# deleting an element
arr.remove(3)
print(arr)

# delete element from a position
arr.pop(3)
print(arr)
