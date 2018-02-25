import sys
script, encoding, error = sys.argv
#defines main with 3 arguments
def main(language_file, encoding, errors):
    line = language_file.readline() #reads one line from language files it is given.

    if line: #IF statement lets you make decisions about your code, test the truth of a variable, and based on that truth run more code or not.
        #here, we are testing whether line has something in it. as long as readline gives us something, this is true and next lines run. If false, python skips next lines
        print_line(line, encoding, errors) #calls seperate function to print this line.
        return main(language_file, encoding, errors) #calls main again inside main. This jumps back to top of main function and runs code again. Runs in loop until if statement is false.
#defines print_line which does actual encoding of each line from languages.txt file
def print_line(line, encoding, errors):
    next_lang = line.strip() #strips invisible \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors=errors) #takes whats in languages.txt and encode it into raw bytes. next_lang is a string so to get raw bytes, must call .encode(). Must pass to .encode() the encoding I want and how to handle errors.
    cooked_string = raw_bytes.decode(encoding, errors=errors) #raw_bytes is bytes, so I call .decode() on it to get a string. The string should be the same as next_lang.
#On the left are numbers for each byte of the UTF-8 shown as raw_bytes, on the right side are cooked_string so we can see them in the terminal
    print (raw_bytes, "<====>", cooked_string) #prints both out to show you what they look like.
#languages defined as open languages.txt file with UTF-8 encoding
languages = open("languages.txt", encoding="utf-8")
#calls main function with correct parameters to kick-start loop. In main function, the if statement keeps function from looping forever.
main(languages, encoding, error)
