# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Program to check the type of credit card by user input of the credit card number

# seting a dictionary for type of Credit Cards and coresponding first digit
ccTypes = {3 :'American Express',4 :'Visa',5 :'Master Card',6 :'Discover'}

# set the try/except/else method for eliminating/catching user input format errors
try:
    # user input of the credit card number and integer
    userCCInput = int(input('Enter the credit card number without spaces: '))

    # slice the first digit from user inputed number and assign it to variable ccTypeCheck
    ccTypeCheck = int(str(userCCInput)[:1])

    # boolean for defining the comparancement of sliced first digit from the user entry cc number
    if ccTypeCheck in ccTypes:
        print("Your input is a credit card type: ", ccTypes[ccTypeCheck])

    # boolean raising error if user input cc number is not included into the predifined types
    # into the dictionary ccTypes
    else:
        print("Your input is a credit card type: Unknown Card")

# exception to report an error in case user input is not in numerical format
except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format, without spaces!")
