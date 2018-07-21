# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will count from a predetermine range of values - numbers and divisable by a predetermine number

count = 0

for i in range (1, 1001):
    if i % 3 == 0 :
        print(i,end=',') # print on one line with commas
        count = count + 1

print()
print("The number of numbers between 1 and 1000 that are divisable by 3 is: ", count)
