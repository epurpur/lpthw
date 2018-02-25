#from sys import argv
#script, filename = argv

#txt = open(filename)

#print (f"Here's your file {filename}: ")
#print (txt.read())

#this time I am using input() to get filename from user, instead of argv


filename = input("Enter a filename: ")
txt = open(filename)
print (f"Here's your file {filename}:")
print (txt.read())
txt.close()

#Why is this method better? I assume this method is better if this is a
#user facing program. If the creator is giving input directly in shell then
#argv works. If the user is giving input via a form or something, input() is better.
