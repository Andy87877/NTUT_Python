List_keyboard = []
# player_score = 0
# computer_score = 0
# player_card = []
# computer_card = []

def card_to_score(card):
    if (card == 'A'):
        score = 1
    elif (card == 'J' or card == 'K' or card == 'Q'):
        score = 0.5
    elif (card == '10'):
        score = 10
    else:
        score = ord(card)-ord('0')
    return score
    
def judge(index, player_score, computer_score):
    player_continue = List_keyboard[index]
    index += 1
    if (player_continue == "Y"):
        card = List_keyboard[index]
        index += 1
        player_score += card_to_score(card)
    
    if ((player_score > computer_score) or (computer_score <= 8)):
        card = List_keyboard[index]
        index += 1
        computer_score += card_to_score(card)


    return index, player_score, computer_score
 
def print_ans(player_score, computer_score):
    if (player_score > 10.5):
        player_score = 0
    if (computer_score > 10.5):
        computer_score = 0

    if (computer_score == player_score):
        print("it's a tie")
    elif (computer_score > player_score):
        print("computer win")
    else:
        print("player win")

def main():
    RUN = True
    while(RUN):
        try:
            tmpchar = input()
        except EOFError:
            RUN = False
            break
        finally:
            List_keyboard.append(tmpchar)

    card = List_keyboard[0]
    player_score = card_to_score(card)
    card = List_keyboard[1]
    computer_score = card_to_score(card)

    index = 2
    while(index != len(List_keyboard)):
        index, player_score, computer_score  = judge(index, player_score, computer_score)
    
    print_ans(player_score, computer_score)

main()