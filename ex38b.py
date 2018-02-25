class Human(object): #defines class Human as object
    def __init__(self, name, friend=None): #2 arguments: self and name. Defines friend = none
        self.name = name #calls name on self = name
        self.friend = friend #calls friend on self = friend
    def say_name(self): #defines say_name with argument self
        print("My name is "+self.name) #prints .... self.name
    def say_goodnight(self): #defines say_goodnight with argument self
        if self.friend is None: #if no friend
            print("Good night nobody.")
        else: #if friend
            print("Good night "+self.friend.name) #prints Good Night "friend name"

#create a new human object named Erich
erich = Human("Erich")
#create a human object named joe with Erich as a friend
joe = Human("Joe", erich)

erich.say_name() #shows 'My name is Erich'
erich.say_goodnight() #shows 'Good night nobody.'
joe.say_name() # shows 'My name is Joe'
joe.say_goodnight() #shows 'Good night Erich'
