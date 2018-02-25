## Animal is-a object (yes, sort of confusing) looking at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## Person is-a super employee and has-a name and has-a salary
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

##rover is-a dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet, satan the cat
mary.pet = satan

## Frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

LOOK AT GPA2.PY
