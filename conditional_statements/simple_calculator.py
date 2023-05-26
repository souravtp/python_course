a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = input("choose the operation +,-,*,/ :")

if c=='+':
    print("the sum, a+b=", a+b)
elif c=='-':
    print("the difference a-b=", a-b)
elif c=='*':
    print("the product a*b=", a*b)
elif c=='/':
    print("the division a/b=", a*b)
else:
    print("entered operation is not available")