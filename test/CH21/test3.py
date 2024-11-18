#

# bytes 轉字串 string 方式一
b = b"\xe9\x80\x86\xe7\x81\xab"
string = str(b, "utf-8")
print(string)
# bytes 轉字串 string 方式二
b = b"\xe9\x80\x86\xe7\x81\xab"
string = b.decode()  # 第一參數預設utf-8，第二參數預設 strict
print(string)
# bytes 轉字串 string 方式三
b = b"\xe9\x80\x86\xe7\x81haha\xab"
string = b.decode("utf-8", "ignore")  # 忽略非法字符，用strict會拋出異常
print(string)
# bytes 轉字串 string 方式四
b = b"\xe9\x80\x86\xe7\x81haha\xab"
string = b.decode("utf-8", "replace")  # 用？取代非法字符
print(string)
