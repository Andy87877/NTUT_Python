def move(n, x, y):
    print(n, ":", x, "->", y)


# n層，A搬到C，透過B
def hanoi(n, A, C, B):
    if n == 1:
        move(n, A, C)
    else:
        hanoi(n - 1, A, B, C)
        move(n, A, C)
        hanoi(n - 1, B, C, A)


# 二層，A搬到C，透過B


hanoi(5, "A", "C", "B")
