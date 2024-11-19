# page 09

# 開啟檔案
fp = open("out.txt", "a")
# 寫入 This is a testing! 到檔案緩衝區
print("This is a testing!\n", file=fp)
# 將緩衝區寫入檔案，關閉檔案
fp.close()
