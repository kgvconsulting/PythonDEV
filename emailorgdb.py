# by Krasimir Vatchinsky - KGV Consulting Corp - Python v2.7.x
# info@kgvconsultingcorp.com
# Organizations domain received emails count from file

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter a file name: ')

try:
    fhand = open(fname)

except:
    print "File does not exist, Sorry try again: ", fname
    exit()

for line in fhand :
    if line.startswith('From:'):
        flnum = line.split()
        emailresult = flnum[1]
        domain = emailresult.split('@')[1] #extract the email domain == organization
        
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain, ))

        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain, ))
        except:
            cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain, ))

        #conn.commit() #make code run slower

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 15'

for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

conn.commit() # make code run faster
cur.close()

        