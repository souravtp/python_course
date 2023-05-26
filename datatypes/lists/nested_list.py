lst1 = ["apple", "banana", "orange", ["samsung", "redmi", "vivo", "lava"], "pineapple"]
print(lst1[3][3])
lst1[3].append("oppo")
print(lst1)
print(lst1.count("banana"))
print(lst1.count("samsung"))
print(lst1.count(["samsung", "redmi", "vivo", "oppo"]))
lst1[3].insert(1, "iqoo")
print(lst1)
lst1[3].pop(2)
print(lst1)
lst1[3].remove("vivo")
print(lst1)

lst2 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
# lst2[2][1][2].extend(sub_list)
# print(lst2)

lst2[2][1][2].insert(2, sub_list)
print(lst2)
