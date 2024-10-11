
# 字串長度
def check_sentences_length(Sentences):
    List = list(Sentences.split(" "))
    length = 0

    for i in range(len(List)):
        length += len(List[i])

    return length

# 替換文字
def Sentences_replace(Sentences, X_word, Y_word):
    List = list(Sentences.split(" "))
    Ans_sentences = ""

    for i in range(len(List)-1):
        if ((List[i].upper()) == (X_word.upper())):
            List[i] = Y_word
        Ans_sentences += List[i]
        Ans_sentences += " "

    if ((List[-1].upper()) == (X_word.upper())):
        List[-1] = Y_word
    Ans_sentences += List[-1]

    return Ans_sentences

# 反轉文字
def Word_reverse(Word):
    ans_word = ""
    for i in range(len(Word)-1, -1, -1):
        ans_word += Word[i]
    return ans_word

# 隔著輸出
def Diff_print(Diff, Sentences):
    Sentences_ans = ""
    for i in range(0, len(Sentences), Diff):
        Sentences_ans += Sentences[i]
    return Sentences_ans

def main():
    A_sentences = input()
    B_sentences = input()

    X_word = input()
    Y_word = input()

    C_sentences = A_sentences + " " + B_sentences
    D_sentences = Sentences_replace(C_sentences, X_word, Y_word)

    C_length = check_sentences_length(C_sentences)
    D_length = check_sentences_length(D_sentences)

    Y2_word = Word_reverse(Y_word)
    D2_sentences = Sentences_replace(C_sentences, X_word, Y2_word)

    Diff = abs(len(X_word) - len(Y_word))
    final_sentences = Diff_print(Diff, C_sentences)

    # print
    print(C_sentences)
    print(D_sentences)
    print(C_length, D_length)
    print(D2_sentences)
    print(final_sentences)

main()