# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Program for user entry for hours, pay rate and overtime by predetermine pay rate

# seting the value of logical operator nonNumericalInput to be True
nonNumericalInput = True

# set the try/except method for eliminating/catching user input format errors
try:
    # user input of work hours and pay rate
    hours = float(input('Enter work hours in numerical format: '))
    payRate = float(input('Enter hourly pay in numerical format: '))

# exception to reprot an error in case user input is not in numerical format
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")
    nonNumericalInput = False

# boolean for defining the computation in case the user input is in corect format
if nonNumericalInput:
    reminder = hours % 10
    addhr = payRate * 1.5

# boolean define to abort execution
else :
    quit()

# boolean for defining the computation in case the user enters <= 40 hours
if hours <= 40 : 
    totalPay = payRate * hours

# boolean for defining the computation if the user enters > 40 hours
else :
    totalPay = ((hours - reminder) * payRate) + (reminder * addhr)

# output the result for total pay
print("Your Total pay is: ", format(totalPay, '.2f'))
