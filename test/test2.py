def go(m, n):
    print("02", end = "-")
    i=0
    while (True):
        print("03-04-05", end = "-")
        m = m + i
        if (m > n):
            print("06", end = "-")
            break
        # print(m, i)
        print("07-08", end = "-")
        if (m < 8):
            print("09-10", end = "-")
            i = i + 10
            continue
        print("11-12", end = "-")
        # print(m, i)
        i = i + 5
    print("13", end = "-")
    # print(m, i)
go(4, 19)