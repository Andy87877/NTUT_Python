def get_score(A, B, C):
    score = 0
    List = [A,B,C]
    for i in range(3):
        if ((ord(List[i][0]) >= ord('2')) and (ord(List[i][0]) <= ord('9'))):
            score += (ord(List[i])-ord('0'))
        elif (List[i] == '10'):
            score += 10
        else:
            score += 0.5

    if (score > 10.5):
        score = 0
    return score

# input
player_name = input()
P = [0,0,0]
P[0] = input()
P[1] = input()
P[2] = input()

banker_name = input()
B = [0,0,0]
B[0] = input()
B[1] = input()
B[2] = input()

# score
player_score = get_score(P[0], P[1], P[2])
banker_score = get_score(B[0], B[1], B[2])

# P1
if (player_score == 0):
    print("%c Win"%(banker_name))
else:
    if (player_score == banker_score):
        print("Tie")
    elif (player_score > banker_score):
        print("%c Win"%(player_name))
    else:
        print("%c Win"%(banker_name))

# P2
if (player_score == banker_score):
    print("Tie")
elif (player_score > banker_score):
    print("%c Win"%(player_name))
else:
    print("%c Win"%(banker_name))