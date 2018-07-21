
# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program calculating the average word length of words in a sentence entered by user 

# user input of the sentence
userInput = input('Enter a sentence: ')

# breaking up the user input sentence (string) into single words divided by white space
# assign them to variable 'word'
words = userInput.split()

sum = 0

for w in words:
    sum = sum + len(w)

average = sum / len(words)

print(average)


