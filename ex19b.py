def testmath(a, b):
    print ("I'm going to do a little math with this function")
    print ("First I need to get some input from the user")
    userage = input("What is your age?: ")
    userweight = input("What is your height?: ")
    print (f"User age is {a}, user weight is {b}")

testmath(5, 2)
print ("Haha I fooled you. It doesn't matter what you write, yet.")

#this actually confused me. Because I called testmath again, it asks for age and weight a 3rd time.
print ("Ok, I'll return your real age and weight to you now. Please type it one more time.")
realage = int(input("Your age: "))
realweight = int(input("Your weight: "))
totalnumber = realage + realweight
testmath(realage, realweight)


print ("Last I will do some math with your measurements")
print ("your total score of age + weight is:", totalnumber)
