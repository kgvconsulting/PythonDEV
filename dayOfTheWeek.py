# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Program for user entry number 1-7 and display corresponding day of the week

# seting a dictionary for days of the week and coresponding number
weekDays = {1 :'Monday',2 :'Tuesday',3 :'Wednesday',4 :'Tursday',5 :'Friday',6 :'Saturday',7 :'Sunday'}

# set the try/except/else method for eliminating/catching user input format errors
try:
    # user input of day of the week as number and integer
    userDayInput = int(input('Enter day of the week from 1 to 7 in numerical format: '))

    # boolean for defining the comparancement of user entry number with day of the week
    if userDayInput in weekDays:
        print("Your input number corespond to: ", weekDays[userDayInput])

    # boolean raising error if user input number is not from range 1 to 7
    else:
        print("You didn't enter number between 1 and 7. Please try again!")

# exception to report an error in case user input is not in numerical format
except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format, from 1 to 7!")
