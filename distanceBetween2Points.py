# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help finding distance between two points using function

import math

# message about the purpose of this program
print("This is a program calculating the distance between points\n")

# definig the function to calculate distance between two points
def distance(x1,x2,y1,y2):
    distanceTwoPoints = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distanceTwoPoints

# using try/except method for corect user input fromat
try:
    # user input for points values
    userInputX1 = float(input('Enter the X1 for the first point: '))
    userInputY1 = float(input('Enter the Y1 for the first point: '))
    userInputX2 = float(input('\nEnter the X2 for the second point: '))
    userInputY2 = float(input('Enter the Y2 for the second point: '))


    # calling the function distance() and assign it to variable distanceResult
    distanceResult = distance(userInputX1,userInputX2,userInputY1,userInputY2)

    # output for the distance between two points
    print("\nDistance between the points is:", "%.2f" % distanceResult)

# except to rise error notification for th euser if the input format is not numerical
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")

