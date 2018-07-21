# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Small program to help calculate work hours paid
# User entry for hours, pay rate and overtime by predetermine pay rate


# Calculating user entered value for worked hours and pay rate
non_numerical_input = True

try:
    hours = float(input('Enter work hours in numerical format: '))
    pay_rate = float(input('Enter hourly pay in numerical format: '))
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")
    non_numerical_input = False

if non_numerical_input == True :
    reminder = hours % 10
    addhr = pay_rate * 1.5

else :
    quit()

if hours <= 40 : 
    total_pay = pay_rate * hours

else :
    total_pay = ((hours - reminder) * pay_rate) + (reminder * addhr)

print ("Your Total pay is: ", total_pay)
