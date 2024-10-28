def print_mark(i, mark):
    for j in range(i):
        print(mark, end = "")

def G1(L):
    for i in range(L):
        print_mark(i+1, i+1)
        print_mark(L-i-1, "#")
        print()
    
def G2(L):
    for i in range(L):
        print_mark((L-i-1)*2, "#")

        for j in range(i+1):
            print(j+1, end = "")
        for j in range(i-1,-1,-1):
            print(j+1, end = "")

        print()

def G3(L):
    for i in range(L):
        for j in range(i+1):
            print(j+1, end = "")
        print_mark((L-i-1), "^")

        print()
    
    for i in range(L-1,-1,-1):
        for j in range(i+1):
            print(i-j+1, end = "")
        print_mark((L-i-1), "^")

        print()

def G4(L):
    for i in range(L):
        print_mark((L-i-1), "^")
        for j in range(i+1):
            print(i-j+1, end = "")
        for j in range(1,i+1):
            print(j+1, end = "")
        print_mark((L-i-1), "^")

        print()

    for i in range(L-1,-1,-1):
        print_mark((L-i-1), "^")
        for j in range(i+1):
            print(i-j+1, end = "")
        for j in range(1,i+1):
            print(j+1, end = "")
        print_mark((L-i-1), "^")

        print()


def main():
    N = int(input())
    L = int(input())
    if (N == 1):
        G1(L)
    if (N == 2):
        G2(L)
    if (N == 3):
        G3(L)
    if (N == 4):
        G4(L)
main()