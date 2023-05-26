num = int(input("enter the number:"))
num_str = str(num)
l = len(num_str)
i = 1
sum = 0
while i <= l:
    r = num % (10**i)
    s = r // (10**(i-1))
    sum += (s**l)
    i += 1
if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
