# permutation(排列)稱為 "arrangement number"


def f(data):
    if len(data) <= 1:
        return [data]
    r = []
    for i in range(len(data)):
        x = data[i]
        y = data[:i] + data[i + 1 :]
        z = f(y)  # 用一個變數存結果
        for sub in z:
            r = r + [x + sub]  # 排列個數不只一個，要加總
    return r


List = f("ABC")
for i in List:
    print(i)
print(f("ABC"))
