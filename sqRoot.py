# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help calculating square root of user inut 3 digit number.
# If user fail to enter 3 digit number program rise error

import math

# try/except method to catch non numerical value and rise and error warning the user
try:
    # user promt to enter three digit whole number
    userNumberInput = int(input('Enter three digit number: '))

    # convert the user inputed number into strng and assigning to working variable "n"
    n = str(userNumberInput)

    # check if the user inputed number is not three digits, if True rise error, print warning
    # if False, thus is three digit number perform calculation and find the square root of it
    if len(n) !=3:
        print("Please enter only three digit whole numbers")
    else:
        sqNumber = math.sqrt(userNumberInput)

        # output, print the result for the square root of the entered user trhee digits number
        print("The square root of your entered number is: ", float(format(sqNumber, '.2f')))

# exception when the user input is non numerical entry rise an exception and warn to enter only numbers
except Exception as e:
    print("Oops, something went wrong. Please enter only whole numerical format!")
