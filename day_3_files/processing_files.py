####################################
# File processing in python
# -------------------------
# How to process binary, text files,
# and csv files in python.
# you may need to manipulate data in your workflow, good skill to have.
# Binary: is in machine language
# Text file: each line is terminated by an EOL
# csv file: text is separated by commas
# A tutorial I created: https://github.com/purcellconsult/Data-Manipulation-in-Python
####################################

import random
import csv
import json

# manipulating text files in python
file1 = open('Names.txt', 'a') # open file in append mode
file2 = open('Names.txt', 'w+') # puts the script in write mode
file2.write('Adam\n')
file2.write('Ben\n')
file2.write('Cindy\n')
file2.write('Daniel\n')
file2.write('Emily')

# create a file of random numbers

file3 = open('random_numbers.txt', 'a')
file4 = open('random_numbers.txt', 'w')
for x in range(100):
    file4.write(str(random.randint(1, 1000)))
    file4.write('\n')
file4.close()   # close the file

# read a file
with open('random_numbers.txt', 'r') as random_nums:
    lines = random_nums.read()
    print(lines)

with open('software_company.csv', 'w') as employees:
    file = csv.writer(employees)
    file.writerow(["John Q", "lead software engineer", 80000])
    file.writerow(["Anon Pikes", "software engineer", 75000])
    file.writerow(["Marky M", "business analyst", 65000])
    file.writerow(["Don L", "software tester", 65000])
    file.writerow(["Lisa Z", "web developer", 72000])
    file.writerow(["Melissa J", "marketer", 50000])
    file.writerow(["Daniel K", "human relations", 55000])

# creating json dumps
car = {'mileage': 159238.3}
json.dumps(car)

days = """
 {
   "mon": "Monday",
   "tues": "Tuesday",
   "wed": "Wednesday",
   "thurs": "Thursday",
   "fri": "Friday"
 }
"""

d = json.loads(days)

for x in d.values():
    print(x)