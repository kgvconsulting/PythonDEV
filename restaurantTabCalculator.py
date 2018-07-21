# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will calculate restaurant tab with gift certificate

# Restaurant tab calculation program
# This program will calculate a restaurant tab with a gift certificate

# get amount of tax
tax = float(input('Enter amount of the tax: '))

# program greeting
print('This program will calculate a restaurant tab for a couple with')
print('a gift certificate, with a restaurant taxof', tax * 100, '%\n')

# get amount of gift certificate
amt_certificate = float(input('Enter amount of the gift certificate: '))

# cost of ordered items
print('Enter ordered items for person 1')

appertizer_per1 = float(input('Apertizer: '))
entree_per1 = float(input('Entree: '))
drinks_per1 = float(input('Drinks: '))
desert_per1 = float(input('Dessert: '))

print('\nEnter ordered items for person 2')

appertizer_per2 = float(input('Apertizer: '))
entree_per2 = float(input('Entree: '))
drinks_per2 = float(input('Drinks: '))
desert_per2 = float(input('Dessert: '))

# total items
amt_person1 = appertizer_per1 + entree_per1 + drinks_per1 + desert_per1
amt_person2 = appertizer_per2 + entree_per2 + drinks_per2 + desert_per2

# compute tab with taxes
items_cost = amt_person1 + amt_person2
tab = items_cost + items_cost * tax

# display amount owe
print('\nOrdered Itmes: $', format(items_cost, '.2f'))
print('Restaurant tax: $', format(items_cost * tax, '.2f'))
print('Tab: $', format(tab - amt_certificate, '.2f'))
print('(negative amount indicates unused amount of gift certificate)')


