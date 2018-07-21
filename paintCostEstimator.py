# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help calculating surface are of cylinder

# assign given values for minimum surface are, hours need to paint it, gallons paint, 
# and charge per hour for work
basePaintGallon = 1 # gallon
minimumSurfaceArea = 114 # sq feet
minimumHoursWork = 8 # hours for base work od minimumSrfaceArea
workHourCharge = 37 # $ per hour work cost

# accept user input for square footage to be painted and price per gallon of paint
userSquareFeet = float(input('Enter the square feet of wall to be paint in numerical format: '))
userPriceGallon = float(input('Enter the price of paint per gallon numerical format: '))

# calculate the required paint gallons for the user inputed surface area
paintNumberGallons = (userSquareFeet / minimumSurfaceArea) * basePaintGallon 

# calculate total work hours needed for the paint job
totalHoursWork = paintNumberGallons * minimumHoursWork

# calculate price for the needed paint
totalPriceGallonPaint = paintNumberGallons * userPriceGallon

# calculate cost of the work
totalWorkCost = totalHoursWork * workHourCharge

# calculate total cost
totalCost = totalPriceGallonPaint + totalWorkCost

# print the results for needed paint, hours work, price for the paint, work cost and total cost
print("The number of gallons of paint required: ",format(paintNumberGallons,'.2f'), "Gallons")
print("The hours of labor required: ",format(totalHoursWork, '.2f'), "Hours")
print("The total cost of the paint: $",format(totalPriceGallonPaint,'.2f'), "USD")
print("The total labor charges: $",format(totalHoursWork,'.2f'), "USD")
print("The total cost of the whole paint job: $",format(totalCost,'.2f'), "USD")

