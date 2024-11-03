global_Face_list = []
global_Suit_list = []

Face_OK_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
Suit_OK_list = ["S", "H", "D", "C"]


def input_error(card_list):
    if len(card_list) != 10:
        return True

    for i in range(len(card_list)):
        now_card = card_list[i]

        if not (2 <= len(now_card) <= 3):
            return True

        Face = "0"
        Suit = "."
        if len(now_card) == 3:
            if not (now_card[0] == "1" and now_card[1] == "0"):
                return True
            Face = "10"

            if now_card[2] not in Suit_OK_list:
                return True
            Suit = now_card[2]
        else:

            if now_card[0] not in Face_OK_list:
                return True
            Face = now_card[0]

            if now_card[1] not in Suit_OK_list:
                return True
            Suit = now_card[1]

        global_Face_list.append(Face)
        global_Suit_list.append(Suit)

    return False


def judge_number(card_list, Face_list, Suit_list):
    # Flush
    Flush = False
    if Suit_list.count(Suit_list[0]) == 5:
        Flush = True

    # Straight & Face_number
    Face_number = [0] * 13
    for i in range(len(Face_list)):
        for j in range(13):
            if Face_list[i] == Face_OK_list[j]:
                Face_number[j] += 1

    # print(Face_number)
    Straight = False
    flag = False
    times = 0
    for i in range(-7, 13):
        if Face_number[i] == 1:
            flag = True
            times += 1
            if times == 5:
                Straight = True
                break
        else:
            if flag:
                break

    Face_number = sorted(Face_number, reverse=True)

    if Straight and Flush:
        return 9
    if Face_number[0] == 4:
        return 8
    if Face_number[0] == 3 and Face_number[1] == 2:
        return 7
    if Flush:
        return 6
    if Straight:
        return 5
    if Face_number[0] == 3:
        return 4
    if Face_number[0] == 2 and Face_number[1] == 2:
        return 3
    if Face_number[0] == 2:
        return 2
    return 1


def check_duplicate(card_list):
    card_set = set(card_list)
    if len(card_set) != 10:
        return True
    return False


def main():
    card1_list = input().split()
    card2_list = input().split()

    all_card_list = card1_list + card2_list

    Error_input = input_error(all_card_list)
    if Error_input:
        print("Error input")
        exit()

    Duplicate = check_duplicate(all_card_list)
    if Duplicate:
        print("Duplicate deal")
        exit()

    Face1_list = global_Face_list[:5]
    Suit1_list = global_Suit_list[:5]
    number1 = judge_number(card1_list, Face1_list, Suit1_list)

    Face2_list = global_Face_list[5:]
    Suit2_list = global_Suit_list[5:]
    number2 = judge_number(card2_list, Face2_list, Suit2_list)

    ans_number = max(number1, number2)
    print(ans_number)


main()
