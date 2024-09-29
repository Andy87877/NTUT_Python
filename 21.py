Card = []
Card_face = []
Card_color = []

def check_number(Card_face, Card_color):
    n = len(Card_face)

    # 9 Straight flush
    Flush = True # 花色一樣
    for i in range(n):
        if (Card_color[i] != Card_color[0]):
            Flush = False

    Straight = True # 數字連續的五張牌
    tmp_face = Card_face
    tmp_face = sorted(tmp_face)
    print(tmp_face)

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
    

def classificate(Card):
    # 分類
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

def main():
    Card = list(input().split())
    ERROR, Card_face, Card_color = classificate(Card)

    # print(ERROR, Card_face, Card_color)
    if (ERROR):
        print("Error input")
    else:
        ans = check_number(Card_face, Card_color)
        print(ans)

main()