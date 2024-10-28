def Round_BMI(BMI):
    # 四捨六入五看偶數
    BMI *= 1000
    if (BMI%10 == 5):
        tmp = (BMI%100 - 5)/10
        if (tmp%2 == 1):
            BMI += 5
        else:
            BMI -= 5
    BMI /= 1000

    BMI = round(BMI, 2)
    return BMI

def ans_print(List):
    # sort
    List = sorted(List) 
    MAX = (List[-1])
    MIN = (List[0])
    Median = 0
    n = len(List)
    if (n%2 == 1):
        Median = List[n//2]
    else:
        Median = (List[int(n/2)] + List[int(n/2)-1])/2
        Median = int((Median)*100)
        Median /= 100
    count_mx = 0
    most_count_num = 0
    for i in range(n):
        if (count_mx < List.count(List[i])):
            count_mx = List.count(List[i])
            most_count_num = List[i]
 
    print("%.2f"%(MAX))
    print("%.2f"%(MIN))
    print("%.2f"%(Median))
    print("%.2f"%(most_count_num))

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
