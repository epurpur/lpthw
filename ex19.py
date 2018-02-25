#defines function as cheese_and_crackers with 2 arguments, cheese_count and boxes_of_crackers. Function prints 4 lines.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {boxes_of_crackers} boxes of crackers!")
    print ("Man, that's enough for a party!")
    print ("Get a blanket.\n") #\n prints new line
    #print ("") could use this instead of \n

print ("We can just give the function numbers directly:")
cheese_and_crackers(20,30) #passes 20 for cheese_count and 30 for boxes_of_crackers. Prints them because that is what the function does

print ("OR, we can use variables from our script:") #defines 2 new variables with values. amount_of_cheese and amount_of_crackers
amount_of_cheese = 10
amount_of_crackers = 50

#calls cheese_and_crackers with arguements amount_of_cheese and amount_of_crackers which have been defined above as 10 and 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calls cheese_and_crackers and defines arguments as math problems (10 + 20) and (5 + 6)
print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#calls cheese_and_crackers and combines math with variables amount_of_cheese and amount_of_crackers
print ("and we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print ("Or I can ask the user how many cheese and crackers there should be.")
askcheese = input("How much cheese should we have?")
cheese_and_crackers(askcheese, 25)
