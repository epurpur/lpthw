
#defines types_of_people
types_of_people = 10
# defines x as "There are 10 types of people in the world. Calls types_of_people."
x = f"There are {types_of_people} types of people."

#defines binary
binary = "binary"
#defines do_not as "don't"
do_not = "don't"
#defines y as "Those who know binary and those who don't. Calls binary and do_not."
y = f"Those who know {binary} and those who {do_not}."

print ("")
#print variable x
print(x)
#print variable y
print(y)
#print, then calls variable x
print(f"I said: {x}")
#print, then calls variable y
print(f"I also said: '{y}'")
#defines hilarious as False
hilarious = False
print ("")
#defines joke_evaluation as "Isn't that joke so funny?! with empty bracket, allowing variable to be called in bracket"
joke_evaluation = "Isn't that joke so funny?! {}"
#prints joke_evaluation and uses format syntax to call hilarious variable which = false
#joke_evaluation allows hilarious because of open bracket in definition statement
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#adds w and e together, making a longer string
print (w + e)

weather = "no"
forecast = "The weather looks great. {}"
print (forecast.format(weather))
