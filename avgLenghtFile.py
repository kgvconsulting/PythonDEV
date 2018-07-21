
# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program calculating the average word length of words in a file entered by user 

# user input of the sentence
userInput = input('Enter a text file to read: ')

# Try/except to catch the missign file error
try:
    # open file "myFile.txt", reading it and assigning to f1
    workFile = open(userInput, "r")
    f = workFile.read()

# except to rise and erro if file is missing
except:
    print("File does not exist, Sorry try again ")
    exit()

# breaking up the user input sentence (string) into single words divided by white space
# assign them to variable 'word'
words = f.split()

# set sum to 0
sum = 0

# using forloop to iterate the file conntent
for w in words:
    sum = sum + len(w)

# calculating agerage
average = sum / len(words)

# output the result
print("Average word lenght is: ", average)


