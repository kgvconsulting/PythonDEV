# Created by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com

# This program help converting tempreture from Fahrenheit to Celsius and back

temp = raw_input('Enter the temperature: ')
temp_type = raw_input('Enter tempreture type - 1 for F or 2 for C: ')

t = float(temp) # user inout of temperature
z = int(temp_type)

if z == 1 :
    x = (((t - 32) * 5) / 9.0)
    print x, "in Celsius"

elif z == 2 :
    y = (((t * 9) / 5.0) + 32)
    print y, "in Fahrenheit"

else :
    print "Please use only number 1 for Fahrenheit or 2 for Celsius. Please try again"
