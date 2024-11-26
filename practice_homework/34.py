relate_dic = {}
friend_dic = {}
friend_list = [[], [], [], [], [], [], [], [], [], []]

N = 0  # 人數


def input_data():
    while True:
        tmp_list = list(input().split())
        if len(tmp_list) == 1:
            break

        X = tmp_list[0]
        Y = tmp_list[1]
        K = tmp_list[2]
        relate_dic[(X, Y)] = K


def find_friend():
    for i in range(N):
        for j in range(i + 1, N):
            X = chr(i + 65)
            Y = chr(j + 65)

            # print(X, Y)
            if ((X, Y) in relate_dic) and ((Y, X) in relate_dic):
                relate_number = min(relate_dic[(X, Y)], relate_dic[(Y, X)])
                friend_dic[(X, Y)] = relate_number
                friend_dic[(Y, X)] = relate_number

                friend_list[i].append(j)
                friend_list[j].append(i)


# 1.2行 (找A.B最近的朋友)
def near_friend():
    friend_check = [False] * 10

    now_check = 0
    path = [0]
    friend_check[0] = True

    check_list = [0]  # 要檢查的名單
    path_list = [[0]]  # 路徑

    while friend_check[1] != True:
        END = False
        now_check = check_list[0]
        path = path_list[0]

        check_list.remove(now_check)
        path_list.remove(path)

        now_friend_list = friend_list[now_check]
        for i in range(len(now_friend_list)):
            friend = now_friend_list[i]

            if friend_check[friend] == False:
                friend_check[friend] = True
                check_list.append(friend)

                tmp_path = []
                for path_index in range(len(path)):
                    tmp_path.append(path[path_index])
                tmp_path.append(friend)
                path_list.append(tmp_path)

            if friend == 1:
                path = path_list[-1]
                END = True
                break
        if END:
            break

    # print
    print(len(path) - 1)
    for i in range(len(path) - 1):
        print(chr(path[i] + 65), end=" ")
    print(chr(path[-1] + 65))


# 3.4行 (找到最大的熟悉度)
def most_familiarity_friend():
    ans_number = -1
    ans_path = [0, 1]

    now_check = 0
    path = [0]
    familiarity = 0

    check_list = [0]  # 要檢查的名單
    path_list = [[0]]  # 路徑
    familiarity_list = [0]  # 熟悉度

    while len(check_list) != 0:
        now_check = check_list[0]
        path = path_list[0]
        familiarity = familiarity_list[0]

        check_list.remove(now_check)
        path_list.remove(path)
        familiarity_list.remove(familiarity)

        now_friend_list = friend_list[now_check]
        for i in range(len(now_friend_list)):
            friend = now_friend_list[i]

            if not (friend in path):
                check_list.append(friend)

                tmp_familiarity = familiarity + int(
                    friend_dic[(chr(now_check + 65), chr(friend + 65))]
                )
                familiarity_list.append(tmp_familiarity)

                tmp_path = []
                for path_index in range(len(path)):
                    tmp_path.append(path[path_index])
                tmp_path.append(friend)
                path_list.append(tmp_path)

                if friend == 1:
                    if ans_number < familiarity_list[-1]:
                        ans_path = path_list[-1]
                        ans_number = familiarity_list[-1]
    # print
    print(ans_number)
    for i in range(len(ans_path) - 1):
        print(chr(ans_path[i] + 65), end=" ")
    print(chr(ans_path[-1] + 65))


def main():
    input_data()
    find_friend()

    near_friend()

    most_familiarity_friend()


N = int(input())  # 幾個人
main()
