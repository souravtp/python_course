a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b and b == c:
    print("All three numbers are equal.")
elif a == b or a == c or b == c:
    if a == b and b > c:
        print("a and b have the highest value.")
    elif a == c and c > b:
        print("a and c have the highest value.")
    else:
        print("b and c have the highest value.")
else:
    if a > b and a > c:
        print("a has the highest value.")
    elif b > a and b > c:
        print("b has the highest value.")
    else:
        print("c has the highest value.")
