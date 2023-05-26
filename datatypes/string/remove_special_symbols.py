x = input("Enter the sentence:")
y = ""
for i in x:
    if i.isalpha() or i.isspace():
        y += i
print(y.replace("  ", " "))
