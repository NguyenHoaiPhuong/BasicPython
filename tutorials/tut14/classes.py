from .model import Employee
from .human import *

def create_instants():
    akagi = Employee("Akagi", 2000)
    yushin = Employee("Yushin", 500)
    akagi.displayTotalNumberOfEmployees()
    yushin.displayTotalNumberOfEmployees()

def access_attributes():
    akagi = Employee("Akagi", 2000)
    akagi.displayInfo()
    print("Total employees: " + str(Employee.empCount))

def built_in_class_attribute():
    print(Employee.__doc__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__bases__)
    print(Employee.__dict__)

def inheritance():
    akagi = Male('Akagi', 34)
    misa = Female('Misa', 24)
    print(akagi)
    print(misa)