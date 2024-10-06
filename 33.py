import math

Drone_name = []
Drone_XYZ = []
Distance_List = []

def input_data():
    name, x, y, z = map(int, input().split())
    Drone_name.append(name)
    Drone_XYZ.append([x,y,z])

def find_distance(List1, List2):
    Distance = 0
    for i in range(3):
        Distance += (List1[i]-List2[i])**2
    Distance = math.sqrt(Distance)
    return Distance

def print_answer(Sort_distance_list, Drone_name, Drone_XYZ):
    times = 0
    while (times <= 2):
        for i in range(len(Drone_name)):
            for j in range(i+1, len(Drone_name)):
                if (Sort_distance_list[times] == find_distance(Drone_XYZ[i], Drone_XYZ[j])):
                    # print(find_distance(Drone_XYZ[i], Drone_XYZ[j]))
                    print(Drone_name[i], Drone_name[j], Drone_XYZ[i][0], Drone_XYZ[i][1], Drone_XYZ[i][2], Drone_XYZ[j][0], Drone_XYZ[j][1], Drone_XYZ[j][2])
                    times += 1
                if (times >= 3):
                    return 0

def main():
    N = int(input())
    for i in range(N):
        input_data()
    
    # find distance
    for i in range(N):
        for j in range(i+1, N):
            Distance = find_distance(Drone_XYZ[i], Drone_XYZ[j])
            Distance_List.append(Distance)

    # sort
    Sort_distance_list = sorted(Distance_List)



    print_answer(Sort_distance_list, Drone_name, Drone_XYZ)

main()

# 【隱藏測試資料二】bug? 第三長的有兩個 有點尷尬
    # for i in range(4):
    #     print(Sort_distance_list[i])
# print(find_distance(Drone_XYZ[1], Drone_XYZ[2]))
# print(find_distance(Drone_XYZ[4], Drone_XYZ[12]))