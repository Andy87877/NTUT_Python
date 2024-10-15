import math

def get_Triangle(list_len):
    list_len = sorted(list_len)
    a, b, c = list_len[0], list_len[1], list_len[2]

    if (a+b <= c):
        print("not a triangle")
        return -1
    
    # get Area 
    s = (a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    Area = round(Area, 2)
    
    if (a == b and a == c and b == c):
        print("equilateral triangle %.2f" %(Area))
    elif ( ((a == b) and ((a**2 + b**2) > c**2 )) or ((b == c) and ((b**2 + c**2) > a**2 )) ):
        print("isosceles triangle %.2f" %(Area))
    elif (a*a + b*b < c*c):
        print("obtuse triangle %.2f" %(Area))
    elif (a*a + b*b > c*c):
        print("acute triangle %.2f" %(Area))
    elif (a*a+b*b == c*c):
        print("right triangle %.2f" %(Area))
    else:
        print("not a triangle")

    return Area



def main():
    n = int(input())

    List = []

    input_list = []

    for i in range(n):
        list_len = [0,0,0]
        list_len[0], list_len[1], list_len[2] = map(int, input().split(" "))
        input_list.append(list_len)

    for i in range(n):
        Area = get_Triangle(input_list[i])
        if (Area != -1):
            List.append(Area)

    if (len(List) == 0):
        print("All inputs are not triangles!")
    else:
        List = sorted(List)
        print(f"{List[-1]:.2f}")
        print(f"{List[0]:.2f}")

main()