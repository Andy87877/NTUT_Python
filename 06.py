import math

a = int(input())
b = int(input())
c = int(input())

tmp = b*b - 4*a*c

if (tmp >= 0):
    T = math.sqrt(b*b - 4*a*c)
    x1 = (-b+T)/(2*a)
    x2 = (-b-T)/(2*a)
    print("%.1f" %(x1))
    print("%.1f" %(x2))
else:
    x11 = -b/(2*a)
    x12 = math.sqrt(-tmp) / (2*a)

    x21 = x11
    x22 = x12

    print("%.1f+%.1fi" %(x11,x12))
    print("%.1f-%.1fi" %(x21,x22))