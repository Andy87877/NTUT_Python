
# page 17

import csv


import csv
with open('data.csv', encoding = 'utf-8') as csvfile:
    readFile = csv.reader(csvfile)
    for row in readFile:
        print(row)



