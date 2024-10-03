A = [1,2,3,4]
B = 1
C = A

def change():
    A[0] = 0
    B = 0

def main():
    print(A, B, C)
    change() 
    print(A, B, C)

main()

