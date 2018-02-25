"""
animals = ['bear', 'tiger', 'penguin', 'zebra']
print (animals[0])

numberslist = [1, 2, 3, 4, 5, 6, 11, 13, 16, 22]
print (numberslist[1:5])
print (numberslist[6:])
print (len(numberslist))

total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done' : break #escape code. when user types 'done' the program ends
    value = float(inp) #turns user input into floating point decimal
    total = total + value #adds user input to total
    count = count + 1  #adds 1 to count

print (f"Total is {total}, Count is {count}")  #prints total and count



numlist = []   #starts with empty list numlist[]
while (True) :
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)      #makes variable value = floating point of user input
    numlist.append(value)   #appends value to numlist (which is empty list)

average = sum(numlist) / len(numlist)  #calculates average as the sum of the numlist divided by length of numlist
print ("Average: ", average)



rocks = open("mbox-short.txt")
for line in rocks:
    if not line.startswith('From ') : continue
    words = line.split()
    print (words[2])



from sys import argv
script, filename = argv

txt = open(filename)
print (f"Here is your file {filename}")
print (txt.read())



readfile = open("ex15_sample.txt")
print (readfile.read())
"""

read_desktop = open("/Users/ep9k/Desktop/ex15_sample.txt") #reads file from other location on computer. Destop in this case. Uses relative path to locate file.
print (read_desktop.read())
