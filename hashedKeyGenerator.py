# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will generate random string / password from user inputed string

print('This program will convert user inputed string to hashed SHA512 string - password', '\n')

import hashlib

user_string = input('Please enter a string, any combination of letters and digits: ')
bytes_user_string = str.encode(user_string)

hashed_password = hashlib.sha512(bytes_user_string)
converted_password = hashed_password.hexdigest()

print('\n''Your SHA512 secure password is:', converted_password)

