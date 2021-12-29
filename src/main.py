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