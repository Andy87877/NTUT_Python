def M1(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,end = "")
        for j in range(i-1, 0, -1):
            print(j,end = "")
        print()

def M2(N):
    for i in range(1,N+1):
        for j in range(N-i):
            print("_", end = "")

        for j in range(1,i+1):
            print(j,end = "")
        for j in range(i-1, 0, -1):
            print(j,end = "")
        
        for j in range(N-i):
            print("_", end = "")

        print()

def M3(N):
    for i in range(N, 0, -1):
        for j in range(N-i):
            print("_", end = "")

        for j in range(1,i+1):
            print(j,end = "")
        for j in range(i-1, 0, -1):
            print(j,end = "")
        
        for j in range(N-i):
            print("_", end = "")

        print()

def main():
    M = int(input())
    N = int(input())

    if (M == 1):
        M1(N)
    if (M == 2):
        M2(N)
    if (M == 3):
        M3(N)

main()