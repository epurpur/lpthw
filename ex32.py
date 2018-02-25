the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


#this first kind of for-loop goes through a list
for number in the_count: #number is independent, can be named anything. Basically it is the argument in the for loop
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print (f"A fruit of type: {fruit}")

#we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print (f"I got {i}")

#we can also build lists, first start with an empty one
#elements = [1, 2, 3, 4, 5]
elements = []
#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print (f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i) #appends numbers 1-5 to elements[] list

#now we can print them out too
for i in elements: #looks at what is inside elements[] list
    print (f"Element was: {i}") #prints each element in list

Var1 = range(10, 20)
print (list(Var1)) #lists numbers 10 - 20 (horizontally)

for i in range(10,20):
    print (i) #prints numbers 10-20 (vertically, each on own line)

for i in range (0, 10, 3): #print 0 to 10 by 3s. Moves forwards
    print (i)

for i in range (0, -10, -2): #prints 0 to -10 by 2s. Moves backwards
    print (i)
