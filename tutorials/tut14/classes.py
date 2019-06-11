from .employee import Employee
from .human import Male, Female
from .vector import Vector
from .counter import Counter

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

def inherit_and_override():
    akagi = Male('Akagi', 34)
    misa = Female('Misa', 24)
    print(akagi)
    print(misa)

def overload():
    a = Vector(1, 3)
    b = Vector(6, 7)
    c = a + b
    print(c)

def hide_data():
    cnt1 = Counter()
    cnt1.Count()
    cnt2 = Counter()
    cnt2.Count()

    try:
        print(Counter.__count)
    except Exception as e:
        print(e)