def findMaxValueDFS(s, caveGraph, pathStack):
    # 如果節點 s 已在路徑棧中，或 s 等於 0，則返回 0
    if s in pathStack or s == 0:
        return 0
    else:
        # 將節點 s 加入路徑棧
        pathStack.append(s)
        # 計算當前節點的金礦數量，並遞迴計算子節點路徑的最大值
        result = caveGraph[s]["Gold"] + max(
            findMaxValueDFS(caveGraph[s]["Next1"], caveGraph, pathStack),
            findMaxValueDFS(caveGraph[s]["Next2"], caveGraph, pathStack),
        )
        # 回溯，從路徑棧中移除節點 s
        pathStack.pop()
        return result


def findMaxValue(s, caveGraph):
    # 初始化路徑棧，並將起始節點加入路徑棧
    pathStack = list()
    pathStack.append(s)
    # 返回起始節點的金礦數量，加上從兩個可能的下一步節點中獲取的最大值
    return caveGraph[s]["Gold"] + max(
        findMaxValueDFS(caveGraph[s]["Next1"], caveGraph, pathStack),
        findMaxValueDFS(caveGraph[s]["Next2"], caveGraph, pathStack),
    )


def main():
    # 讀取節點數量 n 和起始節點 k
    n, k = [int(x) for x in input().split()]
    caveGraph = dict()
    # 讀取每個節點的金礦數量及其兩個相鄰節點
    for _ in range(n):
        idx, gold, Y, Z = [int(x) for x in input().split()]
        caveInfo = dict()
        caveInfo["Gold"] = gold
        caveInfo["Next1"] = Y
        caveInfo["Next2"] = Z
        caveGraph[idx] = caveInfo

    # 計算從起始節點出發可獲得的最大金礦數量並輸出結果
    result = findMaxValue(k, caveGraph)
    print(result)


main()
