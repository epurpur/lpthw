#built my own variations onto ex35.py
from sys import exit

def gold_room(): #the way it is now, number must be 0, 1, 50 or program thinks I didn't type a number. why?
    print ("This room is full of gold. How much do you take?")

    choice = int(input("> "))
    if choice <= 1:
        print ("Nice, you're not greedy! You win!")
        exit()
    elif choice > 1 and choice <= 50:
        print ("That is a reasonable amount to take.")
        exit()
    elif choice > 50:
        print ("You greedy bastard!")
        print ("This is Cthulhu's gold!")
        toomuchgold()
    else:
        dead("Man, learn to type a number")

def toomuchgold(): #incorporates returns to other functions
    print ("You took too much!")
    truth = input("Did you really take more than 50? ")
    if truth == "yes":
        print ("Now you are returned to Cthulhu's room.")
        cthulhu_room()
    if truth == "no":
        print ("Lying is not good, but at least you aren't greedy.")
        gold_room()

#    if how_much < 50:
#        print("Nice, you're not greedy, you win!")
#        exit(0)
#    else:
#        dead("You greedy bastard!")

def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False
#TRY REPLACING WITH FOR LOOP
#I did not understand this while loop. Now I do. So we have defined bear_moved = False. While this is true, run the rest of the code.
#It doesn't matter that bear_moved = False. The while loop runs while this is true. Then if/elif other things happen it changes bear_moved to True, etc.
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door.")
            print ("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")

def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(x): #needs argument in dead(x).  Why? I think because dead() is called when finishing outcomes to end program. And this tells you why the outcome is so ex: "Bear chews your legs"
    print(x, "Now you die.")
    exit()

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

#start() #even though functions are defined out of order, this starts program with start()
#gold_room()  #starts directly at gold_room()
bear_room()
