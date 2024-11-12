def FindPath(dict, startNode, endNode, middleNode):
    queue = [[startNode]]          # 初始化queue，包含起始node的路徑
    visited = []                   # 初始化已訪問node列表
    FindMiddle = False             # 標記是否已找到中間node

    while queue:
        path = queue.pop()         # 從queue中取出最後一條路徑
        node = path[-1]            # 取得當前路徑的最後一個node
        if node not in visited:
            for neighbor in dict[node]:    # 遍歷當前node的所有鄰居
                if neighbor in visited:    # 如果鄰居已訪問過，跳過
                    continue

                if neighbor == middleNode: # 如果鄰居是中間node
                    queue.clear()           # 清空queue，因為要從中間node開始新路徑
                    cur_path = path + [neighbor]  # 更新當前路徑，加上中間node
                    queue.append(cur_path)         # 將新路徑加入queue
                    FindMiddle = True             # 標記已找到中間node
                    break                         # 跳出鄰居遍歷

                cur_path = path + [neighbor]  # 更新當前路徑，加上鄰居node
                queue.append(cur_path)         # 將新路徑加入queue

                if FindMiddle == True:         # 如果已找到中間node
                    if neighbor == endNode:    # 並且鄰居是終點node
                        return len(cur_path)-1, cur_path  # 返回路徑長度和路徑

            visited.append(node)  # 將當前node標記為已訪問

    return -1, None  # 如果沒有找到符合條件的路徑，返回 -1 和 None


if __name__ == "__main__":
    content = input().split()           # 讀取第一行輸入並分割成列表
    rest = [int(i) for i in input().split()]  # 讀取第二行輸入並轉換為整數列表

    N = int(content[0])                 # 圖中邊的數量
    startNode = int(content[1])         # 起始node
    endNode = int(content[2])           # 終點node

    dict = {}                            # 初始化圖的鄰接表
    for i in range(N):
        start, end = input().split()     # 讀取每條邊的兩個node
        start = int(start)               # 將起點轉換為整數
        end = int(end)                   # 將終點轉換為整數
        if start not in dict:
            dict[start] = []             # 如果起點不在鄰接表中，初始化其列表
        if end not in dict:
            dict[end] = []               # 如果終點不在鄰接表中，初始化其列表
        dict[start].append(end)          # 將終點加入起點的鄰居列表
        dict[end].append(start)          # 將起點加入終點的鄰居列表（無向圖）

    answer = 99999                        # 初始化最短路徑長度為一個大數
    answer_path = []                      # 初始化最短路徑
    rest_position = 0                     # 初始化中間node位置為 0（表示未找到）

    for n in rest:
        count, path = FindPath(dict, startNode, endNode, n)  # 嘗試找到經過node n 的路徑
        if (count != -1) and (len(path) < answer):         # 如果找到且路徑比目前最短
            answer_path = [str(i) for i in path]           # 更新最短路徑
            rest_position = n                              # 更新中間node
            answer = len(path)                             # 更新最短路徑長度

    if rest_position == 0:
        print("NO")          # 如果沒有找到任何符合條件的路徑，輸出 "NO"
    else:
        print(rest_position) # 輸出選擇的中間node
        print(' '.join(answer_path))  # 輸出最短路徑的node序列