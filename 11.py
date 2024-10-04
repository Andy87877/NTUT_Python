import math
def compute_money(number, origal_money, discount1, discount2, discount3):
    money = origal_money
    if (number <= 10):
        money = origal_money*number
    elif (number <= 20):
        money = origal_money*number*(discount1*0.01)
    elif (number <= 30):
        money = origal_money*number*(discount2*0.01)
    else:
        money = origal_money*number*(discount3*0.01)
    
    money = round(money, 2)
    money = math.ceil(money)
    return money

def compare_print(A, B, C):
    List = [A,B,C]
    List = sorted(List)
    # print(List[0], List[1], List[2])

    for i in range(2, -1, -1):
        if (A == List[i]):
            print("A,%d" %(A))
            A = -1
        elif (B == List[i]):
            print("B,%d" %(B))
            B = -1
        elif (C == List[i]):
            print("C,%d" %(C))
            C = -1

    total_num = sum(List)
    print("%d"%(total_num))


A_discount = [0,0,0]
B_discount = [0,0,0]
C_discount = [0,0,0]

x = 0
y = 0
z = 0

x, A_discount[0], A_discount[1], A_discount[2] = map(int, input().split(","))
y, B_discount[0], B_discount[1], B_discount[2] = map(int, input().split(","))
z, C_discount[0], C_discount[1], C_discount[2] = map(int, input().split(","))

A_money = compute_money(x, 380, A_discount[0], A_discount[1], A_discount[2])
B_money = compute_money(y, 1200, B_discount[0], B_discount[1], B_discount[2])
C_money = compute_money(z, 180, C_discount[0], C_discount[1], C_discount[2])

compare_print(A_money, B_money, C_money)