people = 40
cars = 30
trucks = 15


if cars > people: #branch in code, evaluates cars and people
    print ("We should take the cars.")
elif cars < people: #if previous statement is false, moves to this statement.
    print ("We should not take the cars.")
else: #if neither of the previous are true, prints else ("We can't decide")
    print ("We can't decide.")

if trucks > cars: #branch in code. evaluates trucks and cars
    print ("That's too many trucks.")
elif trucks < cars: #if previous statement is false, moves on to this statement.
    print ("Maybe we could take the trucks.")
else: #if neither of the following statements are true, prints else ("We still can't decide")
    print ("We still can't decide.")

if people > trucks: #branch in code. Evaluates people and trucks.
    print ("Alright, let's just take the trucks.")
else: #if the above statement is false, prints else ("Fine, let's stay home then.")
    print ("Fine, let's stay home then.")
