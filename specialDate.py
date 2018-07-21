# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Program to help to calculate the special date from user inputed date: MM/DD/YY 

# def function to check the input date for special date
def calendar(month,date,year):
    if month * date == year:
        print("You entered a special date: ", month,"/", date,"/", year)
    else:
        print("You entered not a special date: ", month,"/", date,"/", year)
    return month, date, year


# try/except to catch user non numerical format input
try:
    # user input
    userMonthInput = int(input('Enter month in numerical format: '))
    userDateInput = int(input('Enter date of the month in numerical format: '))
    userYearInput = int(input('Enter year in two digit numerical format: '))

    # calling the predefined functon calendar()
    output = calendar(userMonthInput,userDateInput,userYearInput)

# exception if user input is not numerical format
except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format")

