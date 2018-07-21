# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program determine the distance (in km) a surface-to-air missile 
# must travel to reach a given height and angle. The height (in km) & angle are given as inputs.

print("This program determine the distance (in km) a surface-to-air missile\nmust travel to reach a given height and angle.\nThe height (in km) & angle are given as inputs.\n")

from math import *

try:
    missile_Height = float(input('Enter missile height in km: '))
    missile_Angle = float(input('Enter missile angle in degrees: '))

    missile_Angle_Radians = missile_Angle * pi / 180

    missile_Distance = missile_Height / sin(missile_Angle_Radians)

    print("\nThe distance missile will travel is: ", format(missile_Distance, '.4f'), "km")

except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format!")

