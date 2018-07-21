# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will replace the empty spaces of user inputed phrase with underscores and print it

print("This program will replace the empty spaces of user inputed phrase with underscores and print it"'\n')

user_string = input('Enter your phrase: ')

new_phrase = user_string.replace(" ","_")

print(new_phrase)
