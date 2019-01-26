import random

def getAnswer(answerNumber):
    retVal = ''
    if answerNumber == 1:
        retVal = 'It is certain'
    elif answerNumber == 2:
        retVal = 'it is decidely so'
    elif answerNumber == 3:
        retVal = 'Yes'
    elif answerNumber == 4:
        retVal = 'Reply hazy try Again'
    elif answerNumber == 5:
        retVal = 'Ask again Later'
    elif answerNumber == 6:
        retVal = 'Concentrate and ask again'
    elif answerNumber == 7:
        retVal = 'My reply is no'
    elif answerNumber == 8:
        retval = 'Outlook not so good'
    elif answerNumber == 9:
        retval = 'Very Doubtful'
    return retVal

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

        
        
