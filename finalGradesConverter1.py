# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Program to help to convert user inputed grade numbers from 1 to 100 into letter grades, 

# def function to convert user input grades to letter grades
def gradeScore(score):
    if score >= 93 and score <= 100:
        print("Your grade is : A")
    elif score >=90 and score <= 92:
        print("Your grade is : A-")
    elif score >= 87 and score <= 89:
        print("Your grade is : B+")
    elif score >= 83 and score <= 86:
        print("Your grade is : B")
    elif score >= 80 and score <= 82:
        print("Your grade is : B-")
    elif score >= 77 and score <= 79:
        print("Your grade is : C+")
    elif score >= 73 and score <= 76:
        print("Your grade is : C")
    elif score >= 70 and score <= 72:
        print("Your grade is : C-")
    elif score >= 67 and score <= 69:
        print("Your grade is : D+")
    elif score >= 63 and score <= 66:
        print("Your grade is : D")
    elif score >= 60 and score <= 62:
        print("Your grade is : D-")
    elif score >= 0 and score <=59:
        print("Your grade is : E")

    else:
        print("You didn't enter the number between 1 and 100, Please try again")
    return score

# try/except to catch user non numerical format input
try:
    # user input
    userGradeInput = int(input('Enter an grade number from 1 to 100 only in numerical format: '))
    # calling the predefined functon gradeScore()
    output = gradeScore(userGradeInput)

# exception if user input is not numericla format
except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format")

