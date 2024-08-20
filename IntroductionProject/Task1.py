"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

uniqueNumbers = set()

for row in texts:
    for index, phonenumber in enumerate(row):
        if index > 1:
            continue
        
        uniqueNumbers.add(phonenumber)

for row in calls:
    for index, phonenumber in enumerate(row):
        if index > 1:
            continue

        uniqueNumbers.add(phonenumber)

print(f"There are {len(uniqueNumbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
