def check(a):
    if (int(a[0]) > 5):
        print(-1)
        return False
    else:
        return True

def check_class(list_x,list_y):
    time = 0
    tsonto = False
    if (list_x[1]) <= (list_y[1]):
        time = list_x[1]
    else:
        time = list_y[1]
    for i in range(time):
        for j in range(time):
            if (list_x[i+2]) == (list_y[j+2]):
                print(list_x[0] + "," + list_y[0] + "," + list_x[i+2])
                tsonto = True
    return tsonto

                
def check_tson(classs):
    tsonto = False
    for i in range(len(classs)):
        j = i + 1
        for j in range(j,len(classs)):
            tsonto = (check_class(classs[i],classs[j]) or tsonto)
    return tsonto



def main():
    N = int(input())
    classs = []
    tsonto = False
    check_input = True
    for i in range(N):
        table = []
        class_name = input()
        table.append(class_name)
        class_time = int(input())
        table.append(class_time)
        classs.append(table)
        x = []
        for _ in range(classs[i][1]):
            a = input()
            if check_input == True:
                check_input = check(a)
            classs[i].append(a)

    if check_input == True:
        tsonto = (check_tson(classs) or tsonto)
        if tsonto == False:
            print("correct")
    
main()