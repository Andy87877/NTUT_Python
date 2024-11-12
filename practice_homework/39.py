def print_matrix_or_circle(N, arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def get_matrix(N):
    command_list = list(map(int, input().split()))

    matrix = []
    now_index = 0

    for i in range(N):
        tmp_arr = []
        for j in range(N):
            tmp_arr.append(command_list[now_index])
            now_index += 1
        matrix.append(tmp_arr)

    return matrix


def get_check_circle(N, matrix, circle_number_list):
    check_circle = []
    for i in range(N):
        tmp_arr = []
        for j in range(N):
            if matrix[i][j] in circle_number_list:
                tmp_arr.append("O")
            else:
                tmp_arr.append("X")
        check_circle.append(tmp_arr)
    return check_circle


def check_lines(N, check_circle):
    line_OK = 0

    # 檢查橫的
    for i in range(N):
        flag = True
        for j in range(N):
            if check_circle[i][j] != "O":
                flag = False
                break
        if flag:
            line_OK += 1

    # 檢查直的
    for i in range(N):
        flag = True
        for j in range(N):
            if check_circle[j][i] != "O":
                flag = False
                break
        if flag:
            line_OK += 1

    # 檢查斜的 (左上到右下)
    flag = True
    for i in range(N):
        if check_circle[i][i] != "O":
            flag = False
            break
    if flag:
        line_OK += 1

    # 檢查斜的 (左下到右上)
    flag = True
    for i in range(N):
        if check_circle[i][N - i - 1] != "O":
            flag = False
            break
    if flag:
        line_OK += 1

    return line_OK


def judge_winner(A_lines, B_lines):
    if A_lines > B_lines:
        return "A Win"
    if A_lines < B_lines:
        return "B Win"
    return "Tie"


def main():
    N = int(input())
    M = int(input())

    matrix_A = get_matrix(N)
    matrix_B = get_matrix(N)

    circle_number_list = list(map(int, input().split()))

    check_circle_A = get_check_circle(N, matrix_A, circle_number_list)
    check_circle_B = get_check_circle(N, matrix_B, circle_number_list)

    A_lines = check_lines(N, check_circle_A)
    B_lines = check_lines(N, check_circle_B)

    answer = judge_winner(A_lines, B_lines)
    print(answer)


main()
