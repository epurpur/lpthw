"""
class Planet:
    planet_list = []

    def __init__(self, name):
        self.name = name
        self.planet_list.append(self)

p1 = Planet("earth")
p2 = Planet("mars")

for i in Planet.planet_list:
    print (i.name)
"""

class State():
    states_list = []
    total_pop = 0

    def __init__(self, name, capital, population): #state has-a capital and a population
        self.name = name
        self.capital = capital
        self.population = population
        self.states_list.append(self) #states list itself append itself to states_list
        State.total_pop = State.total_pop + self.population #total pop of states = total pop + population of state itself

    #def add_two(self, add):
    #    print ("adding {add} to {State.total_pop}")

s1 = State("North Carolina", "Raleigh", 1)
s2 = State("Virginia", "Richmond", 2)
s3 = State("Tennessee", "Nashville", 3)

for s in State.states_list:
    print (s.name)
    print (f"Pop = {s.population}")

def new_pop():
    for s in State.states_list:
        s.population = s.population + 2
        print (s.total_pop)

print (f"Total State population = {State.total_pop}")
#print (f"Total state population =", new_pop())

print (type(State))
