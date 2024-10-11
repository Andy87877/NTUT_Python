inning = [[],[],[],[],[],[],[],[],[],[],[]] # 10局 + bonus
bonus = False
def get_inning(time):
    index = time
    Li = []

    score = int(input())
    Li.append(score)
    if (score != 10):
        score = int(input())
        Li.append(score)
    
    inning[index] = Li

def get_score(time):
    if (sum(inning[time]) != 10):
        return sum(inning[time])
    
    score = sum(inning[time])
    if (inning[time][0] == 10):
        score += sum(inning[time+1])
    else:
        score += (inning[time+1][0])

    return score

def main():
    for i in range(10):
        get_inning(i)

    # bonus
    if (sum(inning[9]) == 10):
        get_inning(10)
        bonus = True

    total_score = 0
    for i in range(10):
        total_score += get_score(i)
    print(total_score)

main()