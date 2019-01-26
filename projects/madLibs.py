#! python3
# madLibs.py reads in text files and lets the user add their own text anywhere the word ADJECTIVE,
# NOUN, ADVERB, or VERB appears in the text file

import re

fileReader = open('madlibs.txt','r')

fileContents = fileReader.read()
fileReader.close()
pattern1 = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')

matches = pattern1.findall(fileContents)


if matches != None:
    for pattern in matches:
        if pattern == "ADJECTIVE":
            AdjVal = input('Enter an adjective:')
            adjRegex = re.compile(r'ADJECTIVE')
            fileContents = adjRegex.sub(AdjVal, fileContents)
        elif pattern == "NOUN":
            nounVal = input('Enter a noun:')
            nnRegex = re.compile(r'NOUN')
            fileContents = nnRegex.sub(nounVal, fileContents)
        elif pattern == "ADVERB":
            adverbVal = input('Enter a adverb:')
            advrbRegex = re.compile(r'\bADVERB\b')
            fileContents = advrbRegex.sub(adverbVal, fileContents)
        elif pattern == "VERB":
            verbVal = input('Enter a verb:')
            vrbRegex = re.compile(r'\bVERB\b')
            fileContents = vrbRegex.sub(verbVal, fileContents)

    fReader = open('madlibs.txt','w')
    fReader.write(fileContents)
    fReader.close()
else:
    print("No Text Found")



