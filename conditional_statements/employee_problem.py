service = float(input("Enter your year of service:"))
salary = int(input("Enter your salary:"))
if service > 5:
    bonus = salary*5/100
    print("you are eligible for bonus of INR", bonus, "rupees")
    print("your new salary is", salary+bonus)
else:
    print("you are not eligible for bonus")
