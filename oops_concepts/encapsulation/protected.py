"""
Various object-oriented languages like C++, Java, Python control access modifications which are used to restrict
access to the variables and methods of the class. Most programming languages has three forms of access modifiers,
which are Public, Protected and Private in a class.
public: these are accessible from anywhere in the program. eg: name
protected: these are accessible inside the class and inherited classes. eg: _name
private: these are only accessible inside the class not inside it's child class or outside class. eg: __name
"""


# define parent class Company
class Company:
    # constructor
    def __init__(self, name2, proj):
        self.name2 = name2  # name2(name2 of company) is public
        self._proj = proj  # proj(current project) is protected

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self._proj)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, ename, sal, cname, proj):
        # calling parent class constructor
        Company.__init__(self, cname, proj)
        self.name2 = ename  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name2, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name2, c.show())

print("Welcome to ", c.name2)
print("Here ", e.name2, " is working on ", c._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()
e.show()
c.show()


"""another example"""


# class BankAccount:
#     def __init__(self, name, age):
#         self.__balance = 0  # private attribute. It can only be accessed inside this class.
#         self._name = name  # protected, can be accessed inside this class and child classes.
#         self.age = age  # public, can be accessed anywhere in this program.
#
#     def deposit(self, amount):
#         self.__balance += amount  # private attribute '__balance' is accessible from same class.
#
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient balance")
#         else:
#             self.__balance -= amount
#
#     def get_balance(self):
#         return self.__balance
#
#     def account_holder(self):
#         return self._name
#
#
# class Savings(BankAccount):
#     def savings_balance(self):
#         return self.get_balance()  # we can access the method, defined using private attributes inside
#         # base class from here
#         # return self.__balance  # this is not accessible since __balance is protected.
#
#     def name_of_holder(self):
#         return self._name  # _name is accessible from child class, since it is private.
#
#
# my_account = BankAccount('Sourav', 24)
# print(my_account.account_holder())
# # print(my_account.__balance)  # this gives an error because balance attribute is private and cannot be accessed
# # directly. It can be accessed using get_balance method. same applies for __name attribute.
#
# # print(my_account._name)  # this is not accessible because it is private. only accessible inside class
# # or child class.
