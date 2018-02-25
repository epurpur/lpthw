class Customer(object): #doesn't create a new customer yet. We've only defined a customer
    """A customer of ABC bank with a checking account. Customers have
    the following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account
    """
    def __init__(self, name, balance=0.0): #init used to initialize objects
        """Return a customer object whose name is *name* and starting balance is *balance*."""
        self.name = name #this allows us to say jeff for self. jeff is a fully initialized object.
        self.balance = balance #this allows us to say balance for balance.

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars"""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount #subtracts from previous balance
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars"""
        self.balance += amount #adds to previous balance
        return self.balance

jeff = Customer('Jeff Knupp', 1000.0) #creates customer jeff with name 'Jeff Knupp' and balance 1000.0
    #use customer blueprint to create me a new object I'll refer to as jeff
    #jeff is an instance of customer. This is the realized version of the customer class.

jeff.withdraw(100.0) #jeff (self) is the instance. Withdraw 100.0 from Amount
#could also be written customer.withdraw(jeff, 100)
