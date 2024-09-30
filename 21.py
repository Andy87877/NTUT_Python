Card = []
Card_face = []
Card_color = []

# main (ans = Ans_check_number)
def Ans_check_number(Card_face, Card_color):
    n = len(Card_face)

    # flush
    Flush = True # 花色一樣
    for i in range(n):
        if (Card_color[i] != Card_color[0]):
            Flush = False
    # Straight
    Straight = check_Straight(Card_face) # 數字連續的五張牌

    # 9 Straight flush 
    if (Flush and Straight):
        return 9
    
    Face_times = check_Face_times(Card_face)

    # 8 Four of a kind
    if (Face_times[0] == 4):
        return 8

    # 7 Full House : Three of a Kind
    if (Face_times[0] == 3 and Face_times[1] == 2):
        return 7

    # 6 Flush 
    if (Flush):
        return 6

    # 5 Straight 
    if (Straight):
        return 5

    # 4 Three of a kind
    if (Face_times[0] == 3):
        return 4
    
    # 3 Two pairs
    if (Face_times[0] == 2 and Face_times[1] == 2):
        return 3

    # 2 One pair
    if (Face_times[0] == 2):
        return 2
    
    # High Card
    return 1

# 牌面次數
def check_Face_times(Card_face):
    face_stand = ['A', '2','3','4','5','6','7','8','9','10','J','Q','K']
    Face_times = [0]*(len(face_stand))
    for i in range(len(Card_face)):
        for j in range(len(face_stand)):
            if (Card_face[i] == face_stand[j]):
                Face_times[j] += 1
                break

    Face_times = sorted(Face_times, reverse = True)
    # print(Face_times)
    return Face_times

# 牌面連續的五張牌
def check_Straight(Card_face):
    face_stand = ['A', '2','3','4','5','6','7','8','9','10','J','Q','K']
    check_stand = [False]*(len(face_stand))

    for i in range(len(Card_face)):
        for j in range(len(face_stand)):
            if (Card_face[i] == face_stand[j]):
                check_stand[j] = True
    
    Straight = False
    # 0~ -13
    for i in range(0, -14,-1): # head
        flag = True
        for j in range(0,5):
            if (check_stand[i+j] != True):
                flag = False
                break

        Straight = flag or Straight
    
    return Straight

def check_ERROR(ca):
    ERROR = False
    face_stand = ['A', '2','3','4','5','6','7','8','9','10','J','Q','K']
    color_stand = ['S', 'H', 'D', 'C']
    Face = '0'
    color = '0'

    if (len(ca) == 1 or len(ca) > 3):
        ERROR = True

    if (ca[0] == '1' and ca[1] == '0'):
        Face = '10'
        if (len(ca) != 3):
            ERROR = True
        color = ca[2]
    else:
        if (len(ca) != 2):
            ERROR = True
        Face = ca[0]
        color = ca[1]

    stand_F = False
    for i in range(len(face_stand)):
        if (face_stand[i] == Face):
            stand_F = True
    stand_C = False
    for i in range(len(color_stand)):
        if (color_stand[i] == color):
            stand_C = True
    if (not(stand_F and stand_C)):
        ERROR = True
    

    return ERROR, Face, color
    
# 分類
def classificate(Card):
    ERROR = False
    n = len(Card)
    Card_face = []
    Card_color = []

    for i in range(n):
        ca = Card[i]
        ERROR1, Face, color = check_ERROR(ca)
        ERROR = ERROR or ERROR1
        Card_face.append(Face)
        Card_color.append(color)

    
    return (ERROR, Card_face, Card_color)

# 是否有重複的牌
def check_Duplicate(Card):
    Duplicate = False
    for i in range(len(Card)):
        for j in range(i+1,len(Card)):
            if (Card[i] == Card[j]):
                Duplicate = True
    
    return Duplicate

# 主程式
def main():
    Card = list(input().split())
    ERROR, Card_face, Card_color = classificate(Card)
    Duplicate = check_Duplicate(Card)

    # print(ERROR, Card_face, Card_color)
    if (ERROR):
        print("Error input")
    elif (Duplicate):
        print("Duplicate deal")
    else:
        ans = Ans_check_number(Card_face, Card_color)
        print(ans)

main()