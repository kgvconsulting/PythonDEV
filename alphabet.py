# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This program will print string in alphabetical order from a-z


# assign the given strings
givenOne = 'acegikmoqsuwy'
givenTwo = 'bdfhjlnprtvxz'

# initializing the accumulator
alphabetResult = ''

# iterate trough the elements of the both strings
# the given strings have same len so we can use the range of one of them
for i in range(len(givenOne)):

    # update the accumulator by adding and sorting one character from each string in sequential pattern
    alphabetResult = alphabetResult + givenOne[i] + givenTwo[i]

# print the result of sorted alphabet
print(alphabetResult)
