def binary_to_decimal(str_binary):
    num_decimal = 0
    tmp = 1
    for i in range(len(str_binary)-1, -1, -1):
        if (str_binary[i] == '1'):
            num_decimal += tmp
        tmp *= 2
    return num_decimal

def decimal_to_binary(number):
    list_binary = ["0"]*14
    index = 13
    while (number > 0):
        if (number%2 == 1):
            list_binary[index] = "1"
        number //= 2
        index -= 1

    binary_ans = ""
    for i in range(14):
        binary_ans += list_binary[i]
    return binary_ans

def R_number(now_number):
    ans_number = 0

    while (now_number >= 2):
        ans_number += 1
        if (now_number%2 == 0):
            now_number /= 2
        else:
            now_number = (now_number+1)/2
    
    return ans_number

def judge_ans(T_number):
    T_number = binary_to_decimal(T_number)
    ans_number = 0

    for i in range(T_number+1):
        ans_number += R_number(i)

    binary_ans = decimal_to_binary(ans_number)

    print(binary_ans)

def main():
    Judge_List = []

    tmp_data = "0"
    while (tmp_data != "-1"):
        tmp_data = input()
        if (tmp_data != "-1"):
            Judge_List.append(tmp_data)
    
    for i in range(len(Judge_List)):
        judge_ans(Judge_List[i])

main()