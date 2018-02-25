#defines add function with variables a and b
def add(a, b):
    print (f"ADDING {a} + {b}") #adds a + b
    return a + b #returns value of a + b, stores that value

def subtract(a, b):
    print (f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a, b):
    print (f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print (f"DIVIDING {a} / {b}")
    return a / b

print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print (f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle. In this puzzle the script takes the return value of one function and using it as the argument of another function.
print ("Here is a puzzle")
                                                            #math starts here, with iq/2 (50/2). Retuns value 50, then multiplies that and so on
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#print ("That becomes", what, "Can you do it by hand?")
print (f"That becomes: {what}  Can you do it by hand?")
