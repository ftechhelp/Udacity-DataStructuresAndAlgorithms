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

unique_area_codes_called = set()
bangalore_area_code_called = 0
called_by_bangalore = 0

for row in calls:
    
    caller = row[0]
    receiver = row[1]
    bangalore_area_code = "(080)"

    if (not caller.startswith(bangalore_area_code)):
        continue

    isFixedLine = receiver.startswith("(")
    isMobileNumber = len(receiver.split(" ")) == 2
    isTelemarketer = receiver.startswith("140")

    if (isFixedLine):
        unique_area_codes_called.add(receiver.split(")")[0][1:])
        bangalore_area_code_called += 1 if receiver.startswith(bangalore_area_code) else 0

    if (isMobileNumber):
        unique_area_codes_called.add(receiver[:4])

    if (isTelemarketer):
        unique_area_codes_called.add("140")

    called_by_bangalore += 1

print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(unique_area_codes_called):
    print(area_code)

print(bangalore_area_code_called)
print(called_by_bangalore)

percentage_of_bangalore_to_bangalore = round((bangalore_area_code_called / called_by_bangalore) * 100, 2)
print(f"{percentage_of_bangalore_to_bangalore} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
