from sys import exit

print ("""Today you have a day off and get to climb at Seneca.
How good this day is depends on a lot of factors including weather, day of the week, etc.
There are 4 seasons in the year, please enter them below.
""")


def seasons_in_year():
    seasons = [] #creates new list, seasons
    for season in range(0, 4): #wants 4 seasons entered
        season = input("Enter a season: ") #user enters 4 seasons
        seasons.append(season) #appends each season to list (seasons)
    print (f"Choose from the following seasons: {seasons}")
    current_season()

#####HOW DO I GET USER TO CHOOSE FROM WHAT IS IN seasons_in_year LIST?
#https://github.com/wong2/pick/blob/master/README.md
# ImportError: cannot import name 'pick'
def current_season():
    season_now = input("Which season is it now? ")
    if season_now == ("winter"):
        print (f"Ok the season is {season_now}.")
        print ("That is why it is so cold outside.")
        winter_season() #jumps to winter_season
    elif season_now == ("spring"):
        print (f"Ok the season is {season_now}.")
        print ("That is why the flowers are blooming.")
        spring_season() #jumps to "sping_season"
    elif season_now == ("summer"):
        print (f"Ok the season is {season_now}.")
        print ("That is why I am so sweaty.")
        summer_season() #jumps to "summer_season"
    elif season_now == ("fall"):
        print (f"Ok the season is {season_now}.")
        print ("That is why the leaves are changing.")
        fall_season() #jumps to fall_season
    else:
        print ("Choose a valid season.")
        current_season() #goes back to top, forcing user to select valid season

def winter_season():
    print ("Good days are hard to come by at Seneca in the winter")
    winter_temps = int(input("What is the temperature today? "))
    if winter_temps <= 40:
        dead("Too Cold.") #jumps to dead(x)
    elif winter_temps > 40 and winter_temps <= 55:
        hot_or_cold = input("It is warm enough if there is sun. Is there sun? ")
        if hot_or_cold == "yes":
            sunny_days()#jumps to sunny_days
        elif hot_or_cold == "no":
            dead("Still too cold.")
        else:
            winter_season()
    else:
        print ("Warm enough.")

def summer_season():
WORK ON THIS, READING CONTENTS OF LIST
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekends = ["Saturday", "Sunday"]
    user_day = input("What day is it? ")
    if user_day = weekdays:
        print ("Weekdays")
    elif user_day == weekends:
        dead("too crowded")


def spring_season():
    route_list = open("senecaroutes.txt") #put file name in quotes
    print ("Choose one from the following list of routes.")
    print (route_list.read()) #reads contents of file
    route_choice = input("Which one do you want to climb? ")
    if route_choice != "Prune":
        route_occupied()
    else:
        trad_gear()

def trad_gear():
    print ("When you begin the route you have 10 pieces of gear. It is a long pitch, use them wisely.")
    pieces_of_gear = 10
    while pieces_of_gear > 0: #could also be done with for loop?
        print (f"You have {pieces_of_gear} pieces left.")
        pieces_of_gear = pieces_of_gear - 1
        if pieces_of_gear == 2:
            print ("Be careful you don't have much left!")
        if pieces_of_gear == 1:
            print ("Somehow, you were able to place your last piece, a pink tricam. Somewhere, Lee Carter is smiling.")
        if pieces_of_gear == 0:
            rap_station("Nice you made it, now time to rappel.")

def rap_station(x):
    print (x) #x calls rap_station() from last function (trad_gear)
    rap_knowledge = False

    while True:
        climber_skills = input("Do you know how to rappel? ")

        if climber_skills == "no":
            dead("You were stranded up top and had to be rescued.")
        elif climber_skills == "yes" and not rap_knowledge:
            print ("You rappel to the bottom.")
            rap_knowledge = True
        else:
            rap_station()
        more_routes = input("Do you want to climb another? ")
        if more_routes == "yes":
            spring_season()
        elif more_routes == "no":
            dead("You hike out.")
        else:
                dead("Your indecision is your downfall.")

def route_occupied():
    print ("Route is occupied, choose again \n")
    spring_season() #jumps back to spring_season

def sunny_days():
    print ("Ok, it is sunny enough to climb in the cold. Now let's find a route to climb.")
    classics = input("Have you climbed Soler? ")
    if classics == "yes":
        print ("Ok, look for another classic route")
    elif classics == "no":
        print ("Let's climb that first. It looks like the route is taken. ")
        waiting_game = input("Should we wait? ")
        route_taken = True
        while True:
            if waiting_game == "yes":
                print ("Ok, it shouldn't take too long.")
                dead("We climbed the route and it was awesome.")
            elif waiting_game == "no":
                print ("I don't want to wait either. Maybe there is something we can do about that?")
                flying_object = input("You can throw a hex or a roll of tape at them, which do you choose? ")
                if flying_object == "hex":
                    route_taken = False
                    print ("Alright, we can climb it now!")
                    dead("We climbed the route and it was awesome.")
                elif flying_object == "tape":
                    dead("You waited in line all day.")
                else:
                    dead("Choose something I understand.")
    else:
        print ("You have either done it or not.")
        sunny_days()



def dead(x): #needs argument in dead(x).  Why? I think because dead() is called when finishing outcomes to end program. And this tells you why the outcome is so ex: "Too cold"
    print(x, "Your day is over.")
    exit()

#input("Which season is it now?: ")
#if current_season =

#else: print ("That is not a current season")

#seasons_in_year()
#current_season()
#winter_season()
#sunny_days()
#spring_season()
#trad_gear()
summer_season()
