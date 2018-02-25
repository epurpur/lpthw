class Car(object):
    """Blueprint for car"""
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print ("started")
    def stop(self):
        print ("stopped")
    def accelerate(self):
        print ("accelerating...")
    def change_gear(self, gear_type):
        print (f"gear changed to {gear_type}")


suzuki = Car("ertiga", "black", "Suzuki", 60) #passes these arguments to suzuki for model, color, company, speed_limit
audi = Car("A6", "red", "Audi", 80) #does same for Audi.

suzuki.start()
audi.change_gear(2)
