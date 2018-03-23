import sys

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

    def engine(self):
#I want to return here after every method call, which will drive the game
        next_action = input("What next? ")
        if next_action == "climb":
            self.climb_route((str(input("Enter route name: "))), (float(input("Enter route grade: " ))))
        elif next_action == "finish":
            self.grand_finale()

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
        if self.energy_level <= self.pump_level:
            print ("Your day is over.")
            self.grand_finale()
        self.engine()

    def grand_finale(self):
        sys.exit() #quits program

climber1 = Climber("Erich Purpur", 13.0)
climber1.engine()
