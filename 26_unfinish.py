import math

n = int(input()) # 城市人口
m = int(input()) # 計算時間

a = int(input()) # 第一天確診人數
b = float(input()) # 傳染人數
c = int(input()) # 康復天數
d = float(input()) # 免疫率

total_number = a # 當天總確診人數
new_number_list = [] # 新增確診人數
new_number_list.append(a)

# 天數 總確診人數 新增確診人數 康復人數
print(1, total_number, new_number_list[0], 0)


for times in range(2,m+1):
    limit_number = n * (1-d)
    new_number = 0

    # 可以傳多少人
    x = (b/c) * (1-d)
    x *= total_number
    new_number = math.floor(x)

    # 是否超過limit
    if (total_number+new_number >= limit_number):
        if (total_number <= limit_number):
            new_number = limit_number-total_number

    new_number = int(round(new_number, 0))
    total_number += new_number
    new_number_list.append(new_number)

    recovery = 0
    if (times > c): #有康復的人了
        recovery = new_number_list[times-c-1]
        total_number -= recovery
    d += (recovery/n)

    # 天數 總確診人數 新增確診人數 康復人數
    print(times, total_number, new_number, recovery)

print(sum(new_number_list))

