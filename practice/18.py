def print_char(chr, n):
    for i in range(n):
        print(chr, end="")

# 正三角形
def C1(N):
    for i in range(1,N+1):
        print_char("#", N-i)
        print_char("*", i*2-1)
        print_char("#", N-i)
        print()

# 倒三角形
def C2(N):
    for i in range(1,N+1):
        print_char("#", i-1)
        print_char("*", (N-i+1)*2-1)
        print_char("#", i-1)
        print()

# 菱形
def C3(N):
    for i in range(N//2+1):
        print_char(" ", N//2-i)
        print_char("*", i*2+1)
        print_char(" ", N//2-i)
        print()

    for i in range(N//2-1, -1, -1):
        print_char(" ", N//2-i)
        print_char("*", i*2+1)
        print_char(" ", N//2-i)
        print()

# 魚形
def C4(N):
    for i in range(N//2+1):
        print_char(" ", N//2-i)
        print_char("*", i*2+1)
        print_char(" ", (N//2-i)*2)
        print_char("-", i)
        print()
    for i in range(N//2-1,-1,-1):
        print_char(" ", N//2-i)
        print_char("*", i*2+1)
        print_char(" ", (N//2-i)*2)
        print_char("-", i)
        print()

def main():
    C = int(input())
    N = int(input())

    if (N%2 == 0 or N >= 50 or N <= 2):
        print("error")
    elif (C == 1):
        C1(N)
    elif (C == 2):
        C2(N)
    elif (C == 3):
        C3(N)
    elif (C == 4):
        C4(N)
    else:
        print("error")

main()