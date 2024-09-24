def Round_BMI(BMI):
    # 四捨六入伍看偶數
    BMI *= 1000
    if (BMI%10 == 5):
        if(((BMI%100)-5)%2 == 1):
            BMI += 10
        else:
            BMI -= 10
    elif (BMI%10 > 5):
        BMI += 10
    else:
        BMI -= 10
    BMI //= 10
    BMI /= 100

    return BMI

def ans_print(List):
    # sort
    List = sorted(List) 

    MAX = List[-1]
    MIN = List[0]
    Median = 0

    n = len(List)

    if (n%2 == 1):
        Median = List[n/2]
    else:
        # print(n/2)
        Median = (List[int(n/2)] + List[int(n/2)-1])/2
        print(Median)
        Median = Round_BMI(Median)

    # dic = {}
    # for i in range(len(List)):
    #     dic[List[i]] += 1
    # print(dic)


    print(MAX)
    print(MIN)
    print(Median)

    # for i in range(n):
    #     print(List[i])


def get_BMI():
    meter, kg = map(float, input().split(" "))

    BMI = kg / (meter*meter)
    BMI = Round_BMI(BMI)

    return BMI

def main():
    n = int(input())
    List = []

    # input
    for i in range(n):
        BMI = get_BMI()
        List.append(BMI)

    ans_print(List)

main()
