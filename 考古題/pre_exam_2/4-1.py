def check_error(front_DNA, all_DNA):
    if front_DNA[:3] != all_DNA[:3]:
        print(all_DNA[:3])
        return True

    count_number = 0
    for i in "ATCG":
        count_number += all_DNA.count(i)
    print(len(all_DNA))

    if count_number != len(all_DNA):
        return True
    return False


def do_split_DNA(all_DNA_list, split_DNA):
    tmp_list = []
    for Dna in all_DNA_list:
        Dna_list = Dna.split(split_DNA)
        tmp_list.extend(Dna_list)

    answer_list = []
    for Dna in tmp_list:
        if len(Dna) >= 3:
            answer_list.append(Dna)

    return answer_list


def main():
    front_DNA = input()
    front_DNA = front_DNA[:3]
    back_DNA_list = input().split()

    all_DNA = input()[:-1]
    Error = check_error(front_DNA, all_DNA)

    if Error:
        print("Input error")
        exit()

    all_DNA_list = [all_DNA]
    all_DNA_list = do_split_DNA(all_DNA_list, front_DNA)
    for i in range(3):
        all_DNA_list = do_split_DNA(all_DNA_list, back_DNA_list[i][:3])

    print(all_DNA_list)


main()
