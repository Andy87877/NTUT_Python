def show(List):
    n = len(List)
    for i in range(n):
        for j in range(n):
            print(List[i][j], end = " ")
        print()

def init(n):
    List = []
    for i in range(n):
        tmp = []
        for j in range(1,n+1):
            num = (i*n + j)
            tmp.append(num)
        List.append(tmp)

    return List

def change_times():
    str_change = input()
    clockwise_times = 0

    for i in range(len(str_change)):
        if (str_change[i] == 'R'):
            clockwise_times += 1
        else:
            clockwise_times -= 1

    if (clockwise_times >= 4):
        clockwise_times %= 4
    elif (clockwise_times < 0):
        counter_times = abs(clockwise_times)
        counter_times %= 4
        clockwise_times = (4 - counter_times) % 4

    return clockwise_times

def clockwise(List):
    n = len(List)
    new_List = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            new_List[i][j] = List[n-j-1][i]

    return new_List

def main():
    n = int(input())
    List = init(n)
    
    clockwise_times = change_times()

    for i in range(clockwise_times):
        List = clockwise(List)

    show(List)

main()