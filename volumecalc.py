# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Small program to help calculate volume from user inout of length, width and height


is_numeric = True
volume = 0
user_length = 0
user_width = 0
user_height = 0


try:
    user_length = float(input('Enter length in numerical format: '))
    user_width = float(input('Enter width in numerical format: '))
    user_height = float(input('Enter height in numerical format: '))
    
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")
    is_numeric = False

if is_numeric:
    volume = user_length * user_width * user_height
    print ("Your object volume is: ", volume)
