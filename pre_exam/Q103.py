def init(N):
    arr = []
    for i in range(N):
        tmp = []
        for j in range(1, N + 1):
            tmp.append(i * N + j)
        arr.append(tmp)

    tmp_list = [[]] * N
    for i in range(N):
        tmp_list[i].append(-1)
    return arr, tmp_list


def D1(N, arr, tmp_list):
    for i in range(N):
        for j in range(N):
            tmp_list[i][j] = arr[j][N - i - 1]
            print("%3d" % (tmp_list[i][j]), end="")
        print()


def D2(N, arr, tmp_list):
    for i in range(N):
        for j in range(N):
            tmp_list[i][j] = arr[N - j - 1][i]
            print("%3d" % (tmp_list[i][j]), end="")
        print()


def D3(N, arr, tmp_list):
    for i in range(N):
        for j in range(N):
            tmp_list[i][j] = arr[N - i - 1][j]
            print("%3d" % (tmp_list[i][j]), end="")
        print()


def D4(N, arr, tmp_list):
    for i in range(N):
        for j in range(N):
            tmp_list[i][j] = arr[i][N - j - 1]
            print("%3d" % (tmp_list[i][j]), end="")
        print()


def main():
    N = int(input())
    D = int(input())

    arr, tmp_list = [], []
    arr, tmp_list = init(N)

    if D == 1:
        D1(N, arr, tmp_list)
    if D == 2:
        D2(N, arr, tmp_list)
    if D == 3:
        D3(N, arr, tmp_list)
    if D == 4:
        D4(N, arr, tmp_list)


main()
