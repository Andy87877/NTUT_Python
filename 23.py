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
    
def judge(player_score, computer_score):
    player_continue = True

    while ((player_continue or (player_score > computer_score) or (computer_score <= 8)) and (player_score <= 10.5) and (computer_score <= 10.5)):
        # print(player_score, computer_score, "\n")

        if (player_continue):
            player_continue_char = input()
        if (player_continue_char == "Y" and player_continue):
            card = input()
            player_score += card_to_score(card)
        else:
            player_continue = False

        
        if (((player_score > computer_score) or (computer_score <= 8)) and (player_score <= 10.5)):
            card = input()
            computer_score += card_to_score(card)


    return player_score, computer_score
 
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
    card = input()
    player_score = card_to_score(card)
    card = input()
    computer_score = card_to_score(card)


    player_score, computer_score = judge(player_score, computer_score)
    
    print_ans(player_score, computer_score)

main()