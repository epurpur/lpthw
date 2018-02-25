import datetime # we will use this for date objects

class Person:   #defines class. called person
#self is the object itself
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name #the person's name
        self.surname = surname #the person's surname
        self.birthdate = birthdate

        self.address = address #person's address
        self.telephone = telephone #person's phone number
        self.email = email #person's email address

    def age(self): #function to define the age of self (the object itself)
        today = datetime.date.today()
        age = today.year - self.birthdate.year #age defined as variable inside function
#this next line says "if you haven't reached your birthday this year, your age is your age - 1"
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 2, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name) #person (lower case) defines Person(attributes)
print(person.email)
print(person.age()) #needs open brackets because "self" is needed parameter
