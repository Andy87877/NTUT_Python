
# page 02
outfile = open('hello.txt', 'w') # 以寫入模式開檔 
outfile.write('test1甲\n')
outfile.write('test2乙\n')
outfile.write('test3丙\n')
outfile.close()


# page 07
with open('hello.txt', 'r') as fp:
    data = fp.readlines()
    print(type(data))
    print(data)


fp.close()






