import random

num = random.randrange(1, 100)
num_of_tries = int(input("Input number of guesses: "))
print (f"You have {num_of_tries} guesses.")
user_guess = int(input("Guess a number between 1 and 100: "))
while user_guess != num: #this loops while number is incorrect
    num_of_tries -= 1
    print (f"You have {num_of_tries} tries.")
    if num_of_tries == 0:
        print ("You lose")
        break
    if user_guess < num:
        print ("Higher")
        user_guess = int(input("Guess a number between 1 and 100: "))
    else:
        print ("Lower")
        user_guess = int(input("Guess a number between 1 and 100: "))
if user_guess == num:
    print ("You win")



#def guess:
    #user makes a guess


#def decisions:
    #decides whether guess is correct or not

"""
num = random.randrange(1, 100)
user_guess = int(input("Enter number: "))
for i in range(user_guess, 0, -1):
    if user_guess > num:
        print ("Lower")
    elif user_guess < num:
        print ("Higher")
    elif user_guess == num:
        print ("Winner!")
        break
"""
