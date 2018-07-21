# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will extract emails form user entered data source file,and count how many times this email was used

print("This program will search for an email in data source file\nin user input file source and extract the email address,\nthat was used the most times\n")

file_name = input('Enter a file name: ')

try:
    file_hand = open(file_name)

except:
    print('File does not exist, Sorry try again: ', file_name)
    exit()

emailgroup = dict()

for line in file_hand :
    line = line.rstrip()

    if line.startswith('From:'):
        flnum = line.split()
        emailresult = flnum[1]
        
        emailgroup[emailresult] = emailgroup.get(emailresult, 0) + 1
        maximum = max(emailgroup, key=emailgroup.get)

print('The email account is: ', maximum,'\n','This email was used: ', emailgroup[maximum], 'times')
