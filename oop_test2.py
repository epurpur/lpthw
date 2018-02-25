import random #imports this module. randomizes words from WORD_URL
from urllib.request import urlopen #imports this module
import sys #imports this module

WORD_URL = "http://learncodethehardway.org/words.txt"  # provides URL which words will come from.
WORDS = []  #makes empty lists called WORDS

PHRASES = {            # a bunch of strings in a dictionary mapped to eachother. These are the instructions from last part of exercise
    "xxx is not real":
        "Choose *** instead",
    "All I hear is gun shots @@@":
        "Can I touch something *** what the blood clot"
}

# do they want to drill phrases first
PHRASE_FIRST = False #sets PHRASE_FIRST to false
if len(sys.argv) == 2 and sys.argv[1] == "spanish": #if length of argument is 2, and place 1 is "english", PHRASE_FIRST = True
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #reads lines in word_url
    WORDS.append(word.strip().decode("utf-8")) #appends words to WORDS. strips them, decodes them


def convert(snippet, phrase): #defines method convert with three lists: class_names, other_names, param_names.
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("xxx"))] #takes random sample of WORDS, capitalizes WORDS. counts number of xxx inside that key. class_names will be a random list of words in the size of the count of xxx
    other_names = random.sample(WORDS, snippet.count("***")) #defines other_names as a random list of WORDS in number of times *** occurs.
    results = []    #creates empty list results. results is a string
    param_names = []   #creates empty list param_names. param_names is a list of strings in the size of @@@ found. Each string consists of one, two, or three different words separated by ,(comma)

    for i in range(0, snippet.count("@@@")): #param_names is a list of strings in the size of the number of @@@ found
        param_count = random.randint(1,4)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names: #loops through class_names
            result = result.replace("xxx", word, 1) #replaces xxx with word

        # fake other names
        for word in other_names: #loops through other_names
            result = result.replace("***", word, 1) #replaces *** with word from WORD_URL

        # fake parameter lists
        for word in param_names: #param_names is a list of stings in the size of the number of @@@ found
            result = result.replace("@@@", word, 1) #replaces @@@ with word

        results.append(result) #appends these to results list

    return results #returns the results

# keep going until they hit CTRL-D
try:
    while True: #keep in mind this doesn't mean PHRASE_FIRST = True. It just means whether it is true or false, continue...
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER:  %s\n\n" % answer)
except EOFError:
    print("\nBye")
