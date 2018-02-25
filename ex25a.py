
sentence = ("this is a new test sentence to work with.")


def break_words(stuff):
    """This function will break up words for us.""" #if used help(ex25.break_words) """comments""" are shown
    words = stuff.split(' ') #splits words up individually
    return words #returns the words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints first word after popping it off"""
    word = words.pop(0)
    print (word)

quod = break_words(sentence)
#print (quod)

double12 = sort_words(quod)
print (double12)

print (print_first_word(quod))
