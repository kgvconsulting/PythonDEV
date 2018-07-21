# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help calculating pizza cost by entered measurements 
# and verify the cost if is above .10 usd per inch

from math import *

# using try / except to avoid user input error in case the input is not numerical
try:
    # set the user input for pizza diameter and price
    pizza_Diameter = float(input('Enter pizza diameter in square inches in numerical format: '))
    price_Pizza = float(input('Enter pizza price in numerical format: '))

    # calculating the pizza area and cost per inch
    pizza_Area = pi * (pizza_Diameter / 2)**2
    price_inch = price_Pizza / pizza_Area

    # setting the boolean section to verify if the cost per inch is more than .10 USD
    # and notifing the user about that
    
    print("YOU GOT A DEAL!!! Pizza cost per square inch is: ", format(price_inch,'.2f'), "USD")

# exception if user enter non numerical input
except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format!")
