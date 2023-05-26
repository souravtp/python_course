"""
OOP works with objects and classes.
Object is any entity that has attributes and behaviours. For example, a parrot is an object. It has,
attributes - name2, age, color, etc.
behaviour - dancing, singing, etc.

Similarly, a class is a blueprint for that object.

The main concepts of OOPs are
1. Class:         A collection of objects. It is a logical entity that has some specific attributes and methods.
2. Object:        an object is an instance of a class that encapsulates data and behavior.
3. Encapsulation: Wrapping of a data and the code that operates on the data within a single entity. It is also known as
                  information hiding. This allows us to hide the complexity of our code and protect the data
                  from outside access.
4. Inheritance:   Inheriting the properties of a parent class to child class.
5. Polymorphism:  Polymorphism means "many forms", The word polymorphism means having many forms.
                  In programming, polymorphism means the same function name (but different signatures)
                  being used for different types. The key difference is the data types and number of arguments
                  used in function. and it occurs when we have many classes that are related to each other by
                  inheritance. Polymorphism is a concept of using the same interface to represent different types
                   of objects(for example, we use len() function to find the length of a string, also
                  length of list, tuple, dictionary etc. each time different datatypes are used but len() function
                  works with it). It allows us to write code that can work with objects of different classes.
5. Abstraction:   Data hiding. eg: In an ATM we only need to get money. All the background processes are
                  hidden from us.
                  Abstraction is a concept of simplifying complex systems by breaking them down into smaller,
                  more manageable parts. It involves identifying the essential features of a system and ignoring
                  the rest. This allows us to focus on the important details and ignore the irrelevant ones.
"""

# class Myclass:
#     x = 6
#
#
# obj = Myclass()
# print(obj.x)


# class Car:
#     name2 = ''
#     model = 2015
#
#
# car1 = Car()
# car1.name2 = 'Vento'
# car1.model = 2015
#
# car2 = Car
# car2.name2 = 'Polo'
# car2.model = 2022
#
# print(f'{car1.name2} is {car1.model} model car')
# print(f'{car2.name2} is {car2.model} model car')


"""
Constructor
-----------
In object-oriented programming (OOP), a constructor is a special method that is automatically called
when an object of a class is created. It is used to initialize the instance variables or attributes
of the object.
In Python, the constructor method is called __init__(). When a new instance of a class is created,
Python automatically calls the __init__() method for that class,
passing in the new object as the first parameter (self). there are two types of constructors. Default constructor and
parameterized constructor.
"""

"""default constructor: The default constructor is a simple constructor which does’t accept any arguments.
Its definition has only one argument which is a reference to the instance being constructed. eg:"""


class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    # a method for printing data members
    def print_geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_geek()

"""parameterized constructor: constructor with parameters is known as parameterized constructor.
The parameterized constructor takes its first argument as a reference to the instance being constructed
known as self and the rest of the arguments are provided by the programmer. eg:"""


class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#
# my_car = Car("Toyota", "Corolla", 2022)
# print(my_car.year)


# class Car:
#     def __init__(self, name2, model):
#         self.name2 = name2
#         self.model = model
#
#
# car1 = Car('Vento', 2015)
# print(f'{car1.name2} is {car1.model} model car')


"""another example"""


class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def test(self):
        print("car is started")

    def __str__(self):  # this method returns a string. when the object is called.
        return f'{self.name}({self.model})'


# car1 = Car("Vento", 2015)
# car1.model = 2020  # here we have changed the attribute of the object car1.
# del car1.model  # here we have deleted the attribute 'model'. So the print(car1) will give attribute error.
# print(car1)
# car1.test()


# car2 = Car('mustang', 1969)  # the del attribute only delete an attribute from the object. Not from class. So we can
# # use the class to create another object.
# delattr(Car, 'model')  # this will remove an attribute from a class permanently
# print(car2)
# car3 = Car('GTR', 1972)
# print(car3)  # This will give error because the 'model' attribute is removed from the class itself.


"""
Attributes and methods
----------------------
An attribute is a variable that holds a value. It represents a characteristic of an object,
and it is used to store data. Examples of attributes in a Car class could be make, model, and year.

A method, on the other hand, is a function that performs an action.
It is used to perform some operation on an object or to retrieve data from an object.
Examples of methods in a Car class could be start_engine(), accelerate(), and brake().
"""
# attributes


# class Car:
#     wheels = 4  # class variable
#
#     def __init__(self, make, model, year):
#         self.make = make  # instance variable
#         self.model = model  # instance variable
#         self.year = year  # instance variable
#
#     def car_info(self):
#         return "Make: {}, Model: {}, Year: {}, Wheels: {}".format(self.make, self.model, self.year, self.wheels)
#
#
# my_car = Car('mercedes', 'AMG', 2020)
# print(my_car.wheels)
# print(my_car.year)  # this is an attribute of the object 'my_car'.
# # The instance variables becomes attributes for an object

# methods


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def car_info(self):
#         return "Make: {}, Model: {}, Year: {}".format(self.make, self.model, self.year)
#
#     def drive(self):  # this is a method added to Car class.
#         return "Driving the car"
#
#
# my_car = Car('BMW', 'M8', 2019)
# print(my_car.drive())


"""In this example, __init__() takes three arguments (make, model, and year) along with self,
and assigns them to instance variables (self.make, self.model, and self.year) in the new object.
When we create a new instance of the Car class with my_car = Car("Toyota", "Corolla", 2022) 
Python automatically calls __init__() with the my_car object as self and the provided arguments."""
