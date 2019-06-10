import model

def create_instants():
    akagi = model.Employee("Akagi", 2000)
    yushin = model.Employee("Yushin", 500)
    akagi.displayTotalNumberOfEmployees()
    yushin.displayTotalNumberOfEmployees()
    model.Employee.displayTotalNumberOfEmployees()
