
sentence = ("this is a new test sentence to work with.")


def break_words(stuff):
    """This function will break up words for us.""" #if used help(ex25.break_words) """comments""" are shown
    words = stuff.split(' ') #splits words up individually
    return words #returns the words

def sort_words(words):
    """Sorts the words.""" #sorts in descending order
    return sorted(words) #returns words sorted

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) #removes word in 0 position in list ("all")
    #return (word) #prints that word
    print (word) #when using this instead of return, returns word but also "none" after it. Why?

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #removes last word from list (-1 position). Instead of counting words, goes backwards with -1
    #return (word) #prints that word
    print (word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #defines words as break_words, which splits the words from sentence ("all good things...")
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) #defines words as break_words, which splits the words from sentence ("all good things...")
    print_first_word(words) #takes words(defined above) as argument, calls print_first_word as argument which pops off first word. ("all")
    print_last_word(words) #takes words(defined above) as argument, calls print_last_word as argument which pops off last word. ("who"). Not wait, because words are sorted in descending order

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) #defines words as split words from sentence. called in sort_sentence and in break_words
    print_first_word(words) #prints first word from split sentence ("all")
    print_last_word(words) #prints last word from split sentence ("who")

quod = break_words(sentence)
#print (quod)
misty7 = sort_words(quod)
#print (misty7)
#print (print_first_word(quod))
#print (print_last_word(quod))
#print (quod)
rodeo10 = sort_sentence(sentence)
#print (rodeo10)
print (print_first_and_last(sentence))





#start python module by running "python3.6" in shell
"""
import ex25 - #imports file ex25
sentence = "All good things come to those who wait."    #this is the sentence, used as argument later
words = ex25.break_words(sentence)                      #defines words as break the words in ex25 sentence "all good things..."
words                                                   #prints words, which are already broken by last line
sorted_words = ex25.sort_words(words)                   #defines sorted_words as ex25 sorted words in sentence "all good things..."
sorted_words                                            #prints sorted words (in descending order)
ex25.print_first_word(words)                            #pops first word off list and prints it ("all"). Adds it to sorted_words
ex25.print_last_word(words)                             #pops last word off list and prints it ("wait."). Adds it to sorted_words
words                                                   #prints words again without first and last
ex25.print_first_word(sorted_words)                     #pops off and prints first word from sorted list, ("all")
ex25.print_last_word(sorted_words)                      #pops off and prints last word from sorted list, ("who"). Who instead of wait because words are sorted in descending order, instead of split into a list.
sorted_words                                            #prints sorted_words list again, without first and last words, which have been popped off
sorted_words = ex25.sort_sentence(sentence)             #starts again with sorted_sentence. words are sorted instead of split this time.
sorted_words                                            #prints sorted words list
ex25.print_first_and_last(sentence)                     #pops off and prints first and last word from sorted words list.
ex25.print_first_and_last_sorted(sentence)              #prints the two words that have been popped off ("all", "who")
"""
