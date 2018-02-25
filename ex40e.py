class House(object):
    """Plans for House"""
    def __init__(self, doors, windows):
        self.doors = doors
        self.windows = windows
    def open_door(self):
        print ("open front door")
    def count_doors(self):
        print (f"This house has {self.doors} doors")
    def window_style(self):
        print (f"This house has {self.windows} style windows.")
    def make_breakfast(self, oatmeal):
        print (f"Today you make breakfast with {oatmeal} brand oatmeal.")
    def repairs(self):
        repairs = self.doors * 5
        print (f"You have {self.doors} doors, each takes 5 hours to repair. You have {repairs} hours of repairs.")
my_house = House(3, "Victorian")
#my_house.open_door()
#my_house.count_doors()
#my_house.window_style()
#my_house.make_breakfast("Quaker's")
my_house.repairs()
