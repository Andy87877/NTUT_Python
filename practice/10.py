List = []

a1 = a2 = b1 = b2 = c1 = c2 = 0

a1 = int(input())
List.append(a1)
if (a1 != 10):
    a2 = int(input())
    List.append(a2)

b1 = int(input())
List.append(b1)
if (b1 != 10):
    b2 = int(input())
    List.append(b2)

if (b1+b2 == 10):
    c1 = int(input())
    List.append(c1)
if (b1 == 10):
    c2 = int(input())
    List.append(c2)


ans = 0
# judge
if (a1 == 10):
    ans += 10+List[1]+List[2]
elif (a1+a2 == 10):
    ans += b1+10
else:
    ans += a1+a2

if (b1 == 10):
    ans += c1+c2+10
elif (b1+b2 == 10):
    ans += c1+10
else:
    ans += b1+b2

print(ans)