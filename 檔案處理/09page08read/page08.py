
# page 02
outfile = open('filename.txt', 'w') # 以寫入模式開檔 
outfile.write('test1甲\n')
outfile.write('test2乙\n')
outfile.write('test3丙\n')
outfile.close()


# page 08
#with open('filename.txt', 'r') as fp:
#    for line in fp.readlines():    # 一次讀取所有資料，再一行一行處理
#        print(line, end='')
#
#fp.close()


# page 08
# Python 讀檔將每行資料存到串列中的元素，上述程式可簡化
with open('filename.txt', 'r') as fp:
    for line in fp:
        print(line, end='')

fp.close()

