def input_array(N):
    data = list(map(int, input().split()))
    now_array = []

    for i in range(N):
        tmp_array = []
        for j in range(N):
            tmp_array.append(data[i * N + j])
        now_array.append(tmp_array)
    
    return now_array


def main():
    N, M = list(map(int, input().split()))

    A_number_array = input_array(N)
    B_number_array = input_array(N)


main()
