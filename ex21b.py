#defines heightcm_to_heighm with argument a
def heightcm_to_heighm(a):
    meters = a / 100 #divides cm by 100 to get m
    print (f"Your height in meters is {meters}m")

#you want to ask for input outside function. Converts input to floating point
a = float(input("Enter your height in cm: "))
heightcm_to_heighm(a) #prints heightcm_to_heighm with argument a

#divides a by 2
divide2 = a/2
print (divide2) #prints a/2





#bitcoin_to_usd function defined with argument btc for bitcoin amount
#def bitcoin_to_usd(btc):
#    amount = btc * 527 #amount is btc * 527
#    print(amount) #prints amount

#this works, but input only accepts integers
#btc = int(input("Input your bitcoin amount:"))
#this accepts floating point input from user
#btc = float(input("Input your bitcoin amount:"))

#bitcoin_to_usd(btc)
