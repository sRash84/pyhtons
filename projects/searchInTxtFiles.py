#! python3
# searchInTxtFiles opens all .txt files in a folder and searches for any line that matches a user-supplied
# regular expression.

import os
import re
pwd = os.getcwd()
fileandfolders = os.listdir(pwd)
filearray = list()
for files in fileandfolders:
    if os.path.isfile(files):
        txtRegex = re.compile(r'\.txt$')
        mch      = txtRegex.search(files)
        if mch != None:
            filehandler = open(files)

            fileContent = filehandler.read()
            fileRegex = re.compile(r'What.*of')
            matches = fileRegex.search(fileContent)
            if matches != None:
                print(matches.group())
            filehandler.close()

#print(filearray)

#print(fileandfolders)