"""1)Write a Python function to create and print a list where the
values are square of numbers between 1 and 30 (both included)."""


def sq_list(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i**2)
    return lst


print(sq_list(30))


"""2)Write a Python function that accepts a string and calculate the number of upper case letters 
and lower case letters."""


def count_cases(str1):
    upper = 0
    lower = 0
    for i in str1:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return f'number of upper case letters is {upper}, and lower case letters is {lower}'


my_str = "Hey, How you Doin?"
print(count_cases(my_str))


"""3)Write a Python function that checks whether a passed string is palindrome or not."""


def is_palindrome(str2):
    lstr = str2.lower()
    l = len(str2)
    counter = 0
    for i in range(l // 2):
        if lstr[i] != lstr[-(i + 1)]:
            return f'{str2} is not a palindrome'
        else:
            counter += 1
    if counter == l//2:
        return f'{str2} is a palindrome'


print(is_palindrome("Malayalam"))


"""4) write a python function returns a list with unique elements  of the entered list"""


def unique_list(list1):
    unique = []
    for i in list1:
        if i not in unique:
            unique.append(i)
    return unique


my_list = [1, 3, 5, 1, 5, 2, 4]
print(unique_list(my_list))


"""write a python function to check whether a number is perfect or not."""


def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        return f'{n} is a perfect number'
    else:
        return f'{n} is not a perfect number'


print(is_perfect(28))
