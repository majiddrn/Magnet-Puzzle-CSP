import info

#Getting input from the user:

ms, ns = input().split()

info.posRows = list(map(int, input().split()))
info.negRows = list(map(int, input().split()))

info.posColumns = list(map(int,input().split()))
info.negColumns = list(map(int, input().split()))

info.gameMap = [[]]

info.m = int(ms)
info.n = int(ns)

for i in range(info.m):
    info.gameMap.append([])
    info.gameMap[i] = list(map(int, input().split()))
info.gameMap.pop()

for i in range(info.m - 1):
    for j in range(info.n - 1):
        if info.gameMap[i, j] == info.gameMap[i + 1, j]:
            info.vars.append({"h1": [i, j], "h2": [i + 1, j], "d1": [0, 1], "d2": [1, 0], "d3": info.HomeType.EMPTY,"value": []})
            info.varsStatic.append({"h1": [i, j], "h2": [i + 1, j], "d1": [0, 1], "d2": [1, 0], "d3": info.HomeType.EMPTY,"value": []})
        
        if info.gameMap[i, j] == info.gameMap[i, j + 1]:
            info.vars.append({"h1": [i, j], "h2": [i, j + 1], "d1": [0, 1], "d2": [1, 0], "d3": info.HomeType.EMPTY,"value": []})
            info.varsStatic.append({"h1": [i, j], "h2": [i, j + 1], "d1": [0, 1], "d2": [1, 0], "d3": info.HomeType.EMPTY,"value": []})