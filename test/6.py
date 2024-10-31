import math

a = int(input())
b = int(input())
c = int(input())

T = b * b - 4 * a * c

if T >= 0:
    T = math.sqrt(T)
    x1 = (-b + T) / (2 * a)
    x2 = (-b - T) / (2 * a)
    print("%.1f" % (x1))
    print("%.1f" % (x2))
else:
    x11 = (-b) / (2 * a)
    x21 = x11

    x12 = (math.sqrt(-1 * T)) / (2 * a)
    x22 = x12

    print("%.1f+%.1fi" % (x11, x12))
    print("%.1f-%.1fi" % (x21, x22))
