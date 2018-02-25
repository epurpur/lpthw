from sys import exit

def gold_room(): #the way it is now, number must be 0, 1, 50 or program thinks I didn't type a number. why?
    print ("This room is full of gold. How much do you take?")

    choice = int(input("> "))
    if choice <= 1:
        print ("Nice, you're not greedy! You win!")
        exit(0)
    elif choice > 1 and choice <= 50:
        print ("That is a reasonable amount to take.")
        exit(0)
    elif choice > 50:
        print ("You greedy bastard!")
        dead("There is a special place in hell reserved for the greedy.")
    else:
        dead("Man, learn to type a number")

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

    while True: #why "while true" here? The while loop won't run correctly without it. Zed says: this makes an infinite loop.
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
    exit(0)

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

start() #even though functions are defined out of order, this starts program with start()
#gold_room()  #starts directly at gold_room()
