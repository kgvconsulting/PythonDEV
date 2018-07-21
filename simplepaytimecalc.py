# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Small program to help calculate work hours paid
# User entry for hours, pay rate


# Calculating user entered value for worked hours and pay rate
weekly_pay = 0

try:
    user_hours = float(input('Enter work hours in numerical format: '))
    user_payrate = float(input('Enter hourly pay in numerical format: '))
    
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")
 
weekly_pay = user_payrate * user_hours

print ("Your Total pay is: ", weekly_pay)
