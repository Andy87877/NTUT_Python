def forOps():
    i = 1
    myList = ["asm", "python", "C++", "Java", "iOS", "perl", 
    "C#"]
    for index in myList :
        if (index == "Java"):
            print(i,index, end=', ')
        elif (index == "python"):
            print(i, index, end=', ') 
        elif (i%2!=0):
            print(i, index, end=', ')
            i = i+1
        else:
            i=i+1
forOps()
