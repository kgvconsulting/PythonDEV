# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help user to guess a predefined number using loops and booleans 

# setting the predefined number => myNumber = 7; count = 0 and flag askAgain to be True
myNumber = 7
count = 0
askAgain = True

# starting interactive loop using while loop method
while askAgain:

    # set the try/except method for eliminating/catching user input format errors
    try:
        # user input of their guess about what is the predefined number in numerical format
        userInput = float(input("Please enter your guess about what is my number in numerical format: "))

        # activating the counter
        count = count + 1

        # using boolean to check the different input conditions and determinate when the input match the predefined number
        if userInput < myNumber:
            print("You can do better, guess higher! Try again: \n")

        elif userInput > myNumber:
            print("You can do better, guess lower! Try again: \n")

        else:
            askAgain = False
            print("Great! You finally got it correct! You need it", count, "times for that.")

    # exception to report an error in case user input is not in numerical format
    except Exception as e:
        print("Oops, something went wrong. Please enter only numerical format!\n")
