Card = []
Card_face = []
Card_color = []

Name_List = []
Card_List = []
Card_ALL = []
Ans_Card = []


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
                # print(Card[i])
                Duplicate = True
    
    return Duplicate

# 卡牌大小 
def check_and_sort(index):
    ERROR, Card_face, Card_color = classificate(Card_List[index])
    tmp_check_number = Ans_check_number(Card_face, Card_color)
    Ans_Card.append(tmp_check_number)

def print_sort_result(Name_List, Ans_Card):
    for i in range(len(Name_List)):
        for j in range(i+1,len(Name_List)):
            if (Ans_Card[i] < Ans_Card[j]):
                Ans_Card[i], Ans_Card[j] = Ans_Card[j], Ans_Card[i]
                Name_List[i], Name_List[j] = Name_List[j], Name_List[i]
    
    for i in range(len(Name_List)):
        print(Name_List[i], Ans_Card[i])

# 主程式
def main():
    TRUE_ERROR = False

    N = int(input())
    for iiiiiii in range(N):
        Card_tmp_List = list(input().split())

        Name_List.append(Card_tmp_List[0])
        Card_List.append(Card_tmp_List[1:])

        # print(Card_List)
        for Card_List_index in range(1,len(Card_tmp_List)):
            Card_ALL.append(Card_tmp_List[Card_List_index])
        # print(Card_ALL)

        ERROR, Card_face, Card_color = classificate(Card_List[iiiiiii])
        TRUE_ERROR = TRUE_ERROR or ERROR
    # print(Card_ALL)
    Duplicate = check_Duplicate(Card_ALL)

    # print(ERROR, Card_face, Card_color)
    if (TRUE_ERROR):
        print("Error input")
    elif (Duplicate):
        print("Duplicate deal")
    else:
        for i in range(N):
            check_and_sort(i)
        print_sort_result(Name_List, Ans_Card)

        

main()