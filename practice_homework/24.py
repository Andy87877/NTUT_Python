def card_to_score(card):
    if (card == 'J' or card == 'Q' or card == 'K'):
        return 0.5
    if (card == 'A'):
        return 1
    if (card == '10'):
        return 10

    scroe = ord(card) - ord('0')
    return scroe

def get_player_data(score):
    while (True):
        tmp_data = list(input().split())

        # N
        if (len(tmp_data) == 1):
            return score
        
        card = tmp_data[1]
        score += card_to_score(card)

        if (score > 10.5):
            return 0
        if (score == 10.5):
            return 10.5

def get_bot_data(score, min_score, no_min):
    if (no_min == True):
        return score
    while (score <= min_score):
        card = input()
        score += card_to_score(card)

        if (score > 10.5):
            return 0
        if (score == 10.5):
            return 10.5

        if (score > min_score):
            return score
    return score

def print_ans(Bet_money, Bot_score, player_score_list):
    Bot_total_money = 0

    for i in range(len(player_score_list)):
        print("Player%d" %(i+1), end = " ")
        # print (player_score_list[i], end = " ")
        if (Bot_score == 0 or player_score_list[i] > Bot_score or player_score_list[i] == 10.5):
            print("+%d" %(Bet_money[i]))
            Bot_total_money -= Bet_money[i]
        else:
            print("-%d" %(Bet_money[i]))
            Bot_total_money += Bet_money[i]

    # print(Bot_score)
    if (Bot_total_money >= 0):
        print("Computer +%d" %(Bot_total_money))
    else:
        print("Computer %d" %(Bot_total_money))

def main():
    N = int(input())
    Bet_money = list(map(int, input().split()))
    
    first_card = list(input().split())

    Score_player = [0]*N
    Score_bot = card_to_score(first_card[0])

    for i in range(1, N+1):
        Score_player[i-1] = card_to_score(first_card[i])

    min_score = 10.5
    no_min = True
    for i in range(N):
        Score_player[i] = get_player_data(Score_player[i])
        if (min_score > Score_player[i] and Score_player[i] != 0):
            min_score = Score_player[i]
            no_min = False

    Score_bot = get_bot_data(Score_bot, min_score, no_min)
    
    print_ans(Bet_money, Score_bot, Score_player)

main()