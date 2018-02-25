name = 'Erich M. Purpur'
age = 30 #not a lie
height = 69 #inches
weight = 150 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Bald'


print ("")
print (f"Let's talk about {name}.")
print (f"He's {height} inches tall.")
#print (f"In metric he is {in_to_m} meters tall.)
print (f"He weighs {weight} pounds.")
print ("Actually that's not too heavy.")
print (f"He's got {eyes} eyes and a {hair} head.")
print (f"He has {teeth} teeth because he doesn't drink coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.")
print ("")
#metric measurements here
weightkg = weight / 2.2 #I can add variables later in the code.
heightm = height * .0254 #Not all variables need to be defined at beginning.
print (f"Erich's weight in Kilograms is {weightkg}")
print (f"Erich's height in Meters is {heightm}")

metrictotal = weightkg + heightm
print (f"Erich's metric total number is {metrictotal}")
print ("Erich's metric total number is", metrictotal,)
