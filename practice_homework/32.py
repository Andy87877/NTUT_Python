Board = []  # 數獨棋盤


# 輸出數獨
def print_board():
    for i in range(4):
        for j in range(3):
            print(Board[i][j], end=" ")
        print(Board[i][3])


# 初始化(輸入) 數獨
def input_board():
    for i in range(4):
        Board.append([])
        List_row = list(map(int, input().split()))

        for j in range(4):
            Board[i].append(List_row[j])


# 找到的數字 0 = 沒辦法
def check_list(Tmp_list):
    Check = [0, 0, 0, 0]
    for i in range(4):
        for j in range(1, 5):
            if Tmp_list[i] == j:
                Check[j - 1] += 1

    ans = 0
    for j in range(4):
        if Check[j] == 0:
            if ans != 0:
                return 0
            ans = j + 1
    return ans


# 找是否能填的數字
def find_number(i, j):
    # Column
    Tmp_list = []
    for a in range(4):
        Tmp_list.append(Board[i][a])
    num = check_list(Tmp_list)
    if num != 0:
        return num

    # Row
    Tmp_list = []
    for a in range(4):
        Tmp_list.append(Board[a][j])
    num = check_list(Tmp_list)
    if num != 0:
        return num

    # Block
    Tmp_list = []
    if i <= 1 and j <= 1:  # 左上
        Tmp_list = [Board[0][0], Board[0][1], Board[1][0], Board[1][1]]
    elif i >= 2 and j <= 1:  # 右上
        Tmp_list = [Board[2][0], Board[2][1], Board[3][0], Board[3][1]]
    elif i <= 1 and j >= 2:  # 左下
        Tmp_list = [Board[0][2], Board[0][3], Board[1][2], Board[1][3]]
    else:
        Tmp_list = [Board[2][2], Board[2][3], Board[3][2], Board[3][3]]
    num = check_list(Tmp_list)
    # print(Tmp_list, num)
    return num


# 做數獨 (尋找0 直到沒有0)
def Doing_Sudoku():
    END = False
    times = 0
    while (not END) and (times < 10):
        END = True

        # print_board()

        for i in range(4):
            for j in range(4):
                if Board[i][j] == 0:
                    number = find_number(i, j)
                    END = False
                    if number != 0:
                        Board[i][j] = number

        times += 1


def main():
    input_board()
    Doing_Sudoku()
    print_board()


main()
