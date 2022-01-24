import time
import CSP
import info

#Getting input from the user:

ms, ns = input().split()

info.posRows = list(map(int, input().split()))
info.negRows = list(map(int, input().split()))

info.posColumns = list(map(int,input().split()))
info.negColumns = list(map(int, input().split()))

# print(f"pos Rows:{info.posRows} - negRows:{info.negRows}")
# print(f"pos Columns:{info.posColumns} - negColumns:{info.negColumns}")

info.gameMap = [[]]

info.m = int(ms)
info.n = int(ns)

info.gameMapUpdate = []
    
for i in range(info.m):
    info.gameMapUpdate.append([])
    for j in range(info.n):
        info.gameMapUpdate[i].append(0)

for i in range(info.m):
    info.curr_posRows.append(0)
    info.curr_negRows.append(0)

for j in range(info.n):
    info.curr_posCols.append(0)
    info.curr_negCols.append(0)

for i in range(info.m):
    info.gameMap.append([])
    info.gameMap[i] = list(map(int, input().split()))
info.gameMap.pop()

cnt = 1

for i in range(info.m):
    for j in range(info.n):
        if i + 1 < info.m:
            if info.gameMap[i][j] == info.gameMap[i + 1][j]:
                info.vars.append({"cnt": cnt, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": 0})
                info.varsStatic.append({"cnt": cnt, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": 0})
                cnt += 1
        if j + 1 < info.n:
            if info.gameMap[i][j] == info.gameMap[i][j + 1]:
                info.vars.append({"cnt": cnt, "h1": [i, j], "h2": [i, j + 1], "dir": info.HomeDir.HORIZONTAL
                                , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3, "value": 0})
                info.varsStatic.append({"cnt": cnt, "h1": [i, j], "h2": [i, j + 1], "dir": info.HomeDir.HORIZONTAL
                                , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3, "value": 0})
                cnt += 1

# exit(0)        

varsCount = cnt

time_start = (time.time() * 1000) / 1000

print(CSP.backTracking())

time_end = (time.time() * 1000) / 1000

print("It took", time_end - time_start)

finalGameMap = []

for i in range(info.m):
    finalGameMap.append([])
    for j in range(info.n):
        finalGameMap[i].append('*')

for l in info.vars:
    print(l)


def printMap():
    for l in info.vars:
        if type(l["value"]) is list:
            cntStr = str(l["cnt"])
            if l["value"][0] == 1:
                finalGameMap[l["h1"][0]][l["h1"][1]] = cntStr + '+'
                finalGameMap[l["h2"][0]][l["h2"][1]] = cntStr + '-'

            if l["value"][0] == 0:
                finalGameMap[l["h1"][0]][l["h1"][1]] = cntStr + '-'
                finalGameMap[l["h2"][0]][l["h2"][1]] = cntStr + '+'

    for i in range(info.m):
        for j in range(info.n):
            print(f"\t{finalGameMap[i][j]}", end=' ')
        print()

printMap()
