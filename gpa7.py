class Climber:

    num_of_climbers = 0 #increments by one each time a new climber is created


    def __init__(self, first, last, age, height, weight):
        self.first = first
        self.last = last
        self.age = age
        self.spray = first + last + "@8a.nu"
        self.height = height
        Climber.num_of_climbers += 1 #run this in init because init runs each time a new climber is created

    def fullname(self):
        #print (self.first, self.last) #returns name but doesn't look great
        return ("{} {}".format(self.first, self.last)) #these do the same thing

class Sport_weenie(Climber):
    num_of_sport_weenies = 0
    def __init__(self, first, last, age, height, weight):
        super().__init__(first, last, age, height, weight)
        Sport_weenie.num_of_sport_weenies = Sport_weenie.num_of_sport_weenies + 1

class Trad_Dad(Climber):
    num_of_trad_dads = 0
    def __init__(self, first, last, age, height, weight):
        super().__init__(first, last, age, height, weight)
        Trad_Dad.num_of_trad_dads += 1


climber1 = Climber("Adam", "Ondra", 24, 180, 65)
#print (climber1.fullname())
#print (Climber.num_of_climbers)
climber2 = Climber("Chris", "Sharma", 35, 180, 70)
#print (Climber.num_of_climbers)
#print (climber1.spray, climber2.spray)
sw1 = Sport_weenie("Jonathan", "Siegrist", 31, 160, 60)
#print (sw1.height)
#print ("Now there are", Climber.num_of_climbers, "climbers") #totals when sport climbers are added too
sw2 = Sport_weenie("Dani", "Andrada", 43, 178, 66)
#print ("Adding", sw2.fullname(), "to list. Now there are", Climber.num_of_climbers, "climbers.")
#print ("and", Sport_weenie.num_of_sport_weenies, "of them are sport weenies.")
td1 = Trad_Dad("Alex", "Honnold", 32, 181, 67)
td2 = Trad_Dad("Tommy", "Caldwell", 38, 176, 65)
td3 = Trad_Dad("Mason", "Earle", 28, 183, 64)
#print ("There are", Trad_Dad.num_of_trad_dads, "trad dads.")
#print ("There are", Sport_weenie.num_of_sport_weenies, "sport weenies.")
#print ("There are", Climber.num_of_climbers, "total climbers.")
#print (climber1.fullname(), "and", climber2.fullname(), "are neither sport nor trad specialists.")
#DO Some formatting with the above statement
