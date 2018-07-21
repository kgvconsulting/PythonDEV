# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help display the percentages of males & females in the class, by user inputed data

try:
    user_numberFemales = int(input('Enter the number of females in class: '))
    user_numberMales = int(input('Enter the number of males in class: '))

    classTotal = user_numberFemales + user_numberMales
    malePercent = (user_numberMales / classTotal) * 100
    femalePercent = (user_numberFemales / classTotal) * 100

    print("The percentage of students in class are:", (int(femalePercent)), "%", "Females",
        "and", (int(malePercent)), "%", "Males")

except Exception as e:
    print ("Oops, something went wrong. Please enter only in numerical format!")

