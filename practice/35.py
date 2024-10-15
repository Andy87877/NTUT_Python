School_name = []
School_type = {}

# 輸入資料
def input_data():
    tmp_list = list(input().split())
    name = tmp_list[0]
    List_type = tmp_list[1:]

    School_name.append(name)
    School_type[name] = List_type

# 完全符合
def b0_full_condition(str_condition):
    Condition = list(str_condition.split())
    ans_school = []

    # check all school
    for i in range(len(School_name)):
        name = School_name[i]
        OK = False
        Flag = True
        for j in range(len(Condition)):
            if (Condition[j] == "+"):
                if (Flag):
                    OK = True
                    break
                Flag = True
            elif(not(Condition[j] in School_type[name])):
                Flag = False
        
        if (Flag):
            OK = True

        if (OK):
            ans_school.append(name)
    
    # print
    for i in range(len(ans_school)-1):
        print(ans_school[i], end = " ")     
    print(ans_school[-1])   


# 部分符合
def b1_some_condition(str_condition):
    Condition = list(str_condition.split())

    ans_school = []
    max_match_count = -1

    # check all school
    for i in range(len(School_name)):
        name = School_name[i]
        tmp_match_count = 0

        for j in range(len(Condition)):
            if (Condition[j] in School_type[name]):
                tmp_match_count += 1

        # print(tmp_match_count)

        if (max_match_count < tmp_match_count):
            max_match_count = tmp_match_count
            ans_school = []
            ans_school.append(name)
        elif (max_match_count == tmp_match_count):
            ans_school.append(name)

    # print
    for i in range(len(ans_school)-1):
        print(ans_school[i], end = " ")     
    print(ans_school[-1])   



def judge_and_print():
    # input question
    M = int(input())
    tmp_list = []
    for i in range(M):
        tmp_str = input()
        tmp_list.append(tmp_str)
    
    b = int(input())

    if (b == 0):
        for i in range(len(tmp_list)):
            b0_full_condition(tmp_list[i])
    else:
        for i in range(len(tmp_list)):
            b1_some_condition(tmp_list[i])   

def main():
    N = int(input())
    for i in range(N):
        input_data()

    judge_and_print()

main()