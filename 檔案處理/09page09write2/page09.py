
# page 09

# 開啟檔案
fp = open("filename.txt", "w") 
# 將 lines 所有內容寫入到緩衝區
lines = ["One\n", "Two\n", "Three\n"]
fp.writelines(lines) 
#將緩衝區寫入檔案，關閉檔案
fp.close()
