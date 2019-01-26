# python3
# statesAndCapitalsQuiz.py creates quizzes with questions and answers in random order, along with answer key

import random

statesList = {
    'Andhra Pradesh': 'Amravathi',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar':'Patna',
    'Chhattisgarh':'Raipur',
    'Goa':'Panaji',
    'Gujarat':'Gandhinagar',
    'Haryana':'Chandigarh',
    'Himachal Pradesh':'Shimla',
    'Jammu & Kashmir':'Srinagar (Summer) Jammu (Winter)',
    'Jharkhand':'Ranchi',
    'Karnataka':'Bangalore',
    'Kerala':'Thiruvananthapuram',
    'Madhya Pradesh':'Bhopal',
    'Maharashtra':'Mumbai',
    'Manipur':'Imphal',
    'Meghalaya':'Shillong',
    'Mizoram':'Aizawl',
    'Nagaland':'Kohima',
    'Odisha': 'Bhubaneshwar',
    'Punjab': 'Chandigarh',
    'Rajasthan':'Jaipur',
    'Sikkim':'Gangtok',
    'Tamil Nadu':'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura':'Agartala',
    'Uttar Pradesh':'Lucknow',
    'Uttarakhand':'Dehradun',
    'West Bengal':'Kolkata'
}

#create quiz for n number of students
for quizNumbers in range(5):

    quizQueFile = open('quizQueFile_%s.txt' % (quizNumbers + 1),'w')
    quizAnsFile = open('quizAnsFile_%s.txt' % (quizNumbers + 1),'w')

    quizQueFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizQueFile.write(" "*20 + 'State Capitals quiz (Form no %s)' % (quizNumbers+1))
    quizQueFile.write('\n\n')

    states = list(statesList.keys())
    random.shuffle(states)

    for questionNum in range(29):
        correctAnswer = statesList[states[questionNum]]

        wrongAnswers = list(statesList.values())
        del(wrongAnswers[wrongAnswers.index(correctAnswer)])

        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]

        random.shuffle(answerOptions)

        quizQueFile.write("\n%s. What is the captial of %s?\n\n" % ((questionNum + 1), states[questionNum]))
        for i in range(4):
            quizQueFile.write('%s. %s' % ('ABCD'[i], answerOptions[i]))
            quizQueFile.write('\n')

        quizAnsFile.write('%s. %s %s\n' % ((questionNum+1), 'ABCD'[answerOptions.index(correctAnswer)], correctAnswer))

quizQueFile.close()
quizAnsFile.close()

