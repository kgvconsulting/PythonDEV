# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program help identify a prize winner

initial = input('enter th efirst letter of your name: ')
age = int(input('enter your age: '))

if initial == 'B' and age <= 5:
    print("You are a winner!!")

elif age == 99:
    print("You are a winner!")

elif initial == 'W' and age == 21:
    print("You are our favorite winner")

else:
    print("so sorry ....") 
