# count strings with same starting and ending letters
lst1 = ["aba", "aab", "xyzvx", "efr", "gklopg"]
count = 0
for elem in lst1:
    if len(elem) > 1:
        if elem[0] == elem[-1]:
            count += 1
print(count)