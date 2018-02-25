#write one function "creepy" with 2 arguments, the ages of 2 people.
#it should return "False" if the 2 may date without being creepy
#it should return "True" if dating would be creepy
#Return the boolean value True or False
#it is possible to use if statements, but not encouraged
#this should work for ages > 14

#using if/else statement
"""
def creepy(firstage, secondage):
    low_end_younger = int((firstage / 2) + 7)
    high_end_younger = int((firstage * 2) - 13)
    if secondage >= low_end_younger and secondage <= high_end_younger:
        print ("They may date")
    else:
        print ("Not allowed")

creepy(20, 30)
"""
#not using if/else statement
def creepy(firstage, secondage):
    low_end_younger = int((firstage / 2) + 7)
    high_end_younger = int((firstage * 2) - 13)
    print (secondage >= low_end_younger and secondage <= high_end_younger)

creepy(20, 21)
#a = 2
#b = 3
#newvar = 2>3
#print (newvar)
