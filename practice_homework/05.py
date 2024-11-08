def getTriangle(a,b,c):
    Lis = [a,b,c]
    Lis.sort()
    a = Lis[0]
    b = Lis[1]
    c = Lis[2]

    if (a+b <= c):
        print("not a triangle")
    elif (a == b and b == c and a == c):
        print("equilateral triangle")
    elif (a == b or b == c or a == c):
        print("isosceles triangle")
    elif (a*a + b*b < c*c):
        print("obtuse triangle")
    elif (a*a + b*b > c*c):
        print("acute triangle")
    else:
        print("right triangle")

a = int(input())
b = int(input())
c = int(input())

getTriangle(a,b,c)