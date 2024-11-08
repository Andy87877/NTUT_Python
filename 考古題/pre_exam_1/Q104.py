def main():
    N = int(input())
    name_list = []
    class_list = []

    for _ in range(N):
        name = input()
        name_list.append(name)

        times = int(input())
        tmp_list = []
        for i in range(times):
            class_time = input()
            tmp_list.append(class_time)
        class_list.append(tmp_list)

    # check
    for i in range(N):
        for j in range(i + 1, N):

            for i_index in range(len(class_list[i])):
                for j_index in range(len(class_list[j])):
                    if class_list[i][i_index] == class_list[j][j_index]:
                        print("%s and %s" % (name_list[i], name_list[j]), end=" ")
                        print("conflict on %s" % (class_list[i][i_index]))
                        exit()


main()
