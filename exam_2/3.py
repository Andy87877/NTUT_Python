from functools import reduce


def get_rank(M, N):
    answer = (1 - N / 30) + M * 0.001
    answer *= 100

    return int(answer)


def main():
    K = int(input())

    score_weight = []

    for _ in range(K):
        score, weight = list(map(eval, input().split()))

        score_weight.append([score, weight])

    N = int(input())

    M = reduce(lambda x, y: x + y[0] * y[1], score_weight, 0)

    print(get_rank(M, N), end="%")


main()
