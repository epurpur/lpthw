class BMR():
    def __init__(self, mass, height, age, sex):
        self.mass = mass
        self.height = height
        self.age = age
        self.sex = sex
        self.bmr = 0 #this is an instance variable because it depends on the person

    def calc_bmr(self):
        if self.sex == "male":
            self.bmr = (10*self.mass)+(6.25*self.height)-(5.0*self.age)+5
        elif self.sex == "female":
            self.bmr = (10*self.mass)+(6.25*self.height)-(5.0*self.age)-161
        else:
            print ("Choose male or female")
        return (self.bmr)

person1 = BMR(68, 177, 30, "male")
print ("Erich's BMR", person1.calc_bmr())

person2 = BMR(54, 162.5, 63, "female")
print ("Mom's BMR", person2.calc_bmr())

person3 = BMR(90, 178, 63, "male")
print ("Dad's BMR", person3.calc_bmr())

person4 = BMR(63, 175, 28, "female")
print ("Eileen's BMR", person4.calc_bmr())
