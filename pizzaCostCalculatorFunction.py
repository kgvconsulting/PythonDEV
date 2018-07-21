# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help calculating pizza cost by entered measurements using functions

import math

# define function to calculate the area
def pizzaArea(diameter):
    area = math.pi * (diameter / 2)**2
    return area

# define function to calculate price per square inch
def priceSqInch(price, area):
    price_inch = price / area
    return price_inch

# geting user input, and call the pre-defined functions to receive the final result and output
# using try / except to avoid user input error in case the input is not numerical
try:

    # set the user input for pizza diameter and price
    pizzaDiameter = float(input('Enter pizza diameter in square inches in numerical format: '))
    pricePizza = float(input('Enter pizza price in numerical format: '))

    # call predefined function 'PizzaArea' to perform the calculations and assign to valiable: 'areaOfPizza'
    areaOfPizza = pizzaArea(pizzaDiameter)

    # call predefined function 'priceSqInch' to perform the calculations and assign to variable: 'result'
    result = priceSqInch(pricePizza, areaOfPizza)

    # setting the boolean section to verify if the cost per inch is more than .10 USD
    print("Pizza cost per square inch is: ", format(result,'.2f'), "USD")

# exception if user enter non numerical input
except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format!")
   

