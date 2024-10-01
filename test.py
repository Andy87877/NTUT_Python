def test02():
    A = 'Thank#John@I@am@fine'
    B = 'Hello@John'
    # C = 
    print(B,A[5]*2) #1
    print(B[-1]) #2
    print(A[::4]) #3
    print(A[3:-3:3]) #4
    A_len = len(A)
    print(A[-7::]) #5
    B = A.split('@')
    print(B[3]) #6
test02()