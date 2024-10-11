'''
-20 ~ 0, 0 ~ 20
0 ~ 21, 21 ~ 42

0:no 1: yes
'''
arr = []

for i in range(0,43):
    arr.append(0)

n = int(input())

for t in range(n):
    a, b = map(int, input().split(" "))
    
    for i in range(a+20, b+20):
        arr[i] = 1

ans = 0
for i in range(0,43):
    if (arr[i] == 1):
        ans += 1

print(ans)