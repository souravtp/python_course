# sum and product of items in a dictionary
dict1 = {1: "a", 2: "b", 3: "c", 4: "d"}
sum1 = 0
prod = 1
for i in dict1:
    sum1 += i
    prod *= i
print(f'the sum of all elements in the dictionary: {sum1}')
print(f'the product of all items in the dictionary:{prod}')

# sort dictionary by key
dict2 = {"apple": 5, "orange": 10, "banana": 7, "grapes": 13}
sorted_dict = dict(sorted(dict2.items()))
print(sorted_dict)

# pgm to check if a dictionary is empty or not
dict3 = {"a": 1, "b":2, "c": 3}
if len(dict3) == 0:
    print(f'the dictionary is empty.')
else:
    print(f'the dictionary is not empty.')

# convert a list to a nested dictionary.
list1 = ["a", "b", "c", "d", "e", "f"]
my_dict = {}
current_dict = my_dict  # current_dict = {}
for i in list1:
    current_dict[i] = {}  # current_dict = {'a':}{}
    current_dict = current_dict[i]  # current_dict = {}, which is the value of key 'a'.
print(my_dict)
