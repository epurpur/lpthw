print ("""Today is a beautiful day to climb.
Now you just have to decide where to go today.
It depends on the weather and your goals.

Are you fat or fit today?""")

fat_or_fit = input("> ")

if fat_or_fit == "fat":
    sendingtemps = input("""Well, you had better go trad climbing then.
    Is the weather good?  yes or no> """)

    if sendingtemps == "yes":
        print ("Go to Ship Rock today.")
    elif sendingtemps == "no":
        print ("You could drive to Rumbling Bald. Or go to the gym. Sorry.")

elif fat_or_fit == "fit":
    print ("Great! You trained hard. So what is the temperature today?")

    sendingtemps = int(input("> ")) #like functions, variable names are independent inside elif statements
    if sendingtemps <= 45:
        print ("You should go bouldering. I know you have many projects. Has it rained recently?")
        wetness = input("yes or no? ")
        if wetness == "yes":
            print ("Go to Blowing Rock or Lost Cove.")
        elif wetness == "no":
            print ("Go to Grandmother.")
        else:
            print ("Climb in the gym today.")


    elif sendingtemps > 45:
        print ("Sport Climbing. Go to the dump.")
        gumbies = int(input("How many gumbies at the crag today?"))
        if gumbies >= 100:
            print ("Wait for tomorrow.")
        if gumbies < 100:
            print ("Give er hell.")

else:
    print ("Better luck next time.")
