def tr(index):
    table = [chr(w) for w in range(ord("A"), ord("Z") + 1)]
    if int(index) > 26:
        return "-1"
    return table[int(index) - 1]


def check(x, data):
    print(data)
    if len(x) == 0:
        return True
    if len(x) == 1:
        data[x] = tr(x)
        return True
    if len(x) >= 2:
        if tr(x[0:2]) != "-1":
            data[x[0:2]] = tr(x[0:2])
            check(x[2:], data)
        check(x[:1], data)
        check(x[1:], data)
    return True


data = {}
check("12344321", data)
print(data)
