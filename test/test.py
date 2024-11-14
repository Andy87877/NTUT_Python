import math


def judge_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1, 1):
        if num % i == 0:
            return False
    return True


for i in range(2, 20):
    print(i, judge_prime(i))
