def route(data, start, rout, money):
    if (start in rout) or (start == 0):
        return money

    rout.append(start)
    for sum in data:
        if sum[0] == start:
            money = money + sum[1]
            # print(sum[2],sum[3])
            max_money = max(
                route(data, sum[2], rout, money), route(data, sum[3], rout, money)
            )

    rout.pop()

    return max_money


def main():
    n_start = list(map(int, input().split()))
    data = list()
    for _ in range(n_start[0]):
        a = list(map(int, input().split()))
        data.append(a)
    # print(data)
    rout, start, money = list(), n_start[1], 0
    print(route(data, start, rout, money))

    # total = sorted(total,reverse = True)
    # print(total[0])


main()
