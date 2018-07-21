# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help to determine vacation cost by user input vacation lenght in weeks 

# welcome message
print("We accept weekly rentals for minimum 4 weeks to maximum 16 weeks\n")
print("Type Done if you want to stop and exit the program\n")

# while loop
while True:

    # user input prompt to enter how many weeks whant to rent
    userWeekInput = input("Enter how many weeks you like ot book: ")

    # booleon set the word 'done' or 'Done' or 'DONE' for user to exit the program
    if userWeekInput == 'done' or userWeekInput == 'Done' or userWeekInput == 'DONE':
        break

    # try/except to catch invalid user input
    try:
        # booleon to compare user input with pre defined data about time an dcost for vacation
        if int(userWeekInput) >= 4 and int(userWeekInput) <= 6:

            print("The rental cost is $ 3,080.00 USD\n")
            break

        elif int(userWeekInput) >= 7 and int(userWeekInput) <=10:

            print("The rental cost is $ 2,650.00 USD\n")
            break

        elif int(userWeekInput) >=11 and int(userWeekInput) <=16:

            print("The rental cost is $ 2,090.00 USD\n")
            break

        else:
            print("\nOops, entered week period not in range. Please try again,\n enter between 4 and 16 weeks\n")

    except Exception as e:
        print("\nOops, something went wrong. Please enter only numerical format!\n") 
