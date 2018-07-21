# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This code is for python 3.x.x version, for python 2.7.x version repalce input() with raw_input() && print argument without ()
# Convert seconds to the equivalent number of weeks, days, hours, minutes, and seconds given the number of seconds as an integer from the user.

# Here start logical part verifing the user input to be integer and in numerical form

def convert_input(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print ("Oops, we have wrong input, please enter the seconds as a whole number: ")
            continue
        else:
            return userInput
            break

# Here start the user input && where we compute time convertion from seconds to weeks, days, hours, minutes

seconds_input = convert_input("Please enter the seconds to convert as a whole number: ")

minutes = seconds_input // 60
seconds_input -= 60*minutes

seconds = seconds_input

print (minutes, "Minutes", "and", seconds, "Seconds")
