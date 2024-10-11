def binary_to_decimal(str_number):
    number = 0
    tmp = 1
    for i in range(7,-1,-1):
        if (str_number[i] == '1'):
            number += tmp
        tmp *= 2
    return number

def decimal_to_binary(number):
    Binary_answer_list = ["0","0","0","0"]

    index = 3
    while (number != 0):
        if ((number%2) == 1):
            Binary_answer_list[index] = "1"
        number //= 2
        index -= 1
    
    Binary_answer = ""
    for i in range(4):
        Binary_answer += Binary_answer_list[i]

    return Binary_answer

# 計算答案
def Get_ans(str_number):
    answer = 0
    number = binary_to_decimal(str_number)

    while (number > 1):
        answer += 1
        if (number%2 == 0):
            number /= 2
        else:
            number = (number+1)/2

    # print(answer)
    Binary_answer = decimal_to_binary(answer)

    return Binary_answer


def main():
    Continue_data = 0
    List = []
    while (Continue_data != "-1"):
        tmp_data = input()
        List.append(tmp_data)
        Continue_data = input()

    for i in range(len(List)):
        answer = Get_ans(List[i])
        print(answer)

main()