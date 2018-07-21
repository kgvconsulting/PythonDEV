# Created by Krasimir Vatchinsky - KGV Consulting Corp - info@kgvconsultingcorp.com
# This accumulator program calculating exam score averages


print("This program computes the average of 10 exam scores.")

sum = 0

for i in range (10):
    score = input("Enter the exam score: ")
    score = float(score)
    sum = sum + score

average = sum / 10.0
print("The average of the scores is: ",average)
