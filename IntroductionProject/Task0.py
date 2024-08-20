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

first_text_record_incoming_number = texts[0][0]
first_text_record_answering_number = texts[0][1]
first_text_record_time = texts[0][2]

last_call_record = calls[len(calls) - 1]
last_call_record_incoming_number = last_call_record[0]
last_call_record_answering_number = last_call_record[1]
last_call_record_time = last_call_record[2]
last_call_record_duration = last_call_record[3]

print(f"First record of texts, {first_text_record_incoming_number} texts {first_text_record_answering_number} at time {first_text_record_time}")
print(f"Last record of calls, {last_call_record_incoming_number} calls {last_call_record_answering_number} at time {last_call_record_time}, lasting {last_call_record_duration} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

