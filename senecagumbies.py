print ("""You are going climbing at Seneca today. You plan to crush, but how many gumbies will get in the way?
You will find out based on the following information.""")

day_of_week = input("Is today a weekday or weekend?  > ")

if day_of_week == "weekday":
    print ("You lucky dog, there will be fewer gumbies today.")

    climbingseason = input("Which season is it? spring, summer, fall, winter  > ")
    if climbingseason == "winter":
        todaysweather = input("Is today's weather good or bad?  >")
        if todaysweather == "good":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .001
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%. You will probably be cold on the wall.")
        elif todaysweather == "bad":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .01
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%.")

    elif climbingseason == "spring":
        todaysweather = input("Is today's weather good or bad?  >")
        if todaysweather == "good":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .001
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%. Maybe you'll find an easter egg?")
        elif todaysweather == "bad":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .01
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%.")

    elif climbingseason == "summer":
        todaysweather = input("Is today's weather good or bad?  >")
        if todaysweather == "good":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .001
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%. The likelihood of sunburn is high.")
        elif todaysweather == "bad":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .01
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%.")

    elif climbingseason == "fall":
        todaysweather = input("Is today's weather good or bad?  >")
        if todaysweather == "good":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .001
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%. The fall colors are out today.")
        elif todaysweather == "bad":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .01
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%.")

    else:
        print ("You fail, not a valid season.")

elif day_of_week == "weekend":
    holiday = input("Is this a holiday weekend? yes or no  >")
    if holiday == "yes":
        print ("Cannot compute values. Too many gumbies. Abort mission. May god have mercy on your soul.")
    elif holiday == "no":
        todaysweather = input("Is today's weather good or bad?  >")
        if todaysweather == "good":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .005
            hexes = gumbies * 6
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%.")
        elif todaysweather == "bad":
            cars = int(input("How many cars do you see in the parking lot?  > "))
            gumbies = cars
            accidents = gumbies * .01
            hexes = gumbies * 4
            print (f"Today there will be {gumbies} gumbies, {hexes} hexes, and the likelyhood of an accident is {accidents}%.")

else:
    print ("You fail, it can only be a weekday or weekend.")
