ten_things = "Apples Oranges Crows Telephone Light Sugar"
print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') #splits words in ten_things into list items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: #looks at length of list, "stuff", while this list is not equal to 10....
    next_one = more_stuff.pop()  #pops last item off list in more_stuff. pop() not needed in for loop
    print ("Adding: ", next_one) #adds next item in list
    stuff.append(next_one) #appends last item in list to stuff, which is ten_things split
    print (f"There are {len(stuff)} items now.") #tells user how many items are in list now

print ("There we go: ", stuff) #now that there are 10 items in list, prints list stuff

print ("Let's do some things with stuff.")

print (stuff[1]) #prints first item in stuff
print (stuff[-1]) #prints last item in stuff
print (stuff.pop()) #pops off and prints last item in stuff
print (' '.join(stuff)) #joins all items in stuff into one list
print ('#'.join(stuff[3:5])) #joins items 3 and 4 with a hashtag Telephone#Light. This is a "slice" of the list.
