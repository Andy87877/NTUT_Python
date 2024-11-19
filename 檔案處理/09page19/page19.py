# page 19

import csv

with open("class.csv", encoding="utf-8", newline="") as csvfile:
    readFile = csv.DictReader(csvfile)
    print(readFile)  # 印出 <csv.DictReader object at 0x0000025AE3F9F010>
    for row in readFile:
        print(row["班級"], row["學號"], row["期中考成績"])
