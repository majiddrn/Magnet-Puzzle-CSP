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

cnt = 1

for i in range(info.m - 1):
    for j in range(info.n - 1):
        if info.gameMap[i, j] == info.gameMap[i + 1, j]:
            info.vars.append({"cnt": cnt, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY],"value": 0})
            info.varsStatic.append({"cnt": cnt, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY],"value": 0})
        
        if info.gameMap[i, j] == info.gameMap[i, j + 1]:
            info.vars.append({"cnt": cnt, "h1": [i, j], "h2": [i, j + 1], "dir": info.HomeDir.HORIZONTAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY],"value": 0})
            info.varsStatic.append({"cnt": cnt, "h1": [i, j], "h2": [i, j + 1], "dir": info.HomeDir.HORIZONTAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY],"value": 0})
        
        cnt += 1

varsCount = cnt

info.varsStack.append(info.vars)