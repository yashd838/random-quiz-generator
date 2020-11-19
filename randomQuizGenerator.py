# python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# the quiz data.keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hwaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesoa': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson city', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Caeson city', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
                'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
                'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
                'Columbia', 'South Dakota': 'Pierre', 'Tennesse': 'Nashville', 'Texas': 'Austin', 'Utah':
                'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Medison', 'Wyoming': 'Cheyenne'}

# Generates 35 quiz files
for quiznum in range(1):
    # TODO: Create the quiz and answer key files.
    quizfile=open('capitalsquiz%s.txt' % (quiznum+1), 'w')
    answerkeyfile=open('capitalquiz_answers%s.txt' % (quiznum+1), 'w')

    # TODO: Write out header for the quiz.
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((''*20)+ 'State Capitals Quiz (Form %s)' % (quiznum+1))
    quizfile.write('\n\n')

    # TODO: Shuffle the order of states.
    states=list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        #Get right and wrong answers.
        correctanswer = capitals[states[questionNum]]
        wronganswers= list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers = random.sample(wronganswers, 3)
        answeroptions= wronganswers + [correctanswer]
        random.shuffle(answeroptions)

        # TODO: Write question and answer option to quiz file.
        quizfile.write('%s. What is the capital of %s ?\n' % (questionNum+1, states[questionNum]))
        for i in range(4):
            quizfile.write('    %s. %s\n' % ('ABCD'[i],answeroptions[i]))
        quizfile.write('\n')

        # TODO: Write a answer key to a file.
        answerkeyfile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answeroptions.index(correctanswer)]))

    quizfile.close()
    answerkeyfile.close()

