
# page 21

import csv

with open('output.csv', 'w', encoding = 'utf-8', newline='') as csvfile:
    columns = ['班級', '學號', '成績']
    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=':') 
    writer.writeheader()    # 寫入第一列的欄位名稱
    writer.writerow({'班級': '資工一', '學號': '109590003', '成績': 95})    # 寫入資料
    writer.writerow({'班級': '資工一', '學號': '109590004', '成績': 88})    # 寫入資料
