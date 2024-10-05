A_card = []
B_card = []
Table_card = []

# 排型號碼
def card_number(Card):
    Color_List = []
    Face_List = []

    # Color_List, Face_List
    for i in range(5):
        card = Card[i]

        if (len(card) == 3):
            if (card[1] == '1' and card[2] == '0'):
                face = "10"
            color = card[0]
        else:
            color = card[0]
            face = card[1]
        Color_List.append(color)
        Face_List.append(face)

    # Flush 五張同花色
    Flush = True
    for i in range(1, 5):
        if (Color_List[0] != Color_List[i]):
            Flush = False
    
    # Straight 數字連續的五張牌
    Straight = False
    Face_All_card = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for i in range(-4,9):
        tmp_bool = True
        for j in range(5):
            if (not(Face_All_card[i+j] in Face_List)):
                tmp_bool = False
                break
        if (tmp_bool):
            Straight = True
    
    # 數字次數
    Times_card = [0]*len(Face_All_card)
    for i in range(5):
        for j in range(len(Face_All_card)):
            if (Face_All_card[j] == Face_List[i]):
                Times_card[j] += 1
    Times_card = sorted(Times_card, reverse = True)

    # (9) Straight flush
    if (Straight and Flush):
        return 9
    # (8) Four of a kind
    if (Times_card[0] == 4):
        return 8
    # (7) Full House
    if (Times_card[0] == 3 and Times_card[1] == 2):
        return 7
    # (6) Flush
    if (Flush):
        return 6
    # (5) Straight
    if (Straight):
        return 5
    # (4) Three of a kind
    if (Times_card[0] == 3):
        return 4
    # (3) Two pairs
    if (Times_card[0] == 2 and Times_card[1] == 2):
        return 3
    # (2) One pair
    if (Times_card[0] == 2):
        return 2
    return 1
    

# 判斷
def judge(A_card, B_card, Table_card):
    A_number, B_number = -1, -1
    
    # A
    Total_card = [A_card[0], A_card[1]]
    for i in range(len(Table_card)): 
        Total_card.append(Table_card[i])
    
    for i in range(len(Total_card)): #排除哪個不要
        A_judge_card = []
        for j in range(len(Total_card)):
            if (i != j):
                A_judge_card.append(Total_card[j])
        
        tmp_number = card_number(A_judge_card)
        # print(A_judge_card, tmp_number)
        A_number = max(A_number, tmp_number)
    
    # B
    Total_card = [B_card[0], B_card[1]]
    for i in range(len(Table_card)): 
        Total_card.append(Table_card[i])
    
    for i in range(len(Total_card)): #排除哪個不要
        B_judge_card = []
        for j in range(len(Total_card)):
            if (i != j):
                B_judge_card.append(Total_card[j])
        
        tmp_number = card_number(B_judge_card)
        # print(B_judge_card, tmp_number)
        B_number = max(B_number, tmp_number)

    # print
    if (A_number == B_number):
        print("Tie")
    elif (A_number > B_number):
        print("A %d"%(A_number))
    else:
        print("B %d"%(B_number))        


# 所有的Card
def get_total_card(A_card, B_card, Table_card):
    Total_card = [A_card[0], A_card[1], B_card[0], B_card[1]]
    for i in range(4):
        Total_card.append(Table_card[i])
    return Total_card
    
# 找Error
def check_Error_input(Total_card):
    Color_All_card = ["S","H","D","C"]
    Face_All_card = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    for i in range(len(Total_card)):
        card = Total_card[i]
        color = "."
        face = "."

        if (len(card) == 2):
            color = card[0]
            face = card[1]
        elif (len(card) == 3):
            if (card[1] == '1' and card[2] == '0'):
                face = "10"
            else:
                return True

            color = card[0]
        else:
            return True
        
        if (not(color in Color_All_card)):
            return True
        if (not(face in Face_All_card)):
            return True
    
    return False
        
# 找重複
def check_Duplicate(Card):
    for i in range(len(Card)):
        for j in range(i+1, len(Card)):
            if (Card[i] == Card[j]):
                return True
    return False

# main
def main():
    A_card = list(input().split())
    B_card = list(input().split())
    Table_card = list(input().split())

    Total_card = get_total_card(A_card, B_card, Table_card)
    
    Error = check_Error_input(Total_card)
    Duplicate = check_Duplicate(Total_card)
    if (Error):
        print("Error input")
    elif (Duplicate):
        print("Duplicate deal")
    else:  
        judge(A_card, B_card, Table_card)

main()