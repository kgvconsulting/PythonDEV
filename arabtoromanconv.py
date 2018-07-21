# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Small program to help to convert user inputed arabic numbers from 1 to 10 into roman numerals, 
# if user enter other number than 1 to 10 display an error
# University of Albany
# Programing for Problem Solving
# Instructor Professor Horowitz


arabic_roman = { 1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX', 10 : 'X' }

try:
    arabic_number = int(input('Enter an arabic number from 1 to 10 only in numerical format: '))

    if arabic_number in arabic_roman:
        print( arabic_roman[arabic_number] )

    else:
        print("You didn't enter the number between 1 and 10, Please try again")

except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format")
