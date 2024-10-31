# -20 ~ 20 --> 0~41
arr = [False] * 50

for _ in range(3):
    x1 = int(input())
    x2 = int(input())
    x1 += 20
    x2 += 20

    for i in range(x1, x2):
        arr[i] = True

ans = 0
for i in range(50):
    if arr[i]:
        ans += 1
print(ans)
