#imports argv module
from sys import argv
#declares argv variables here. Must pass one variable for "filename"
script, filename = argv
#defines txt as open(filename). Will open whatever filename is entered in shell at beginning.
txt = open(filename)
#prints "Here is your file: and the filename you declared"
print (f"Here's your file {filename}:")
#calls txt variable, gives it a command (.read). This reads the filename you have opened.
print (txt.read())

print ("Type the filename again:")
#defines file_again as your input
file_again = input("> ")
#defines txt_again to open whatever you entered for file_again
txt_again = open(file_again)
#prints the contents of txt_again, (.read) command reads contents of txt_again
print (txt_again.read())
txt_again.close()
