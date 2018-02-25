
class Restaurant(object): #crates class called Restaurant
    bankrupt = False #assign it a property, bankrupt, which is false
    def open_branch(self): #assign class a function, open_branch, which only occurs if bankrupt = false
        if not self.bankrupt:
            print ("Branch opened")


x = Restaurant() #renames class (restaurant) with x for speend.x is a restaurant which has a property bankrupt and a function open_branch.
print (x.bankrupt) #prints value for bankrupt in x. Which is false.

y = Restaurant #now renames class as y
y.bankrupt = True #defines y.bankrupt as true
print (y.bankrupt) #prints value for y.bankrupt, which is True
