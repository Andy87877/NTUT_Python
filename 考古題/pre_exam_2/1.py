import math


def main():
    N = int(input())

    data = []

    for i in range(N):
        name, money = input().split()
        money = int(money)
        data.append([name, money])

    def is_ok(data):
        return data[1] >= 70

    ok_data = list(filter(is_ok, data))

    sort_data = sorted(ok_data, key=lambda x: x[1], reverse=True)

    for i in range(len(sort_data)):
        sort_data[i][1] *= 0.8
        sort_data[i][1] = math.ceil(sort_data[i][1])

        print(sort_data[i][0], sort_data[i][1])

    # print(sort_data)


main()
