class Employee:

    raise_amt = 1.04 #this is a class variable. Class variables must be accessed through the class itself or an instance of the class
    num_of_employees = 0 #going to increment by 1 each time new employee is created

    def __init__(self, first, last, pay):
        self.first = first #same as saying emp1.first = Erich. Self defines the INSTANCE
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_employees += 1 #run this in init because init runs each time a new employee is created

    def fullname(self):  #each method within a class automatically takes instance(self) as first argument
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) #you have the ability to change raise_amount for single instance if we want to

    @classmethod #class method works with whole class, not just instance
    def set_raise_amount(cls, amount): #common convention for class method: cls. Like self in regular method.
        cls.raise_amt = amount

    @classmethod #we are going to use this class method as an alternative constructor. This will allow user to pass in string and not have to construct new employee every time
    def from_string(cls, emp_str): #starts with from, that is a convention also. Takes cls and emp_str as arguments
        first, last, pay = emp_str.split('-') #splits string on hyphen to get first, last, pay
        return cls(first, last, pay) #this line creates new employee. Return so user receives employee object when cls method is called.

    @staticmethod
    def is_workday(day): #determines whether or not this is a workday or not
        if day.weekday() == 5 or day.weekday() == 6:  #if day is Saturday or Sunday. 0-6 for days
            return False
        return True #doesn't hit this conditional, meaning this is a weekday

class Developer(Employee):  #a developer is-a employee. Developer class is going to inherit from employee class things like name, email, etc
#without any code of its own, Developer class will have all attributes and methods of employee class
    raise_amt = 1.10    #applies 10% raise to developers

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #super().__init__ passes in arguments first, last, pay from Employee __init__ method.
        #Employee.__init__(self, first, last pay) #this method works too but doesn't work for multiple inheritance
        self.prog_lang = prog_lang

class Manager(Employee): #code in here is specific to what we want for a manager

    def __init__(self, first, last, pay, employees=None):  #passes in list of employees, sets it to none at beginning
        super().__init__(first, last, pay) #super().__init__ passes in arguments first, last, pay from Employee __init__ method.
        if employees is None:
            self.employees = [] #start list here because you don't want to pass mutable data types (like list) as default arguments
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self): #prints employees this manager supervises
        for emp in self.employees:
            print (self.first, self.last, "-->", emp.fullname())


#emp1 = ("Erich", "Purpur", 50000)
#emp2 = ("Geri", "McDonnell", 60000)


dev1 = Developer("Erich", "Purpur", 50000, "python") #python walks up chain of inheritance to find first, last, pay, email etc. in Employee class
dev2 = Developer("Geri", "McDonnell", 60000, "java") #chain is called method resolution order

mgr1 = Manager("Sue", "Smith", 90000, [dev1]) #manager's info (first, last, pay, employees) She supervises dev1

print (mgr1.email)
#mgr1.print_emps() #prints list of employees mgr1 manages

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)  #removes dev1 from list of employees managed by mgr1
mgr1.print_emps()
print (isinstance(mgr1, Manager)) #tells you if mgr1 is an instance of Manager (True)
print (issubclass(Developer, Employee)) #tells you if Developer is subclass of Employee (True)


#print (dev1.pay)  #prints out Employee pay
#dev1.apply_raise()  #applies raise of 4% to dev1
#print (dev1.pay)  #prints new Employee pay with raise amount.
#print (help(Developer)) #shows chain of inheritance, where methods come from, etc.  VERY HELPFUL

#print (dev1.email)
#print (dev1.prog_lang)

#Employee.set_raise_amount(1.05)
#emp1.set_raise_amount(1.05)
#print (Employee.raise_amt)
#print (emp1.raise_amt)
#print (emp2.raise_amt)

#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Steve-Smith-30000'
#emp_str_3 = 'Jane-Doe-90000'
#new_emp_1 = Employee.from_string(emp_str_1) #users from_string alternative constructor. Now user can pass in string and get new employee objects

#import datetime
#my_date = datetime.date(2016, 7, 11) #we create a date here, pass in date
#print (Employee.is_workday(my_date)) #now call is_workday static method from class to determine whether date is a weekday or not. If so, returns True. If not, returns false
