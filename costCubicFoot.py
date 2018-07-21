# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will calculate cost of water per cubic foot in a pool

from math import *

# assign the height of the pool
poolHeight = 4

# accept user input for diameter and total cost of the water
userPoolDiameter = float(input('Enter the diameter of the pool in numerical format: '))
userWaterCost = float(input('Enter the total cost of the water in numerical format: '))

# calculate the volume of the pool
volumePool = (pi * ((userPoolDiameter/2)**2 * poolHeight))

# calculate the total cost per cubic feet
totalCost = userWaterCost / volumePool

# print the final result
print("Cost per cubic feet is: ", format(totalCost, '.3f'))
