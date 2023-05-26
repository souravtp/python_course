list1 = [1, 2, 5, 9, 4, 12, 29, 64, 52, 87, 72]
even = []
odd = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even, odd, sep="\n")
