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

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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

area_codes = []

def extract_area_code(record):
    called_num = record[1]

    if called_num.startswith('(0'):  # Fix land case
        return called_num.split(sep=')')[0] + ')'

    elif called_num.startswith('140'):  # Telemarketer case
        return called_num[:3]

    else:  # Mobile case
        return called_num[:4]

for record in calls:
  if record[0].startswith('(080)'):
    area_codes.append(extract_area_code(record))

area_codes_uniq = list(set(area_codes))
area_codes_uniq.sort()
# print(area_codes_uniq)

percentage_local = area_codes.count('(080)')/len(area_codes) * 100

print("The numbers called by people in Bangalore have codes: \n")
for i in area_codes_uniq:
  print("{} \n".format(i))

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_local))