
print ("""We are playing a game today at Ship Rock. All the bros are here. Most points wins.""")


class Climber(object):
    def __init__(self, climber_name, ability): #add ability, do some math with climb method?
        self.climber_name = climber_name
        self.ability = ability
        self.routes_climbed = []
        self.energy_level = 100
        self.pump_level = 0
        self.total_score = 0
        self.pitch_count = 0
        print ("")
        print ("Starting", self.climber_name)

    def engine(self):
#I want to return here after every method call, which will drive the game
        next_action = input(f"What next {self.climber_name}? ")
        if next_action == "climb":
            self.climb_route((str(input("Enter route name: "))), (float(input("Enter route grade: " ))))
        elif next_action == "eat":
            self.eat()
        elif next_action == "drink":
            self.drink()
        elif next_action == "smoke":
            self.smoke()
        elif next_action == "finish":
            self.grand_finale()

    def eat(self):
        #restores energy_level
        food = (input("What are you going to eat? "))
        if food == "snack":
            self.energy_level += 10
            print ("Eating snack...")
            self.engine()
        elif food == "lunch":
            self.energy_level += 25
            print ("Eating lunch...")
            self.engine()
        elif food != "snack" or "lunch":
            print ("Invalid food")
            self.eat()
        return self.energy_level
        self.engine()

    def drink(self):
        #lower energy_level, water raises energy_level, beer lowers energy_level
        drink = (input("What are you going to drink? "))
        if drink == "water":
            self.energy_level += 10
            print ("Drinking water...")
            self.engine()
        elif drink == "beer":
            self.energy_level -= 15
            print ("Drinking beer...")
            self.engine()
        elif drink != "beer" or "water":
            print ("Invalid drink")
            self.drink()
        return self.energy_level
        self.engine()

    def smoke(self):
        #lower energy_level, cigarette raises energy_level, bowl lowers energy_level
        smoke = (input("What are you going to smoke? "))
        if smoke == "cigarette":
            self.energy_level += 5
            print ("Smoking cig...")
            self.engine()
        elif smoke == "bowl":
            self.energy_level -= 10
            print ("Smoking bowl...")
            self.engine()
        elif smoke != "cigarette" or "bowl":
            print ("Invalid smoke")
            self.smoke()
        return self.energy_level
        self.engine()

    def climb_route(self, route_name, grade):
        print ("Climbing...", route_name, " Grade...", grade)
        if grade < (.9 * self.ability):
            self.pump_level += (grade * .8)
        elif grade >= (.9 * self.ability):
            self.pump_level += (grade * 1.5)
        self.energy_level -= (grade * 1.7)
        self.total_score += grade
        self.routes_climbed.append(route_name)
        self.pitch_count += 1
        if self.pitch_count == 3:
            print ("You are hungry, time to eat")
            self.eat()  #returns to eat() method
        if self.energy_level <= self.pump_level:
            print ("Your day is over.")
            self.grand_finale()
        self.engine()


    def grand_finale(self):
        #tally points, see who is winner
        #print (self.name, " totals") Why doesn't this work?
        print ("-----------------")
        print (self.climber_name, "TOTALS")
        print ("-----------------")
        print ("Energy level = ",self.energy_level)
        print ("Pump level = ", self.pump_level)
        print ("Total pitches = ", self.pitch_count)
        print ("Routes climbed = ", self.routes_climbed)
        print ("Total Score = ", self.total_score)
        #sys.exit() #quits program

climber1 = Climber("Erich Purpur", 13)
climber1.engine()
