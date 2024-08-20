from datetime import datetime

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

phoneNumbersAndTotalTimeOnThePhone = {}
longestOnPhoneNumber = ""
longestOnTime = 0

for row in calls:
    date_string = row[2]
    date_object = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
    if date_object.year != 2016 or date_object.month != 9:
        continue

    caller = row[0]
    receiver = row[1]
    timeTaken = row[3]

    if (caller in phoneNumbersAndTotalTimeOnThePhone):
        phoneNumbersAndTotalTimeOnThePhone[caller] += int(timeTaken)
    else:
        phoneNumbersAndTotalTimeOnThePhone[caller] = int(timeTaken)

    if (receiver in phoneNumbersAndTotalTimeOnThePhone):
        phoneNumbersAndTotalTimeOnThePhone[receiver] += int(timeTaken)
    else:
        phoneNumbersAndTotalTimeOnThePhone[receiver] = int(timeTaken)

    if (phoneNumbersAndTotalTimeOnThePhone[caller] > longestOnTime):
        longestOnPhoneNumber = caller
        longestOnTime = phoneNumbersAndTotalTimeOnThePhone[caller]

    if (phoneNumbersAndTotalTimeOnThePhone[receiver] > longestOnTime):
        longestOnPhoneNumber = receiver
        longestOnTime = phoneNumbersAndTotalTimeOnThePhone[receiver]

print(f"{longestOnPhoneNumber} spent the longest time, {longestOnTime} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

