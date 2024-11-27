tribe_map = (
    {}
)  # 字典 (部落連接) {"部落1":["部落2","部落3",.......], "部落2":["部落1","部落3",.......]........}


# 輸入部落連接的方式 (像是地圖的路徑)
def input_tribe_map():
    tribeA, tribeB = map(int, input().split())
    if tribeA not in tribe_map:
        tribe_map[tribeA] = [tribeB]
    else:
        tribe_map[tribeA].append(tribeB)

    if tribeB not in tribe_map:
        tribe_map[tribeB] = [tribeA]
    else:
        tribe_map[tribeB].append(tribeA)


# 走路線 (用BFS)
def walk_round(From_tribe, To_tribe):
    now_route = [From_tribe]  # 現在的路線
    shortest_route = [0] * 999  # 最短的路線

    later_tribe = [From_tribe]  # 等一下要走的部落
    later_route = [[From_tribe]]  # 等一下要走的部落 之前的路線

    while len(later_tribe) != 0:
        now_tribe = later_tribe[0]
        now_route = later_route[0]

        # print(now_tribe, now_route, shortest_route)

        later_tribe.pop(0)
        later_route.pop(0)

        # 接下來的部落剛好是目的地
        if To_tribe in tribe_map[now_tribe]:
            now_route.append(To_tribe)
            if len(now_route) < len(shortest_route):
                shortest_route = now_route
            continue

        # 找接下來要走的部落
        for tmp_tribe in tribe_map[now_tribe]:
            # 如果之前路線沒有走過
            if not tmp_tribe in now_route:
                later_tribe.append(tmp_tribe)
                later_route.append(now_route + [tmp_tribe])

    return shortest_route


def main():
    # 路徑個數N，起點部落X和終點部落Z
    N, start_tribe, end_tribe = map(int, input().split())

    # 休息點的部落
    rest_tribe = map(int, input().split())

    # 輸入部落連接的方式
    for i in range(N):
        input_tribe_map()

    # 走每個休息部落 找到最短的路徑
    route_length_min = N * 100
    find_rest_tribe = -1
    answer_route = []

    for tribe in rest_tribe:
        route_len = 0

        route_Start_to_Rest = walk_round(start_tribe, tribe)
        route_len += len(route_Start_to_Rest)

        route_Rest_to_End = walk_round(tribe, end_tribe)
        route_Rest_to_End.pop(0)
        route_len += len(route_Rest_to_End)

        if route_len < route_length_min:
            find_rest_tribe = tribe
            route_length_min = route_len

            answer_route = []
            for i in route_Start_to_Rest:
                answer_route.append(i)
            for i in route_Rest_to_End:
                answer_route.append(i)

    if len(answer_route) != 0:
        print(find_rest_tribe)
        for tribe in answer_route:
            print(tribe, end=" ")
    else:
        print("NO")


main()
