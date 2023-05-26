i = 10
while i <= 100:
    j = 2
    count = 0
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    if count == 1:
        print(i)
    i += 1
