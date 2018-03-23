class MyClass:

#Constructor (Creates an instance with default settings)
    def __init__(self):
        self.color = "Red"
        self.name = "Square"
        self.size = "Big"

#Messages the object understands (Protocol)
    def showObject(self):
        print ("Color is: %s \nName is: %s \nSize is: %s"
        %(self.color, self.name, self.size))

    def setColor(self, aColor):
        self.color = aColor
        print (self.objSize(aColor))

    def setName(self):
        aName = input("Please enter a name: ")
        self.name = aName

    def objSize(self, aColor):
        if aColor == "Red":
            self.size = "Big"
        elif aColor == "Blue":
            self.size = "Medium"
        else:
            self.size = "Small"
        return ("The size of the object is %s" %self.size)

object1 = MyClass()
object1.setName()
object1.setColor("Blue")
object1.showObject()
