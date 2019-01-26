#! python3
#phoneAndEmail.py Finds Phone and Email addresses on the clipboard.

import pyperclip, re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      #area code
    (\s|-|\.)?              #delimiters
    (\d{3})?                #first 3 digits
    (\s|-|\.)?              #seperator
    (\d{4})?                #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)
#123@gmail.com
#ghagsh123@g.co.in
#^[a-zA-Z0-9\._-]+@[a-zA-Z0-9]*\.+[a-zA-Z\.]{2,5}
emailRegex = re.compile(r'''(
    ([a-zA-Z0-9._-%+])       #first part
    (+@)                    #@ symbol
    ([a-zA-Z0-9]*\.)        #domain 
    (+[a-zA-Z\.]{2,5})?     #.com or co.in
)''', re.VERBOSE)




