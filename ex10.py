#\t makes tab indent
tabby_cat = "\tI'm tabbed in."
#\n puts a new line between split and on
persian_cat = "I'm split\non a line."
#\\ is how to include a backslash character
backslash_cat = "I'm \\ a \\ cat."
#in triple quotes you can quite as many lines of text as you want before ending with another triple quote
#for catnip and grass, \n\t is new line, tab indent
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
#backspace deletes one character (output aaa aaa)
print ("aaaa\b aaa")
#formfeed advances downward to next "page". Acts as page break
print ("aaaa\f aaa")
#vertical tab.  Maybe not useful any more?
print ("aaaa\v aaa")
#carriage return. characters on right move to left and replace existing text
print ("aaaa\r aaab")
