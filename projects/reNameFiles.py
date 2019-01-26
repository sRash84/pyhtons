#! python3
# add a prefix to the start of the filename, such as adding spam_ to rename
# eggs.txt to spam_eggs.txt

import os, shutil,re

textRegex = re.compile(r'\.txt$')

for files in os.listdir('.'):
    matches = textRegex.search(files)
    if matches != None:
        newFilename = 'spam_'+files
        absWorkingDir = os.path.abspath('.')
        oldFileName = os.path.join(absWorkingDir, files)
        renameFile = os.path.join(absWorkingDir, newFilename)

        #renameFiles
        print('Renaming "%s" to "%s".....' % (oldFileName, renameFile))
        shutil.move(oldFileName, renameFile)

