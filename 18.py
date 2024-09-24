def C1(N):
    for i in range(1,N+1):
        for j in range(N-i):
            print("#",end = "")
        for j in range(i*2-1):
            print("*",end = "")
        for j in range(N-i):
            print("#",end = "")
        print()

def C2(N):
    for i in range(1,N+1):
        for j in range(i-1):
            print("#",end = "")
        for j in range((N-i+1)*2-1):
            print("*",end = "")
        for j in range(i-1):
            print("#",end = "")
        print()

def C3(N):
    N = 1

def main():
    C = int(input())
    N = int(input())

    if (N%2 == 0):
        print("error")
    elif (C == 1):
        C1(N)
    elif (C == 2):
        C2(N)
    elif (C == 3):
        C3(N)

main()