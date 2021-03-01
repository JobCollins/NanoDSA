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

def test(uniq):
    symmetric_diff = set([list(line)[0] for line in texts]).symmetric_difference(set([list(line)[0] for line in calls]))
    common_vals = set([list(line)[0] for line in texts]).intersection(set([list(line)[0] for line in calls]))

    assert len(symmetric_diff)+len(common_vals) == len(uniq)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = set([list(line)[0] for line in texts]).union(set([list(line)[0] for line in calls]))
print("There are {} different telephone numbers in the records.".format(len(unique_numbers)))

test(unique_numbers)