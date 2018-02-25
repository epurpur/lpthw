"""
credits = 0
def add_credits(x):
    new_total = credits + x
    return new_total

print (add_credits(3))
print (add_credits(4))
"""

class Employee(object): #object?
    "common base class for all employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name #employee has-a name
        self.salary = salary #employee has-a salary
        Employee.empCount += 1

    def displayCount(self): #do I even need this??
        print ("Total Employee %d" % Employee.empCount) #look up what this line does

    def displayEmployee(self): #displays employee attribute information
        print ("Name: ", self.name, "Salary: ", self.salary)

"This creates first object of Employee class"
emp1 = Employee("Erich", 10000)
emp1.displayEmployee()
print ("Total employees: ", Employee.empCount)
