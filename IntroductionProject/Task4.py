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

possible_telemarketers = set()
impossible_telemarketers = set()

for row in calls:

    caller = row[0]
    receiver = row[1]

    possible_telemarketers.add(caller)

    if (receiver in possible_telemarketers and receiver not in impossible_telemarketers):
        possible_telemarketers.remove(receiver)
        impossible_telemarketers.add(receiver)

for row in texts:

    sender = row[0]
    receiver = row[1]

    if (sender in possible_telemarketers):
        possible_telemarketers.remove(sender)

    if (receiver in possible_telemarketers):
        possible_telemarketers.remove(receiver)

print("These numbers could be telemarketers: ")
for telemarketer in sorted(possible_telemarketers):
    print(telemarketer)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

