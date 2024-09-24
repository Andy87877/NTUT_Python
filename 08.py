name = []
time = []

end = False

for i in range(3):
    n = input()
    name.append(n)

    H = int(input())

    if (H > 3 or H <= 0):
        end = True

    tmp = []

    for j in range(H):
        n = input()
        if not(ord(n[0]) >= ord('1') and ord(n[0]) <= ord('5')):
            end = True
        if not(ord(n[1]) >= ord('1') and ord(n[1]) <= ord('9')):
            if not (n[1] == 'a' or n[1] == 'b' or n[1] == 'c'):
                end = True

        tmp.append(n)
    
    time.append(tmp)
    
if (end):
    print(-1)
else:
    # judge
    flag = True
    for i in range(3):
        for i_2 in range(i+1,3):
            for j in range(len(time[i])):
                for j_2 in range(len(time[i_2])):
                    if (time[i][j] == time[i_2][j_2]):
                        print("%s,%s,%s"%(name[i], name[i_2], time[i][j]))
                        flag = False

    if (flag):
        print("correct")