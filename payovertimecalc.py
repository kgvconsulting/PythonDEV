# Created by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com
# Small program to help calculate work hours paid
# The program is for Python 2.x.x for Python 3.x.x need to update raw_input() to input()

non_numerical_input = True

def computepay(hours, rate):
    total_pay = hours * rate
    
    if hours <= 40 : 
        return total_pay

    else :
        total_pay = ((hours - reminder) * rate) + (reminder * addhr)
        return total_pay

try :
    hours = float(raw_input('Enter work hours: '))
    rate = float(raw_input('Enter pay per hour: '))

except Exception, e:
    print "Please enter only numerical input"
    non_numerical_input = False

if non_numerical_input == True:
    reminder = hours % 10
    addhr = rate * 1.5

else:
    quit()

print computepay(hours, rate)