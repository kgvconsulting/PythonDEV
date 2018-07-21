# by Krasimir Vatchinsky - KGV Consulting Corp 
# info@kgvconsultingcorp.com

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80)) # you can add any url
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n') # you can add any url

count = 0 
picture = ""; 
while True:
    data = mysock.recv(5120)
    if ( len(data) < 1 ) : break 
    # time.sleep(0.25)
    count = count + len(data) 
    print len(data),count 
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF) 
pos = picture.find("\r\n\r\n");
print 'Header length',pos
print picture[:pos]

# Skip past the header and save the picture data 
picture = picture[pos+4:]
fhand = open("stuff.jpg","wb") 
fhand.write(picture);
fhand.close()
