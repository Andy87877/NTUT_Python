# page 15
def getHeader():  # 讀取檔案第一列和第二行
    i = 0
    with open("translate.txt", "r", encoding="utf-8") as infile:
        for line in infile:
            if i == 0:
                eng = line.split()
                print(eng)
            else:
                chi = line.split()
                print(chi)
            i = i + 1
    return eng, chi


def convert(aFile, bFile, eng, chi):
    f1 = open(aFile, "r", encoding="utf-8")
    f2 = open(bFile, "w", encoding="utf-8")
    data = f1.read()
    # zip 將 eng, chi 打包成 tuple
    for e, c in zip(eng, chi):
        data = data.replace(e, c)
        print(e, c, " :", data)
    print(data, "\n####")
    f2.write(data)
    f1.close()
    f2.close()


eng, chi = getHeader()

convert("English.txt", "Chinese.txt", eng, chi)
