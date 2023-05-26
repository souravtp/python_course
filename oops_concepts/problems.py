"""1. Create a class with instance attributes"""

# class Vehicle:
#     def __init__(self, name2, model):
#         self.name2 = name2
#         self.model = model
#
#
# x = Vehicle("polo", 2015)
# print(x.name2, x.model)


"""simple calculator using class"""

# class Calculator:
#     # def __init__(self, a, b):
#     #     self.a = a
#     #     self.b = b
#     def addition(self, a, b):
#         return a + b
#
#     def subtraction(self, a, b):
#         return a - b
#
#     def multiplication(self, a, b):
#         return a * b
#
#     def division(self, a, b):
#         return a / b


# x = int(input("enter first number:"))
# y = int(input("enter second number:"))
# calculator = Calculator()
# choice = 1
# while choice != 0:
#     print("choice1: Addition\nchoice2: Subtraction\nchoice3: Multiplication\nchoice4: Division\nenter 0 to exit ")
#     choice = int(input("enter choice:"))
#     if choice == 1:
#         print(calculator.addition(x, y))
#     elif choice == 2:
#         print(calculator.subtraction(x, y))
#     elif choice == 3:
#         print(calculator.multiplication(x, y))
#     elif choice == 4:
#         print(calculator.division(x, y))
#     elif choice == 0:
#         break
#
# else:
#     print('enter a valid choice!')


"""create a class vehicle and add attributes and child class"""

# class Vehicle:
#     def __init__(self, make, model, year, color, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.mileage = mileage
#
#     def drive(self, distance):
#         return distance/self.mileage
#
#     def get_info(self):
#         print(f'{self.make}, {self.model}, {self.year}, {self.color}, {self.mileage}')
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, color, mileage, num_doors, engine_type):
#         super().__init__(make, model, year, color, mileage)
#         self.num_doors = num_doors
#         self.engine_type = engine_type
#
#     def get_info(self):
#         print(f'{self.make}, {self.model}, {self.year}, {self.color}, {self.mileage}, {self.num_doors},\
#         {self.engine_type}')
#
#
# my_vehicle = Vehicle('toyota', 'supra', 1993, 'yellow', 10.54)
# my_car = Car('toyota', 'supra')
# my_car.get_info()


"""a"""

"""
a circle class models a circle with a radius and color
attributes: radius, color
methods: Circle, get_radius, get_circumference
"""
# from math import pi
# import turtle
# t = turtle.Turtle()
#

# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def circle(self):
#         print(f'the circle is created with radius {self.radius} and color {self.color}')
#         t.pencolor(self.color)
#         t.circle(self.radius, -360)
#         turtle.done()
#
#     def get_area(self):
#         return pi * self.radius**2
#
#     def get_circumference(self):
#         return 2 * pi * self.radius
#
#
# c = Circle(100, 'red')
# c.circle()
# print(c.get_area())


"""the rectangle class"""

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_length(self):
#         print(self.length)
#
#     def get_width(self):
#         print(self.width)
#
#     def get_area(self):
#         return self.length*self.width
#
#
# obj = Rectangle(10, 20)
# print(obj.get_area())


"""The employee class"""

# class Employee:
#     def __init__(self, id, firstname, lastname,  salary):
#         self.name = None
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#
#     def getid(self):
#         print(self.id)
#
#     def getfirstname(self):
#         print(self.firstname)
#
#     def getlastname(self):
#         print(self.lastname)
#
#     def getname(self):
#         self.name = self.firstname + self.lastname
#         print(self.name)


"""date class"""


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def get_day(self):
#         print(self.day)
#
#     def get_month(self):
#         print(self.month)
#
#     def get_year(self):
#         print(self.year)
#
#     def set_day(self, day):
#         self.day = day
#
#     def set_month(self, month):
#         self.month = month
#
#     def set_year(self, year):
#         self.year = year
#
#     def set_date(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def tostring(self):
#         print(f'{str(self.day)}/{str(self.month)}/{str(self.year)}')
#
#
# today = Date(19, 4, 2023)
# today.tostring()
# today.set_day(25)
# today.tostring()
# today.set_date(12, 3, 1999)
# today.tostring()

"""python program to find validity of a string of parentheses"""


# class py_solution:
#     def is_valid_parenthese(self, str1):
#         stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
#         for parenthese in str1:
#             if parenthese in pchar:
#                 stack.append(parenthese)
#             elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
#                 return False
#         return len(stack) == 0
#
#
# print(py_solution().is_valid_parenthese(""))


"""create a class and method with arguments, a list and a target integer, such that the method returns
index of elements of the list whose sum is the given target"""


# class pysolution:
#     def twosum(self, arr, target):
#         for i in range(len(arr)):
#             for j in range(i+1, len(arr)):
#                 if arr[j] == target - arr[i]:
#                     return i, j
#
#
# arr1 = [1, 3, 7, 5, 12, 15, 22, 17]
# target1 = 19
# print(pysolution().twosum(arr1, target1))


"""with less time complexity O(n)"""
from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_table = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in hash_table:
#                 return [hash_table[complement], i]
#             hash_table[num] = i
#         return None
#
#
# arr1 = [1, 3, 7, 5, 12, 15, 22, 17]
# target1 = 19
# print(Solution().twoSum(arr1, target1))

# print(list(enumerate(arr1)))


"""find three elements that sums to zero from a list of elements"""


# class Pysolution:
#     def sum_of_two(self, nums):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 return nums[i]+nums[j]
#
#     def sum_to_zero(self, nums: List[int]) -> List[int]:
#         negs = [i for i in nums if i<0]
#         pos = [i for i in nums if i>=0]
#         if self.sum_of_two(nums) <= 0:
#             for i in pos:
#                 if pos[i] = -self.sum_of_two()


# print(Pysolution().sum_to_zero([1, 2, 3, -3, 4, -6, 7]))


# def sum_to_zero(nums):
#     l = len(nums)
#     for i in range(l):
#         for j in range(i, l):
#             s2 = nums[i]+nums[j]
#             # temp = nums[:]
#             temp = [nums[x] for x in range(l) if (x != i or x != j)]
#             to_find = 0-s2
#             if to_find in temp:
#                 print(to_find, nums[i], nums[j])
#
#
# nums1 = [5, 1, 2, 3, -3, 4, -6, 7]
# sum_to_zero(nums1)

