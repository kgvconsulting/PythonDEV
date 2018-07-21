# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program to write with user input and display content of text file 

# user input file name
userFile = input("please enter five words: ")


# open file "myFile.txt", writing mode and add the user input
workFile = open('userFile.txt', "w")

workFile.write(userFile)

# close the work file
workFile.close()

# open the worFile and read it
workFile = open('userFile.txt', "r")

# output for line number, file name, status close or open, and opening mode
print("\nYour input is: ", workFile.read())

# finction close() to manualy close the file
workFile.close()
