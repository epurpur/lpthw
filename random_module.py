import random
"""
choice = int(input("Choose a number: "))
random_number = random.randint(0, 5) #random numbers between 0 and 4
print (f"Random number is: {random_number}")
if choice == random_number:
    print ("Winner")
else:
    print ("Loser")
"""
"""
a = ["facebook", "twitter", "myspace", "instagram", "snapchat"]
random.shuffle(a)
print (a)
"""
climbers = ["Sharma", "Ondra", "Megos", "Hukkataival", "Woods", "Webb", "Graham"]
#print (random.choice(climbers)) chooses one random item from list
num_to_select = 2
climbers_list = random.sample(climbers, num_to_select)
first_climber = climbers_list[0]
second_climber = climbers_list[1]

print (first_climber, second_climber)
