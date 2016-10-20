# by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com
# This code is for Python 2.7.x for Python 3.x.x need to replace raw_input() with input()
# Small program to help extract email address form data sorce and how many times this email was used

fname = raw_input('Enter a file name: ')

try:
    fhand = open(fname)

except:
    print "File does not exist, Sorry try again: ", fname
    exit()

emailgroup = dict()

for line in fhand :
    line = line.rstrip()

    if line.startswith('From:'):
        flnum = line.split()
        emailresult = flnum[1]
        #print emailresult # extract list of all emails in the data source
        
        emailgroup[emailresult] = emailgroup.get(emailresult, 0) + 1
        maximum = max(emailgroup, key=emailgroup.get)

print maximum, emailgroup[maximum]