def summation(n):
    total = 0 
    for i in range(n+3, 1, -2): 
        if i % 2 == 0 : 
            total += i
        else: 
            total -= i
    return total, i
def test(): 
    result, n = summation(9) 
    print(type(result)) #(1)
    print(n) #(2)
    print(result) #(3)
test()