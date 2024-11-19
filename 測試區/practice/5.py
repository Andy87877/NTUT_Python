Length_List = [0] * 3


def getTriangle(a, b, c):
    if a >= b + c:
        return "not a triangle"
    if a == b and b == c and a == c:
        return "equilateral triangle"
    if a == b or b == c or a == c:
        return "isosceles triangle"
    if a * a > b * b + c * c:
        return "obtuse triangle"
    if a * a < b * b + c * c:
        return "acute triangle"
    if a * a == b * b + c * c:
        return "right triangle"

    return "bruh"


Length_List[0] = int(input())
Length_List[1] = int(input())
Length_List[2] = int(input())
Length_List = sorted(Length_List, reverse=True)

ans = getTriangle(Length_List[0], Length_List[1], Length_List[2])

print(ans)
