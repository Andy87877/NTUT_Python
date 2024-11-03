def card_to_score(card):
    if card == "J" or card == "Q" or card == "K":
        return 0.5
    if card == "A":
        return 1

    return int(card)


def main():
    N = int(input())
    money_list = input().split()

    first_card = input().split()
    bot_card = first_card[0]
    first_card = first_card[1:]

    player_score_list = []
    player_card_num_list = []
    min_score = 10.5
    for i in range(N):
        score = card_to_score(first_card[i])
        card_num = 1

        while True:
            command = input().split()
            if command[0] == "N":
                break
            score += card_to_score(command[1])
            card_num += 1

            if score == 10.5:
                break
            if score > 10.5:
                score = -1
                break
            if card_num == 5:
                break

        if score != -1 and card_num != 5:
            min_score = min(min_score, score)
        player_score_list.append(score)
        player_card_num_list.append(card_num)

    print(player_card_num_list)
    print(player_score_list)

    # bot
    bot_score = card_to_score(bot_card)
    while True:
        if bot_score >= min_score:
            break

        command = input()
        bot_score += card_to_score(command)

        if bot_score > 10.5:
            bot_score = 0
            break

    for i in range(N):
        Win_player = True

        if player_score_list[i] == -1:
            Win_player = False
        elif bot_score == 0:
            Win_player = True
        elif player_score_list[i] == 10.5:
            Win_player = True
        elif player_card_num_list[i] == 5:
            Win_player = True
        elif bot_score >= player_score_list[i]:
            Win_player = False
        else:
            Win_player = True

        print("Player%d " % (i + 1), end="")
        if Win_player:
            print("+%s" % (money_list[i]))
        else:
            print("-%s" % (money_list[i]))


main()
