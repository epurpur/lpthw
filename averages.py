"""
#mean
#different ways to do this

#
import numpy
numbers = [1, 5, 1]
print (numpy.mean(numbers))

#simplest way, but only useful if numbers don't change
def mean(a, b, c):
    average = (a + b + c)/3
    print (average)
mean(1, 5, 1)

#i dont like this one, what does ,1 mean?
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
print (mean([1,5,2]))

a = [1, 5, 1]
print (sum(a) / len(a))

#median
import statistics
items = median[1, 5, 1]
print (statistics.median(items))
"""
"""
# to do exponentiation this is the syntax below
print (5 **(2))

#syntax for square root
import math
print (math.sqrt(9))

#root mean squared = square all values, take average of squares, take square root of averages
#I'll do it the long way the first time to make sure I do it right.
a = 1
b = 5
c = 1
a = a**2
b = b**2
c = c**2
print ("a, b, c squared is:", a, b, c)
average =(a+b+c)/3
print ("Mean of a, b, c squared is:", average)
square_root = math.sqrt(average)
print ("Square root of average is:", square_root)
print ("Final answer is", square_root)
"""
import math
#now a little more elegant way
#numbers = (1, 5, 1)
def func1(a, b, c):
    print (f"We will now square {a}, {b}, {c} and add them")
    y = (a**2) + (b**2) + (c**2)
    print (f"y = ", y)
    x = y/3
    print ("x = ", x)
    z = math.sqrt(x)
    print ("z = ", z)
    return z
func1(1, 5, 1)







#print ("Mean should be",numpy.mean(numbers))

#def mean(x):
#    mean = numpy.mean(numbers)
#    return mean #have to return a value to use it later
#print ("Mean is:", mean(numbers))
#print (numbers)
