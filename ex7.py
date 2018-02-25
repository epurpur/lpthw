print("Mary had a little lamb.")
#I dont quite understand this yet. But it seems like the open bracket
#allows the format syntax to call a variable in the curly bracket.
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
#"." prints a dot. * 10 multiplies it by 10 and prints it 10 times.
print("." * 10) #What did that do?
print ("")

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# you can also multiply variables, for example, end1 here (C)
print (end1 * 10)
# here, the last statement continues the next print statement
# , end = '' continues the next print statement but on the same line
print(end1 + end2 + end3 + end4 + end5 + end6, end ='')
print(end7 + end8 + end9 + end10 + end11 + end12)

cheese = (end1 + end2 + end3 + end4 + end5 + end6)
burger = (end7 + end8 + end9 + end10 + end11 + end12)

print ("")
print (cheese + burger)
print ("")
print (cheese)
print (burger)
#here I learned that end is not specific to the variables I defined earlier (end1, etc.)
#, end = '' adds the next print statement to the current one. Just like ex: print (a + b)
print (cheese, end ='')
print (burger)
