"""
class Wallet(object):
    def __init__(self):
        self.credits = 0

    def add_to_total(self, amount):
        self.credits = self.credits + amount
        #self.total += amount

wallet = Wallet()
wallet.add_to_total(5)
print (wallet.credits)
wallet.add_to_total(10)
print (wallet.credits)
"""

class Wallet(object):
    credits = 0
    def __init__(self, amount):
        Wallet.credits += amount
        print (Wallet.credits)

add1 = Wallet(5)


"""
class CreditCount(object):
    def __init__(self):
        #why not (self, total)?
        self.total = 0

    def add_to_total(self, amount):
        #self.total += amount
        self.total = self.total + amount
        print (self.total)

cc = CreditCount() #is this step necessary?  Yes it is necessary!
cc.add_to_total(1)
#print (cc.total)
cc.add_to_total(4)
#print (cc.total)
cc.add_to_total(10)
"""
