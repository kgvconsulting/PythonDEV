# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program display content of text file 

# user input file name
userFile = input("please enter file name: ")

# Try/except to catch the missign file error
try:
    # open file "myFile.txt", reading it and assigning to f1
    workFile = open(userFile, "r")

# except to rise and erro if file is missing
except:
    print("File does not exist, Sorry try again ")
    exit()

# output for line number, file name, status close or open, and opening mode
print(workFile.read())

# finction close() to manualy close the file
workFile.close()
