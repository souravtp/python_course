set1 = {"apple", "banana", "orange", 1, 3, 4, 5, 10}
set2 = {"apple", "kiwi", "mango", 2, 8, 12, 5}

# union '|'
# S3 = set1.union(set2)  # or print(set1 | set2)
# print(S3)  # update() method adds set2 elements to set1

# intersection '&'
# S4 = set1.intersection(set2)  # or print(set1 & set2)
# print(S4)

# difference '-'
# S5 = set1.difference(set2)  # or print(set1 - set2)
# print(S5)

# symmetric difference '^'
# S6 = set1.symmetric_difference(set2)  # or print(set1 ^ set2)
# print(S6)


# set3 = {"car", "scooter", "van", "lorry", 1, 3, 5, 7}
# set4 = {"apple", "orange", "banana", "van", 1, 2, 3, 4}

# update()
# set3.update(set4)
# print(set3)

# intersection_update() '|='
# set3.intersection_update(set4)
# print(set3)

# difference update()
# set3.difference_update(set4)
# print(set3)

# symmetric_difference_update()
# set3.symmetric_difference_update(set4)
# print(set3)


S1 = {"a", "b", "c", "d", "e"}
S2 = {"a", "b", "c"}

x = S1.issuperset(S2)
print(x)

y = S2.issubset(S1)
print(y)

z = S1.isdisjoint(S2)  # returns true if no common elements for two sets.
print(z)

p = S1.copy()
print(p)
