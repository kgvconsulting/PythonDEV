# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help to compare inputed results from 3 sources, 
# if 2 results matched - are equal, print the result, if non result match discard all

# set a Flag
validResult = None

# create empty list
inputs = []

# try/except method to catch non numerical value and rise and error warning the user
try:
    # loop to get 3 computer inputs
    for i in range(3):
        inputs.append( int( input('Enter computer ' + str(i + 1) + ' timed result: ') ) )

# exception when the user input is non numerical entry rise an exception and warn to enter only numbers
except Exception as e:
    print("Oops, something went wrong. Please enter only whole numerical format!")

# using for loop and booleon to iterate throughout the list with stored inputs
# and check if there are at least two same timed results inputs, if they are print them as result 
# if no than print Discard results and close
for inputValue in inputs:
    if inputs.count(inputValue) > 1:
        validResult = inputValue

if validResult is not None:
    print("Result is " + str(validResult))
else:
    print("Discard results")
