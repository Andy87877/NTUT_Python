
# page 12

fp = open('hello.txt', 'w') 
fp.write("First line\n#Second line\n#Third line") 
fp.close()

with open('hello.txt', 'r') as infile:
    data = infile.read()
    print(data)
    #print(data[0], data[-1])
