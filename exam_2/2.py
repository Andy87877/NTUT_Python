def main():
    N = int(input())

    class_data = []

    for _ in range(N):
        input_data = input().split()

        name = input_data[0]
        score_data = list(map(int, input_data[1:]))

        avg_score = int(sum(score_data) // len(score_data))

        class_data.append([name, avg_score])

    def is_ok(data):
        return data[1] >= 60

    ok_class_data = list(filter(is_ok, class_data))

    sort_class_data = sorted(ok_class_data, key=lambda x: x[1])

    for name, avg_score in sort_class_data:
        print(name, avg_score)


main()
