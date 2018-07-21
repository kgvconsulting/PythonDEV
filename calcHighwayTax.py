# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help calculating highway tax

try:
    # accepting user input and in the same time converting it to float
    user_marketValue = float(input('Enter the property full market value numerical format: '))

    # the assessed value of a house is 95% of full market value
    assessed_value = 0.95 * user_marketValue

    # calculationg highway tax by multiplying the coeficent provided to us - 0.000809676 by the assessed_value
    highway_Tax = 0.000809676 * assessed_value

    # output - print the result for calculating the highway tax
    print('\n'"For a house estimated to be worth: $", format(user_marketValue, '.2f'),'\n'"Highway tax is: ","$",highway_Tax)

except Exception as e:
    print("Oops, something went wrong. Please enter only numerical format!") 
