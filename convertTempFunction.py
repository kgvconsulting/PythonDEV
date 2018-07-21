# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help converting tempreture from Celsius to Fahrenheit using function

# definig the function to convert Celsius into Farenheit
def tempConvert(temp):
    tempCelsius = (((temp * 9) / 5.0) + 32)
    return tempCelsius

# using try/except method for corect user input fromat
try:
    # user input for tempreature in Celsius
    userTemp = float(input('Enter the temperature in Celsius: '))

    # calling the function tempConvert() and assign it to variable tempResult
    tempResult = tempConvert(userTemp)

    # output for the coverted temprature
    print("Your temperature is:", "%.2f" % tempResult, "in Fahrenheit")

# except to rise error notification for th euser if the input format is not numerical
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")

