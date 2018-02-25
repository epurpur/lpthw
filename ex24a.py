#mathproblem = 10 * 10 % 3
#print (mathproblem)


#I will determine the amount of available_routes, accidents, and hexes based on amount of gumbies_at_seneca given by the user
def gumbymath(seneca):
    available_routes = gumbies_at_seneca / 2
    accidents = gumbies_at_seneca * .001
    hexes = gumbies_at_seneca * 4
    return available_routes, accidents, hexes


"""
gumbies_at_seneca = int(input("How many gumbies are there today?: "))
a, b, c = gumbymath(gumbies_at_seneca)

print (f"Today at seneca there are {gumbies_at_seneca} gumbies, {a} routes, {b} accidents, and {c} hexes.")
"""

"""
weather = True
goodweather = "The weather is good today! {}" #with empty bracket, allowing variable to be called in bracket"
#prints goodweather and uses format syntax to call weather variable which = false
#goodweather allows weather because of open bracket in definition statement
print (goodweather.format(weather))
"""

"""
forecast = str(input("What is the temperature today?: "))
if forecast == "warm": #needs == to accept string
    print ("Lets go climbing!")
if forecast == "hot":
    print ("Lets climb in the shade")
else:
    print ("Lets do something else today.")
"""

gumbyforecast = int(input("How many gumbies are there today? "))
if gumbyforecast > 100:
    gumbymath(gumbyforecast)
    print (f"Total Gumbies: ")
else:
    print ("Go climbing")
