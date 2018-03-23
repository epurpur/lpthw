#mean funcction
def mean(a, b, c):
    average = (a + b + c)/3
    return average
mean_value = mean(1, 5, 1)
print ("Mean is", mean_value)

#median function
import statistics
def median(lst):
    median_num = statistics.median(lst)
    return median_num
median_value = median([1, 5, 1])
print ("Median is", median_value)

#Root-Mean-Squared functions
import math
def squares(a, b, c):
    #print (f"We will now square and add {a}, {b}, {c}.")
    x = (a**2) + (b**2) + (c**2)
    return x
a = 1
b = 5
c = 1
value1 = squares(a, b, c)
#print ("Answer is:", value1)

def mean(value1):
    #print ("Now we will take the average of value1.")
    y = value1/3
    return y
value2 = mean(value1)
#print ("Answer is:", value2)

def square_root(value2):
    #print ("Now we import the math module and find square root.")
    z = math.sqrt(value2)
    return z
rms_value = square_root(value2)
print ("RMS is:", rms_value)

def middle_averages(lst):
    final_average = statistics.median(lst)
    return final_average
final_average = middle_averages([mean_value, median_value, rms_value])
print ("Middle averages = ", final_average)
