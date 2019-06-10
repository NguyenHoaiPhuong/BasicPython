class Employee:
    empCount = 0

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayTotalNumberOfEmployees(self):
        strRes = 'Total number of employees: ' + str(Employee.empCount)
        print(strRes)

    