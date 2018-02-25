from sys import argv
#read the WYSS section for how to run this

script, first, second, third = argv
#why does this line always return "ex13.py" no matter what I write as my variable? I think this is because ex13.py is my first argument
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
fourth = input("Write a fourth variable: ")
print (f"The fourth variable is: {fourth}")
