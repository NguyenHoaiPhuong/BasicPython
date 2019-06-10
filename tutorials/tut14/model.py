class Employee:
    'Common base class for employee'
    
    empCount = 0

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayTotalNumberOfEmployees(self):
        strRes = 'Total number of employees: ' + str(Employee.empCount)
        print(strRes)

    def displayInfo(self):
        strRes = "Name: " + self.name + "\n" \
            + "Salary: " + str(self.salary) + "$"
        print(strRes)