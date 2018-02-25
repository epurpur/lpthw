#defines formatter with 4 curly brackets, allowing 4 replacement values
formatter = "{} {} {} {}"
#print, calls variable formatter, calls str.format() function and passes values 1 2 3 4 into curly brackets as defined in variable formatter
print (formatter.format(1, 2, 3, 4))
#print, calls variable formatter, and passes strings "one" "two" "three" "four" into curly brackets as replacement values
print (formatter.format("one", "two", "three", "four"))
#print, calls variable formatter, passes in True, False, etc in curly brackets
#True, False are special keywords representing the concept of true or false
print (formatter.format(True, False, False, True))
#print, calls variable formatter, calls str.format() function and passes variable formatter into curly brackets as values
#because formatter is defined as {}{}{}{}, is passes this variable in 4 times resulting in 16 brackets as the output
print (formatter.format(formatter, formatter, formatter, formatter))
#print, calls variable formatter, calls str.format(), adds string with text, uses comma to continue string on one output line
print (formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))
