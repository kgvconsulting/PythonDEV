# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program print the middle character from a user inputed string 

print("This program print the middle character of user inputed string"'\n')

user_string = input('Enter your string: ')
middle_string_number = len(user_string)/2
middle_string_number = int(middle_string_number)

print("The middle character is: ",user_string[middle_string_number])
