'''
-20 ~ 0, 0 ~ 20
0 ~ 21, 21 ~ 42

0:no 1: yes
'''
arr = []

for i in range(0,43):
    arr.append(0)

for t in range(3):
    a = int(input())
    b = int(input())
    
    for i in range(a+20, b+20):
        arr[i] = 1

ans = 0
for i in range(0,43):
    if (arr[i] == 1):
        ans += 1

print(ans)