#for i in range(10, 20, 3): #can only accept 3 arguments or less. Not more
#    print (i)

#newlist = []
#for x in range(-5, 5):
#    newlist.append(x)
#    print (x)

#secondlist = []
#for y in range(-8, -2):
#    print (y) #append can come before or after print statement
#    secondlist.append(y) #append can come before or after print statement

elements = []
#then use the range function to do 0 to 5 counts. Loops first to last without including the last.
for i in range(0, 6):
    print (f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i) #appends numbers 1-5 to elements[] list

for i in elements: #looks at what is inside elements[] list
    print (f"Element was: {i}") #prints each element in list


BestList = ["one", "two", "three", "four"]
print (BestList)

greatlist = []
greatlist.append(["One", "Two", "Three"]) #appends strings to greatlist
print (greatlist)

mathlist = [] #appends user input to mathlist
mathlist.append(input("Write something> ")) #appends user input to list
mathlist.append(int(input("Write something else > "))) #requies integer as input
mathlist.append(str(input("Write something again > "))) #turns input into string
print (mathlist)


addlist = []
userinput = int(input("Write a number > ")) #define userinput as an interger input from user
addlist.append(userinput) #now I can add my variable userinput
addlist.append(userinput + -1) #now I can do math with my variable and user input
print (addlist)


lastlist = []
your_input = int(input("Write a number > "))
lastlist.append(your_input)
if your_input > 10: #if loop involving list
    print ("Big Number")
elif your_input <= 10:
    print ("Small number")

print (lastlist)
