class Dog:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def get_color(self):
        print (self.color)
    def get_age(self):
        print (self.age)

buster = Dog('red', 4)
buster.get_color()
buster.get_age()
