class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
        name: a string representing the customer's name.
        balance: A float tracking the current balance of the customer's account
    """

    def __init__(self, name, balance = 0.0): #this initializes a new customer
        """Return a customer object whose name is *name* and starting balance is *balance*"""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* of dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance = self.balance - amount
        return self.balance #returns balance for person

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance = self.balance + amount
        return self.balance

customer1 = Customer("Erich Purpur", 1000)  #this actually creates a customer with a name (Erich Purpur) and a balance (1000)
print ("Balance before", customer1.balance)
customer1.deposit(1000)
print ("Balance now", customer1.balance)
