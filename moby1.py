#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:41:59 2018

@author: ep9k
"""
mobyfile = open('mobydick.txt', encoding='utf-8')
mobylines = []
for line in mobyfile.readlines():
    line = line.strip()
    mobylines.append(line)
"""
startindex = 851
endindex = 21964 + 1

mobytxt = mobylines[startindex:endindex]

import re #importing for this purpose of creating regular expression
for i, line in enumerate(mobytxt):
    if re.search('^CHAPTER', line):
        mobytxt[i] = ' '

moby_bigline = ' '.join(mobytxt) #finds objects separated by spaces, operating on mobytxt
moby_bigline = moby_bigline.lower() #now that moby_bigline is string, lower cases everything
moby_bigline = re.sub(r'\W+', ' ', moby_bigline) #substitutes, finds pattern, replace with this pattern (2nd argument), in moby_bigline. in this case finds everything that is alphanumeric character, replace it with blankk
moby_bigline = re.sub(r'\s', ' ', moby_bigline) #replaces wierd spaces with single space.

moby_words = re.split(r'\s+', moby_bigline)
#moby_words = moby_bigline.split() #does same without re library

stops = []
for stop in open('stopwords.txt').readlines():
    stop = stop.strip()  #strips hard returns
    stops.append(stop)

for i, word in enumerate(moby_words):
    if word in stops:
        moby_words[i] = ''

moby_bigline = ' '.join(moby_words).strip()
moby_words = re.split(r'\s+', moby_bigline)

moby_words_counts = {}
for word in moby_words:
    if word in moby_words_counts:
        moby_words_counts[word] = moby_words_counts[word] + 1
    else:
        moby_words_counts[word] = 1

"""    
