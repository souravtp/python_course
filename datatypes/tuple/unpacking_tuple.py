tuple1 = ("apple", "orange", (10, 20, 30), ["car", "bus", "lorry"], 50)
(a, b, c, d, e) = tuple1
print(a)
print(c)
print(a, *b)

(x, *y) = tuple1
print(x)
print(y)
