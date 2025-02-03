import math


def main():
    N = int(input())

    Data = []

    for i in range(N):
        input_list = input().split()

        name = input_list[0]
        score_list = list(map(int, input_list[1:]))

        avg = sum(score_list) / len(score_list)
        avg = int(avg)

        Data.append([name, avg])

    def is_ok(data):
        return data[1] >= 60

    ok_data = list(filter(is_ok, Data))

    sort_data = sorted(ok_data, key=lambda x: x[1])

    for i in range(len(sort_data)):
        print(sort_data[i][0], sort_data[i][1])


main()
