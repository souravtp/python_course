class Company:
    def company_name(self):
        return 'Google'


class Employee(Company):
    def info(self):
        c_name = super().company_name()
        print('John works at', c_name)


