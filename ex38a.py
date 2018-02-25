ten_things = "Apples Oranges Crows Telephone Light Sugar"
print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') #splits words in ten_things into list items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
"""
while len(stuff) < 10: #while loop makes more sense in my head than for loop.
    next_one = more_stuff.pop()
    print ("adding: ", next_one)
    stuff.append(next_one)
    print (f"There are {len(stuff)} items now.")
"""
print ("There we go: ", stuff)

for items in stuff: #same as while loop but with for loop. Not sure if this is easier or harder than while loop.
    next_one = more_stuff.pop()
    print ("adding: ", next_one)
    stuff.append(next_one)
    print (f"There are {len(stuff)} items now.")
    if len(stuff) == 10 : break
