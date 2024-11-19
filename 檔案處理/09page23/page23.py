# page 23

import csv


def trans(row):
    data = {}
    score = 0
    subject = ["國文", "英文", "數學"]
    for key, value in row.items():
        # print('=>', key, value)
        if key in subject:
            score = score + int(value)
    for key, value in row.items():
        if key == "班級":
            data["Class"] = value
        elif key == "學號":
            data["Student Id"] = value
    data["average"] = score // 3
    return data


with open("score.csv", encoding="utf-8", newline="") as csvfile:
    readFile = csv.DictReader(csvfile)
    # print(readFile)
    inData = []
    for row in readFile:
        print(row)
        inData.append(trans(row))

print(inData)

with open("output.csv", "w", encoding="utf-8", newline="") as csvfile:
    # columns = ['班級', '學號','國文','數學','英文']
    columns = ["Class", "Student Id", "average"]
    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=",")
    writer.writeheader()  # 寫入第一列的欄位名稱
    for data in inData:
        writer.writerow(data)  # 寫入資料
