
# page 02
outfile = open('hello.txt', 'w', encoding="utf-8") # 以寫入模式開檔 
outfile.write(u'test1甲\n')
outfile.write(u'test2乙\n')
outfile.write(u'test3丙\n')
outfile.close()


# page 02
infile = open('hello.txt', 'r', encoding="utf-8") # 以讀取模式開檔
infile.close()


# page 06
with open('hello.txt', 'r', encoding="utf-8") as infile:
    while True:                         # 無窮迴圈
        data = infile.readline()    # 一次讀一行資料
        print(data)
        if not data:                       # 所有資料讀取完畢
            print('end reading...')
            break

infile.close()
