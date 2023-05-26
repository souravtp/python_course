# count vowels
x = input("enter the word:")
x = x.lower()
vowels = "aeiou"
count = 0
for i in x:
    if i in vowels:
        count += 1
print(count)
