def forOps(m,n):
    sum = 0
    multi = 1
    for index in range(m, n+1, 2):
        sum += index
        multi *= index
        print(index, end = ", ")
    print("\n相加總合", sum)
    print("\n相乘總和", multi)

forOps(6, 12)