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
    for i in range(N//2+1):
        for j in range(N//2-i):
            print(" ",end = "")
        for j in range(i*2+1):
            print("*",end = "")
        for j in range(N//2-i):
            print(" ",end = "")
        print()

    for i in range(N//2-1, -1, -1):
        for j in range(N//2-i):
            print(" ",end = "")
        for j in range(i*2+1):
            print("*",end = "")
        for j in range(N//2-i):
            print(" ",end = "")
        print()

def C4(N):
    for i in range(N//2+1):
        for j in range(N//2-i):
            print(" ",end = "")
        for j in range(i*2+1):
            print("*",end = "")
        for j in range((N//2-i)*2):
            print(" ",end = "")
        for j in range(i):
            print("-",end = "")
        print()
    for i in range(N//2-1,-1,-1):
        for j in range(N//2-i):
            print(" ",end = "")
        for j in range(i*2+1):
            print("*",end = "")
        for j in range((N//2-i)*2):
            print(" ",end = "")
        for j in range(i):
            print("-",end = "")
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