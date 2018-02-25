class Crag(object):
    routes_climbed = 0
    routes_list = []

    def __init__(self, crag_name, route_name):
        self.crag_name = crag_name
        self.route_name = route_name #crag has-a route_name
        Crag.routes_climbed= Crag.routes_climbed + 1
        self.routes_list.append(self)
        #print (Crag.routes_climbed)
        #print ("Routes climbed: ", self.routes_climbed) #prints count total without explicity asking outside class

    def display_info(self): #displays route name
        print ("Crag Name: ", self.crag_name)
        print ("Route Name: ", self.route_name)
        #print ("Routes climbed: ", Crag.routes_climbed)  #I like this solution best. Enter route names and count all at once
        print ("Routes climbed: ", self.routes_climbed)


route1 = Crag("Kaymoor", "Lactic Acid Bath")
#route1.display_info()
#print (Crag.routes_climbed)

route2 = Crag("Lower Meadow", "Mango Tango")
#route2.display_info()
#print (Crag.routes_climbed)

route3 = Crag("Cirque", "Proper Soul")
#route3.display_info()

print ("Routes climbed....")
for i in Crag.routes_list:
    print (i.route_name)
