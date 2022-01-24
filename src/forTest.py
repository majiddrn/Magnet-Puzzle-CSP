# import CSP
# import info

# l = [{}]

# info.gameMap = [[]]

# info.posColumns = [4, 4, 4, 4]
# info.negColumns = [4, 4, 4, 4]

# info.posRows = [4, 4, 4, 4]
# info.negRows = [4, 4, 4, 4]

# info.m = 4
# info.n = 4

# for i in range(4):
#     info.gameMap.append([])
#     info.gameMap[i] = list(map(int, input().split()))
# info.gameMap.pop()

# cnt = 1

# for i in range(4):
#     for j in range(4):
#         if i + 1 < 4:
#             if info.gameMap[i][j] == info.gameMap[i + 1][j]:
#                 info.vars.append({"cnt": cnt, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
#                             , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": 0})
#                 info.varsStatic.append({"cnt": cnt + 1, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
#                             , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": 0})
#                 cnt += 1
#         if j + 1 < 4:
#             if info.gameMap[i][j] == info.gameMap[i][j + 1]:
#                 info.vars.append({"cnt": cnt, "h1": [i, j], "h2": [i, j + 1], "dir": info.HomeDir.HORIZONTAL
#                                 , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3, "value": 0})
#                 info.varsStatic.append({"cnt": cnt + 1, "h1": [i, j], "h2": [i, j + 1], "dir": info.HomeDir.HORIZONTAL
#                                 , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3, "value": 0})
#                 cnt += 1

# i = 5
# storedDomains = CSP.storeDomains(CSP.getNeighbors(info.vars[i]))
# info.vars[i]["value"] = [1, 0]
# info.vars[i]["domain"][0] = 0
# print("CNT::", info.vars[i]["cnt"])
# CSP.forwardChecking_var(info.vars[i])
# print(CSP.calDSize(info.vars[i]))

# CSP.regetDomains(storedDomains)

# i = 2
# storedDomains = CSP.storeDomains(CSP.getNeighbors(info.vars[i]))
# info.vars[i]["value"] = [1, 0]
# info.vars[i]["domain"][0] = 0
# print("CNT::", info.vars[i]["cnt"])
# CSP.forwardChecking_var(info.vars[i])
# print(CSP.calDSize(info.vars[i]))

# CSP.regetDomains(storedDomains)

# def printStack():
#     for l in info.vars:
#         print(l)

# printStack()

# # var = {"cnt": 1, "h1": [1, 2], "h2": [2, 2], "dir": info.HomeDir.VERTICAL
# #                             , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": 0}

# # var = {"cnt": cnt, "h1": [i, j], "h2": [i + 1, j], "dir": info.HomeDir.VERTICAL
#                             # , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": [1, 0]}

# # print(CSP.checkConstraint(2, 2, [], var))

print([0, 1] == 0)