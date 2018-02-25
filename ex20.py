#imports argv module
from sys import argv
#declares argv variables here. Must pass one for input_file
script, input_file = argv
#defines print_all function with one argument, f
def print_all(f):
    print(f.read()) #reads and prints contents of f
#defines function rewind with one argument (f)
def rewind(f):
    f.seek(0) #seek() defines where the code begins in the file. seek(0) moves file to 0 byte or first byte, in file. pydoc file.seek for more documentation
#defines function print_a_line with 2 arguments line_count and f
def print_a_line(line_count, f):
    print(line_count, f.readline())#prints linecount, and reads lines in f
    print("")
#defines variable current_file as opens input_file
current_file = open(input_file)
#prints this string with \n new line
print("First let's print the whole file:\n")
#calls function print_all with argument current_file. current_file opens input_file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#calls rewind with argument current_file. current_file opens input_file
rewind(current_file)

print("Let's print three lines:")
#defines current_line as 1
current_line = 1
#calls print_a_line with arguments current_line and current_file
#each time print_a_line is runs, you are passing in variable current_line. current_line is passed as first argument which is line_count. current_line begins = 1
print_a_line(current_line, current_file)
#defines current_line as current_line + 1, or next line in file
#I'm not sure about the += yet. 
current_line += current_line
print_a_line(current_line, current_file)
#same thing as above, but next line in file again
current_line += current_line
print_a_line(current_line, current_file)
