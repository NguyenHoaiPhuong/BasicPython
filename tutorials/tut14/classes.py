import model

def create_instants():
    akagi = model.Employee("Akagi", 2000)
    yushin = model.Employee("Yushin", 500)
    akagi.displayTotalNumberOfEmployees()
    yushin.displayTotalNumberOfEmployees()

def access_attributes():
    akagi = model.Employee("Akagi", 2000)
    akagi.displayInfo()
    print("Total employees: " + str(model.Employee.empCount))

def built_in_class_attribute():
    print(model.Employee.__doc__)
    print(model.Employee.__name__)
    print(model.Employee.__module__)
    print(model.Employee.__bases__)
    print(model.Employee.__dict__)
