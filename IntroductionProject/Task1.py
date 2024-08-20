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

unique_numbers = set()

for row in texts:
    sender = row[0]
    receiver = row[1]
        
    unique_numbers.add(sender)
    unique_numbers.add(receiver)

for row in calls:
    sender = row[0]
    receiver = row[1]
            
    unique_numbers.add(sender)
    unique_numbers.add(receiver)

print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
