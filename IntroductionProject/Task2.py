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

phone_numbers_and_total_time_on_the_phone = {}
phone_number_longest_on_the_phone = ""
time_of_longest_on_the_phone = 0

for row in calls:
    date_string = row[2]
    date_object = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
    if date_object.year != 2016 or date_object.month != 9:
        continue

    caller = row[0]
    receiver = row[1]
    time_taken = row[3]

    if (caller in phone_numbers_and_total_time_on_the_phone):
        phone_numbers_and_total_time_on_the_phone[caller] += int(time_taken)
    else:
        phone_numbers_and_total_time_on_the_phone[caller] = int(time_taken)

    if (receiver in phone_numbers_and_total_time_on_the_phone):
        phone_numbers_and_total_time_on_the_phone[receiver] += int(time_taken)
    else:
        phone_numbers_and_total_time_on_the_phone[receiver] = int(time_taken)

    if (phone_numbers_and_total_time_on_the_phone[caller] > time_of_longest_on_the_phone):
        phone_number_longest_on_the_phone = caller
        time_of_longest_on_the_phone = phone_numbers_and_total_time_on_the_phone[caller]

    if (phone_numbers_and_total_time_on_the_phone[receiver] > time_of_longest_on_the_phone):
        phone_number_longest_on_the_phone = receiver
        time_of_longest_on_the_phone = phone_numbers_and_total_time_on_the_phone[receiver]

print(f"{phone_number_longest_on_the_phone} spent the longest time, {time_of_longest_on_the_phone} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

