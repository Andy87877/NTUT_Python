# page 14

with open("passwd.txt") as f1:
    # 遍歷檔案的每一行內容 ;
    for line in f1:
        # 字串替換
        bline = line.replace("root", "west")
        with open("tmp.txt", "a+") as f2:
            # 寫入新檔案
            f2.write(bline)
