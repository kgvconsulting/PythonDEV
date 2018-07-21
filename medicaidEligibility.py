# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help to determine 2018 Medicaid eligibility by inputed size of family and monthly income 


# set a dictionary with base data for family size and income
levels2018 = {2 : 2919, 3 : 3340, 4 : 3761, 5 : 3382}

# def function for comparing and calculating medicaid eligibility
def eligibility(size,income):
    if size in levels2018 and income <= levels2018[size]:
        return "You are eligible for medicaid"
    elif size > 5:
        xPeople = size - 5
        xIncome = 3382 + (622 * xPeople)
        if income <= xIncome:
            return "You are eligible for medicaid"
        else:
            return "You are not eligible for medicaid"
    else:
        return "You are not eligible for medicaid"

# try/except method to catch non numerical value and rise and error warning the user
try:
    # inputs for family size and monthly income
    userInputSize = int(input('Enter the size of your family: '))
    userInputIncome = int(input('Enter monthly income: '))


# exception when the user input is non numerical entry rise an exception and warn to enter only numbers
except Exception as e:
    print("Oops, something went wrong. Please enter only whole numerical format!")

# caling the function eligibility()
result = eligibility(userInputSize,userInputIncome)

# print the output
print(result)
