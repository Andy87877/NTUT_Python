def judge(D, input_str):
    Fail = False # 是否失敗了

    now_D = 0 # 現在的深度
    List_parentheses = [] # 括弧
    ans_str = "" # 該深度的答案

    for i in range(len(input_str)):
        now_char = input_str[i]
        if (now_char == "{" or now_char == "[" or now_char == "("):
            # 增加深度
            List_parentheses.append(now_char)
            now_D += 1
        elif (now_char == "}" or now_char == "]" or now_char == ")"):
            # 減少深度
            if (len(List_parentheses) == 0):
                Fail = True
                break

            Last_pare = List_parentheses[-1]
            if ((now_char == "}" and Last_pare == "{") or (now_char == "]" and Last_pare == "[") or (now_char == ")" and Last_pare == "(")):
                List_parentheses.pop()
                now_D -= 1
            else:
                Fail = True
                break
        else:
            if (now_D == D):
                ans_str += now_char
    
    if (Fail or (len(List_parentheses) != 0)):
        print("fail")
    else:
        print("pass, ", end = "")
        if (ans_str == ""):
            print("EMPTY")
        else:
            print(ans_str)

def main():
    N = int(input())
    D = int(input())
    for times in range(N):
        input_str = input()
        judge(D, input_str)
main()