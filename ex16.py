from sys import argv
#declares argv variable here. Must pass one variable for "filename"
script, filename = argv

print (f"We're going to erase {filename}.")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")
#asks for user input
input("?")

print ("Opening the file...")
#defines target as open, the filename you provided. 'w' is to enable you to write to that filename
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
#truncates target file
target.truncate()

print ("Now I'm going to ask you for three lines.")

#asks user for three lines, which will later be written to filename
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print ("I'm going to write these to the file.")
#writes line1, line2, line3 (which are user input) to filename. \n is for new line
#I don't yet understand how to do this in one line instead of 6.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()
