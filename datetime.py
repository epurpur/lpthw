"""
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

printme("String Here")

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
#print ("Values outside the function: ", mylist)
"""

#Im going to write a sentence passing in values as arguments
def func1(a, b, c):
    answer1 = (a**2) + (b**2) + (c**2)
    return answer1
result1 = func1(1, 5, 1)
print (result1)
#print (func1(1, 5, 1))

def func2(answer1):
    answer2 = answer1 / 3
    return answer2
result2 = func2(result1)
print (result2)

def func3(answer1):
    answer3 = answer1 + 500
    return answer3
result3 = func3(result1)
print (result3)

def func4(answer2):
    answer4 = answer2 + 1
    return answer4
result4 = func4(result2)
print (result4)

def func5(answer1, answer2):
    answer5 = answer1/answer2
    return answer5
result5 = func5(result1, result2)
print (result5)
