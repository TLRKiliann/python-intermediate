#!/usr/bin/python3


class Employee(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        informations = self.name, self.age, self.salary
        return f'{informations}'

    @staticmethod
    def entry_salary(age):
        if age > 25:
            return 5000
        if age < 25:
            return 3000
        return 9000

class SoftwareEngieneering(Employee):
    def __init__(self, name, age, salary, motivation):
        super().__init__(name, age, salary)
        self.motivation = motivation

    def declinaison(self):
        print(f'Name: {self.name} age: {self.age} is working for: {self.salary}')

    def work(self):
        print(f'{self.name} is coding')

    def motiv(self):
        print(f'Motivated ? {self.motivation}')


class Designer(Employee):
    def __init__(self, name, age, salary, motivation):
        super().__init__(name, age, salary)
        self.motivation = motivation

    def declinaison(self):
        print(f'Name: {self.name} age: {self.age} is working for: {self.salary}')

    def work(self):
        print(f'{self.name} is drawing')

    def motiv(self):
        print(f'Motivated ? {self.motivation}')


class SoftwareProgramming(Employee):
    def __init__(self, name, age, salary, motivation):
        super().__init__(name, age, salary)
        self.motivation = motivation

    def declinaison(self):
        print(f'Name: {self.name} age: {self.age} is working for: {self.salary}')

    def work(self):
        print(f'{self.name} is programming...')

    def motiv(self):
        print(f'Motivated ? {self.motivation}')


class TestSomethingElse(Employee):

    def toTest(self):
        print(f'To test app => Name: {self.name} age: {self.age} is working for: {self.salary}')

"""
soft = SoftwareEngieneering("Art", 24, 3400, "yes")
soft.declinaison()
soft.work()
soft.motiv()

des = Designer("Mathias", 21, 2300, "no")
des.declinaison()
des.work()
des.motiv()
"""

"""
Wîth staticmethod
e1 = SoftwareEngieneering("Art", 24, 3400, "yes")
print(e1.entry_salary(27))
"""

t1 = TestSomethingElse("Carla", 23, 4500)
t1.toTest()


employees = [SoftwareEngieneering("Art", 27, 7000, "no"),
             SoftwareEngieneering("Sabrina", 24, 3400, "yes"),
             Designer("Mathias", 21, 2300, "no"),
             SoftwareProgramming("Wendy", 37, 2700, "yes")]

def callEmp(employees):
    for employee in employees:
        employee.declinaison()
        employee.work()
        employee.motiv()

callEmp(employees)
