def print_mark(i, mark):
    for j in range(i):
        print(mark, end="")


def print_number(first, end, inter):
    for j in range(first, end, inter):
        print(j, end="")


def G1(L):
    for i in range(L):
        print_mark(i + 1, i + 1)
        print_mark(L - i - 1, "#")
        print()


def G2(L):
    for i in range(L):
        print_mark((L - i - 1) * 2, "#")
        print_number(1, i + 2, 1)
        print_number(i, 0, -1)

        print()


def G3(L):
    for i in range(L):
        print_number(1, i + 2, 1)
        print_mark((L - i - 1), "^")

        print()

    for i in range(L - 1, -1, -1):
        print_number(i + 1, 0, -1)
        print_mark((L - i - 1), "^")

        print()


def G4(L):
    for i in range(L):
        print_mark((L - i - 1), "^")

        print_number(i + 1, 0, -1)
        print_number(2, i + 2, 1)

        print_mark((L - i - 1), "^")

        print()

    for i in range(L - 2, -1, -1):
        print_mark((L - i - 1), "^")

        print_number(i + 1, 0, -1)
        print_number(2, i + 2, 1)

        print_mark((L - i - 1), "^")

        print()


def main():
    N = int(input())
    L = int(input())
    if N == 1:
        G1(L)
    if N == 2:
        G2(L)
    if N == 3:
        G3(L)
    if N == 4:
        G4(L)


main()
