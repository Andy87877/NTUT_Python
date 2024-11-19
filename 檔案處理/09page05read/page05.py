# page 02
outfile = open("hello.txt", "w", encoding="utf-8")  # 以寫入模式開檔
outfile.write("test1甲\n")
outfile.write("test2乙\n")
outfile.write("test3丙\n")
outfile.close()


# page 02
infile = open("hello.txt", "r", encoding="utf-8")  # 以讀取模式開檔
infile.close()


# page 05
with open("hello.txt", "r", encoding="utf-8") as infile:
    data = infile.read()  # 一次讀全部
    print(data)

infile.close()
