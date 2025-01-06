def get_route(data, start, route, money):
    print(start, route, money)
    if (start in route) or (start == 0):
        return money

    route.append(start)

    for tmp_cave in data:
        if tmp_cave[0] == start:
            print(money, tmp_cave[1], money + tmp_cave[1])
            money = money + tmp_cave[1]

            max_money = max(
                get_route(data, tmp_cave[2], route, money),
                get_route(data, tmp_cave[3], route, money),
            )

    route.pop()
    return max_money


def main():
    N, start_num = list(map(int, input().split()))
    data = []
    for _ in range(N):
        tmp_input = list(map(int, input().split()))
        data.append(tmp_input)

    answer = get_route(data, start_num, [], 0)

    print(answer)


main()
