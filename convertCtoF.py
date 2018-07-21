# Created by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com

# This program help converting tempreture from Fahrenheit to Celsius and back

temp = raw_input('Enter the temperature in C: ')

c = float(temp)

temp_result = (((c * 9) / 5) + 32)

print temp_result, "in Fahrenheit"
