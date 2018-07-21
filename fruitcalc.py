# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# Small program to help calculate total price for purchased fruits by user input purchased number of oranges and lemons
# and getting the total price with preset price per fruit

is_numeric = True
total_price = 0
number_oranges = 0
number_lemons = 0


try:
    number_oranges = float(input('Enter number of purchased oranges numerical format: '))
    number_lemons = float(input('Enter number of purchased lemons in numerical format: '))
    
except Exception as e:
    print ("Oops, something went wrong. Please enter only numerical format!")
    is_numeric = False

if is_numeric:
    price_oranges = 0.30
    price_lemons = 0.15
    total_price = (number_oranges * price_oranges) + (number_lemons * price_lemons)
    print ("Your Total Price is: ", total_price)
