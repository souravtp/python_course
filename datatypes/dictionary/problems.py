# 1.convert two lists into a dictionary
list1 = ["model", "company", "engine", "fuel"]
list2 = ["supra", "toyota", "2000cc", "petrol"]
# car = {}
# j = 0
# for i in list1:
#     car.setdefault(i, list2[j])
#     j += 1
# print(car)

# or
# print(dict(zip(list1, list2)))

# 2.merge two python dictionaries into one
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5}
# dict3 = dict1 | dict2  # or dict1.update(dict2)
# print(dict3)

# 3.print value of key 'history' from below dictionary
# sampledict = {
#     "class": {
#         "student": {
#             "name2": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampledict['class']['student']['marks']['history'])

# 4.Initialize dictionary with default values
# list3 = ["D1", "D2"]
# default = {"place": "abc", "phone": 45213}
# dict1 = dict.fromkeys(list3, default)
# print(dict1)

# 5.create a dictionary by extracting values from a given dictionary
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


# 6.Delete a list of keys from a given dictionary
# list1 = ["a", "b", "c"]
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for i in list1:
#     if i in dict1:
#         dict1.pop(i)
# print(dict1)

# 7.check if a value exists in a dictionary
# x = input("enter the value:")
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": "apple"}
# if x or int(x) in dict1.values():
#     print("the value exists in the dictionary")
# else:
#     print("the value is not in the dictionary")

# 8.rename key of a dictionary
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": "apple"}
# dict1['z'] = dict1.pop("a")
# print(dict1)

# 9.get the key of a minimum value from the following dictionary
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# x = min(dict1, key=dict1.get)
# print(x)

# 10.change value of a key in a nested dictionary
# sampledict = {
#     "class": {
#         "student": {
#             "name2": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# sampledict["class"]["student"]["marks"]["physics"] = 90
# print(sampledict)

# to change a key in nested dictionary
# sampledict["class"]["student"]["marks"]["chemistry"] = sampledict["class"]["student"]["marks"].pop("history")
# print(sampledict)
