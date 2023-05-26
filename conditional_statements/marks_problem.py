marks = int(input("enter your marks:"))
if 0 <= marks < 25:
    print("your grade is F")
elif 25 <= marks < 45:
    print("your grade is E")
elif 45 <= marks < 50:
    print("your grade is D")
elif 50 <= marks < 60:
    print("your grade is C")
elif 60 <= marks < 80:
    print("your grade is B")
elif 80 <= marks <= 100:
    print("your grade is A")
else:
    print("enter marks between 0 and 100")