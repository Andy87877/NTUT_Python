
# page 17

import csv
f= open('data.csv', encoding = 'utf-8')
#f= open('data.csv')
readFile = csv.reader(f)            #<_csv.reader object at 0x0000025AE3EE2EC0>
print(readFile)
for row in readFile:
    print(row)
f.close()


