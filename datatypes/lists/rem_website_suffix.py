list1 = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
list2 = []
for i in list1:
    x = i.find(".", 4)
    print(i[x:])
    list2.append(i[x:])
print(list2)