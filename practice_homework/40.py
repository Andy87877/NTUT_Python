import math


def Check_find_gene(first_gene, back_gene_list, full_gene):
    if len(full_gene) < len(first_gene):
        return False

    N = len(first_gene)
    if full_gene[:N] != first_gene:
        return False

    N = len(full_gene)
    for back_gene in back_gene_list:
        M = len(back_gene)
        if full_gene[N - M :] == back_gene:
            return True

        if len(full_gene) < len(back_gene):
            return False

    return False


def Split_gene(first_gene, back_gene_list, full_gene):
    full_gene = full_gene[len(first_gene) :]
    back_gene_list.insert(0, (first_gene))

    tmp_gene_list = list()
    tmp_gene_list.append(full_gene)

    for i in range(4):
        gene_list = []
        for gene in tmp_gene_list:
            gene_list.extend(gene.split(back_gene_list[i]))
        tmp_gene_list = gene_list

    return gene_list


def judge_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def Let_gene_short(gene):
    gene_short = ""
    for i in range(1, len(gene)):
        gene_short += gene[i]
    return gene_short


def Get_gene(check_gene_list):
    answer_gene_list = []
    for gene in check_gene_list:
        now_gene = gene
        if len(gene) <= 1:
            continue

        while True:
            N = len(now_gene)
            if N <= 2:
                break
            if judge_prime(N):
                answer_gene_list.append(now_gene)
                break

            now_gene = Let_gene_short(now_gene)

    return answer_gene_list


def Sort_gene_list(gene_list):
    # 字典序排序
    gene_list = sorted(gene_list)

    # 長度排序
    for i in range(len(gene_list)):
        for j in range(i + 1, len(gene_list)):
            if len(gene_list[i]) > len(gene_list[j]):
                gene_list[i], gene_list[j] = gene_list[j], gene_list[i]

    return gene_list


def print_answer(gene_list):
    for gene in gene_list:
        print(gene)


def main():
    first_gene = input()
    back_gene_list = input().split()
    full_gene = input()

    # 檢查該基因是否存在
    find_gene = Check_find_gene(first_gene, back_gene_list, full_gene)
    if not find_gene:
        print("No gene")
        exit()

    # 把基因分割
    check_gene_list = Split_gene(first_gene, back_gene_list, full_gene)

    check_gene_list = Sort_gene_list(check_gene_list)

    # 得到正確的基因
    gene_list = Get_gene(check_gene_list)

    # 基因排序
    gene_list = Sort_gene_list(gene_list)

    # 輸出答案
    print_answer(gene_list)


main()
