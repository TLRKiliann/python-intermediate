#!/usr/bin/python3

class Employee(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._bugs = 0

    @staticmethod
    def calcage(age):
        if age < 40:
            return 3000
        if age > 60:
            return 7000
        return 5500

    def code(self):
        self._bugs += 1

    def get_salary(self):
        return self._salary

    def set_salary(self, base_value):
        self._salary = self._calculate(base_value)

    def _calculate(self, base_value):
        if self._bugs < 10:
            return base_value
        if self._bugs < 100:
            return base_value * 2
        return base_value * 3


ce = Employee("Klara", 42)
print(ce.name, ce.age)

for i in range(11):
    ce.code()

ce.set_salary(2000)
print(ce.get_salary())

print(ce.calcage(42))
