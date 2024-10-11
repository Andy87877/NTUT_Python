def gray_code(n, k):
    ans_code = ""

    while (n != 1):
        # print (n, k, ans_code)
        if (k < pow(2, n-1)):
            ans_code += "0"
        else:
            ans_code += "1"
            k = (pow(2, n) - k - 1)
        n -= 1
    
    if (k == 0):
        ans_code += "0"
    else:
        ans_code += "1"

    print(ans_code)

def main():
    List_data = []
    while (True):
        input_data = list(map(int, input().split()))
        if (len(input_data) == 1):
            break
        List_data.append(input_data)

    for i in range(len(List_data)):
        n, k = List_data[i][0], List_data[i][1]
        gray_code(n, k)

main()