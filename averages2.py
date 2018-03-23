"""
import math

def squares(a, b, c):
    print (f"We will now square and add {a}, {b}, {c}.")
    x = (a**2) + (b**2) + (c**2)
    return x
a = 3
b = 5
c = 3
value1 = squares(a, b, c)
print ("Answer is:", value1)

def mean(value1):
    print ("Now we will take the average of value1.")
    y = value1/3
    return y
value2 = mean(value1)
print ("Answer is:", value2)

def square_root(value2):
    print ("Now we import the math module and find square root.")
    z = math.sqrt(value2)
    return z
value3 = square_root(value2)
print ("Answer is:", value3)
"""
d = "this"
def funcx(random):
    print (random, "function prints random words")
    return ("example", random)
print (funcx(d))

f = int(input("Enter Input: "))
def funcy(thismeansnothing):
    print ("The number you entered is: ", thismeansnothing)
    return thismeansnothing
print (funcy(f))

"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print (f"You have {cheese_count} cheeses!")
    if boxes_of_crackers == 1:
        print (f"You have {boxes_of_crackers} box of crackers.")
    else:
        print (f"You have {boxes_of_crackers} boxes of crackers")

print ("We can just give the function numbers directly")
cheese_and_crackers(20, 30)

print ("Or we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
cheese_and_crackers(10+ 20, 6-4)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
"""
