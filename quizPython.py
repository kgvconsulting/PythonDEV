# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Program for Python Quiz

# welcome message
print("Welcome to Krasimir Vtachinsky Python Quiz\n")

# 0 the score
score = {
    'correct': 0,
    'incorrect': 0
}

# set the quiz dictionary of questions and coresponding answers
quizQuestions = [
    {
        'text': 'Which of the following function returns the max alphabetical character from the string str?',
        'answers': [
        {
            'key': "A",
            'text': "lower()",
            'correct': False
        },
        {
            'key': "B",
            'text': "lstrip()",
            'correct': False
        },
        {
            'key': "C",
            'text': "max(str)",
            'correct': True    
        },
        {
            'key': "D",
            'text': "min(str)",
            'correct': False
        },
    ]      
},
{
        'text': 'What is the output of for x in [1, 2, 3]: print x?',
        'answers': [
        {
            'key': "A",
            'text': "x x x",
            'correct': False
        },
        {
            'key': "B",
            'text': "1 2 3",
            'correct': True
        },
        {
            'key': "C",
            'text': "Error",
            'correct': False    
        },
        {
            'key': "D",
            'text': "None of the above",
            'correct': False
        },
    ]
},
{
        'text': 'What is the following function removes last object from a list?',
        'answers': [
        {
            'key': "A",
            'text': "list.indx(obj)",
            'correct': False
        },
        {
            'key': "B",
            'text': "list.pop(obj=list[-1]",
            'correct': True
        },
        {
            'key': "C",
            'text': "list.insert(index.obj",
            'correct': False    
        },
        {
            'key': "D",
            'text': "list.remove(obj)",
            'correct': False
        },
    ]
},
{
        'text': 'Which of the following is correct about dictionaries in python?',
        'answers': [
        {
            'key': "A",
            'text': "Python dictionaries are kind of hash table type",
            'correct': False
        },
        {
            'key': "B",
            'text': "They work like associative arrays or hashes found in Perl and consist of key-value pairs",
            'correct': False
        },
        {
            'key': "C",
            'text': "A dictionary key can be almost any Python type, Values acn be any arbitary object",
            'correct': False    
        },
        {
            'key': "D",
            'text': "All of the above",
            'correct': True
        },
    ]
},
{
        'text': 'Which of the following function checks in a string that all characters are digits?',
        'answers': [
        {
            'key': "A",
            'text': "shuffle(lst)",
            'correct': False
        },
        {
            'key': "B",
            'text': "capitalize()",
            'correct': False
        },
        {
            'key': "C",
            'text': "isalnum()",
            'correct': False    
        },
        {
            'key': "D",
            'text': "isdigit()",
            'correct': True
        },
    ]
},
{
        'text': 'Which of the following is correct about Python?',
        'answers': [
        {
            'key': "A",
            'text': "It supports functional and structured programming methods as well as OOP",
            'correct': False
        },
        {
            'key': "B",
            'text': "It can be used as a scripting language or can be compiled to byte-code for building large applications.",
            'correct': False
        },
        {
            'key': "C",
            'text': "It provides very high-level dynamic data types and supports dynamic type checking.",
            'correct': False    
        },
        {
            'key': "D",
            'text': "All of the above",
            'correct': True
        },
    ]
},
{
        'text': "What is the output of print list[0] if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?",
        'answers': [
        {
            'key': "A",
            'text': "[ 'abcd', 786 , 2.23, 'john', 70.2 ]",
            'correct': False
        },
        {
            'key': "B",
            'text': "abcd",
            'correct': True
        },
        {
            'key': "C",
            'text': "Error",
            'correct': False    
        },
        {
            'key': "D",
            'text': "All of the above",
            'correct': False
        },
    ]
},
{
        'text': 'Which of these is NOT a Python datatype?',
        'answers': [
        {
            'key': "A",
            'text': "int",
            'correct': False
        },
        {
            'key': "B",
            'text': "long",
            'correct': False
        },
        {
            'key': "C",
            'text': "decimal",
            'correct': True    
        },
        {
            'key': "D",
            'text': "float",
            'correct': False
        },
    ]
},
{
        'text': 'How can we add two strings together?',
        'answers': [
        {
            'key': "A",
            'text': "s.join(s2)",
            'correct': False
        },
        {
            'key': "B",
            'text': "s.add(s2)",
            'correct': False
        },
        {
            'key': "C",
            'text': "s = s + s2",
            'correct': True    
        },
        {
            'key': "D",
            'text': "s ++ s2",
            'correct': False
        },
    ]
},
{
        'text': 'How to access list elements?',
        'answers': [
        {
            'key': "A",
            'text': "print l->get(0)",
            'correct': False
        },
        {
            'key': "B",
            'text': "print l[0]",
            'correct': True
        },
        {
            'key': "C",
            'text': "print l.item(0)",
            'correct': False    
        },
        {
            'key': "D",
            'text': "print l(0)",
            'correct': False
        },
    ]
}
]

# define function for use when asking questions
def askQuestions(q):
    print(q['text'] + '\n')
    for a in q['answers']:
        print('\t' + a['key'] + ' - ' + a['text'] + '\n')

# define the accepted answer input format
def validAnswers(answer):
    validChoices = ['A','B','C','D']
    return answer in validChoices


# define get user answers with input and use try/except for input error
def getUserAnswer():

    try:
        userAnswer = input("Enter your answer A; B; C or D\n\n Your answers is: ")

        # if/else method to determine if the answer is matching the accepted format A, B, C or D
        if validAnswers(userAnswer):
            return userAnswer

        else:
            raise ValueError("Invalid Answer Input, Please use A, B, C, or D")

    except Exception as e:
        print("There is an error")
        print(e)
        return None

# define function to check if the answers is a correct answer to a question with parameters q-question and a-answer
# by verifying with the stored data for True/Flase condition
def checkAnswers(q, a):
    answers = q["answers"]
    correctAnswer = None
    for answer in answers:
        if answer["correct"]:
            correctAnswer = answer
            break
    
    if correctAnswer is None:
        print("Question has no correct answer")
        return False

    correctAnswerKey = correctAnswer["key"]

    return a == correctAnswerKey

# calling the previously defined finctions for execution and runnig them trough loop for 
# iterating over each question, ask the question, get the input, verify the answer, print the output and final score
for question in quizQuestions:
    askQuestions(question)

    answer = getUserAnswer()

    isAnswerCorrect = checkAnswers(question, answer)

    if isAnswerCorrect:
        print(" Your answer is correct!\n")
        score['correct'] += 1
    else:
        print(" Your answer is incorrect\n")
        score['incorrect'] += 1

# calculating quiz score as percent
percent = str(score['correct'])
percent = int(percent)

# output print results
print("Quiz Done!!! \n")
print("You got " + str( score['correct'] ) + " Correct questions and " +  str( score['incorrect'] ) + " Incorrect questions")
print("Your Quiz score is: ", format((percent / 10) * 100, '.2f'),'%')

