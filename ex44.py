"""
class Parent(object):
    def implicit(self):
        print ("PARENT implicit()")
class Child(Parent):
    pass

dad = Parent()
son = Child()

print (dad.implicit())
son.implicit()
"""
"""
class Parent(object):
    def override(self):
        print ("PARENT override()")
class Child(Parent):
    def override(self):
        #print ("CHILD override(). Now says this")
        pass
dad = Parent()
son = Child()
dad.override()
son.override()
"""
"""
class Parent(object):
    def altered(self):
        print ("Parent altered()")
class Child(Parent):
    def altered(self):
        print ("Child, Before Parent altered()") #runs just like you would expect when son.altered() is called
        super(Child, self).altered() #call super with arguments Child and self, then call function altered on what it returns
        print ("Child, After Parent altered()") #now prints out Child.altered function

dad = Parent()
son = Child()

dad.altered()
son.altered()
"""
"""
class Parent(object):
    def override(self):
        print ("PARENT override()")
    def implicit(self):
        print ("PARENT implicit()")
    def altered(self):
        print ("PARENT altered()")

class Child(Parent):
    def override(self):
        print ("CHILD override()")
    def altered(self):
        print ("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print ("CHILD, AFTER PARENT altered()")
dad = Parent()
son = Child()

dad.implicit() #son doesn't have implicit function, meaning son will inherit this from dad
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
"""
class Other(object):
    def override(self):
        print ("OTHER override()")
    def implicit(self):
        print ("OTHER implicit()")
    def altered(self):
        print ("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print ("CHILD override()")
    def altered(self):
        print ("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print ("CHILD, AFTER OTHER altered()")
son = Child()
son.implicit()
son.override()
son.altered()
