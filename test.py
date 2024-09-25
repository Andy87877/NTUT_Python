a = []

n = 10

for i in range(n):
    tmp = ["中文 "]*n
    # for j in range(n):
    #     tmp.append(abs(i-j))
    a.append(tmp)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = " ")
    print()