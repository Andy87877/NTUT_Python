Name_list = ["."] * 3
Class_list = [[]] * 3


def check_conflict():
    Confilct = False

    for i in range(3):
        for j in range(i + 1, 3):
            for i_index in range(len(Class_list[i])):
                for j_index in range(len(Class_list[j])):
                    if Class_list[i][i_index] == Class_list[j][j_index]:
                        print(
                            "%s,%s,%s"
                            % (Name_list[i], Name_list[j], Class_list[i][i_index])
                        )
                        Confilct = True

    return Confilct


def check_input_error(List):
    for i in range(len(List)):
        now_name = List[i]
        if len(now_name) != 2:
            return True

        Day_list = ["1", "2", "3", "4", "5"]
        Day = now_name[0]
        if Day not in Day_list:
            return True

        lesson_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c"]
        lesson = now_name[1]
        if lesson not in lesson_list:
            return True

    return False


def input_data(index):
    name = input()
    Name_list[index] = name

    tmp_list = []
    H = int(input())
    for i in range(H):
        name_class = input()
        tmp_list.append(name_class)
    Class_list[index] = tmp_list


def main():
    N = 3
    for i in range(N):
        input_data(i)

    ERROR = False
    for i in range(N):
        ERROR = check_input_error(Class_list[i]) or ERROR

    if ERROR:
        print("-1")
        exit()

    Confilct = check_conflict()
    if not Confilct:
        print("correct")


main()
