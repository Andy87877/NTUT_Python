def main():
    N = int(input())
    data = []

    def is_ok(data):
        return data[1] >= int(70 * 0.8)

    for _ in range(N):
        name, money = input().split()
        money = int(int(money) * 0.8)
        data.append([name, money])

        data = list(filter(is_ok, data))

    sort_data = sorted(data, key=lambda x: x[1], reverse=True)

    for name, money in sort_data:
        print(name, money)

    # print(sort_data)


main()
