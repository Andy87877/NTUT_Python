def strOps():
    words = "小明今天去學校，小明遲到。"
    wordLength = len(words)
    print(wordLength)
    sentence = words.replace("小明","湯姆")
    print(words)
    print(sentence)
    wordsSplit = words.split("明")
    print(wordsSplit)

strOps()