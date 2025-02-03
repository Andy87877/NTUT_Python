def get_answer(N, M):
    number = (1 - N / 30) + M * 0.001
    number *= 100
    number = int(number)

    return number


def main():
    K = int(input())

    M = 0

    for i in range(K):
        score, weight = list(map(eval, input().split()))
        M += score * weight

    N = int(input())

    answer = get_answer(N, M)

    print(answer, end="%")


main()
