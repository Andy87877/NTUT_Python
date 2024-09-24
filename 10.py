ans = 0

List = []

# input
a1 = int(input())
List.append(a1)
a2 = 0
if (a1 != 10):
    a2 = int(input())
    List.append(a2)

b1 = int(input())
List.append(b1)
b2 = 0
if (b1 != 10):
    b2 = int(input())
    List.append(b2)

c1 = 0
c2 = 0
if (b1+b2 == 10):
    c1 = int(input())
    List.append(c1)
if (b1 == 10):
    c2 = int(input())
    List.append(c2)

# sum
for i in range(len(List)):
    ans += List[i]

# add
if (a1 == 10):
    ans += List[1]+List[2]
elif (a1+a2 == 10):
    ans += List[2]

if (b1 == 10):
    ans += c1+c2
elif (b1+b2 == 10):
    ans += c1

print(ans)