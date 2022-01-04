import info

def updateGameMap():
    info.gameMapUpdate = []
    
    for i in range(info.m):
        info.gameMapUpdate.append([])
        for j in range(info.n):
            info.gameMapUpdate[i].append(0)

    # print(info.gameMapUpdate)

    for v in info.vars:
        if type(v["value"]) is list:
            if v["value"] == [1, 0]:
                info.gameMapUpdate[v["h1"][0]][v["h1"][1]] = +1
                info.gameMapUpdate[v["h2"][0]][v["h2"][1]] = -1
            if v["value"] == [0, 1]:
                info.gameMapUpdate[v["h1"][0]][v["h1"][1]] = -1
                info.gameMapUpdate[v["h2"][0]][v["h2"][1]] = +1

#*****************************************************************************************************
    
def isGoal():
    updateGameMap()

    #checking rows:
    for i in range(info.m):
        posRow = 0
        negRow = 0
        for j in range(info.n):
            if info.gameMapUpdate[i][j] == +1:
                posRow += 1
            if info.gameMapUpdate[i][j] == -1:
                negRow += 1
        if posRow != info.posRows[i] or negRow != info.negRows[i]:
            return False
    
    for j in range(info.n):
        posColumn = 0
        negColumn = 0
        for i in range(info.m):
            if info.gameMapUpdate[i][j] == +1:
                posColumn += 1
            if info.gameMapUpdate[i][j] == -1:
                negColumn += 1
        if posColumn != info.posColumns[j] or negColumn != info.negColumns[j]:
            return False
    
    return True

#*****************************************************************************************************

def mrv():
    minVar:map = {"value": -1}
    minVarDomain = 10
    unassignedVars = []

    for v in info.vars:
        if v["value"] == 0:
            unassignedVars.append(v)

    for v in unassignedVars:
        if calDSize(v) < minVarDomain:
            minVarDomain = calDSize(v)
            minVar = v

    # print("*-*-*-*-*-*-*-*-*-*-*-*-*")
    # print("\t\t", minVarDomain, minVar["cnt"])
    # printStack()
    # printMap()
    # print("*-*-*-*-*-*-*-*-*-*-*-*-*")

    return minVar

#*****************************************************************************************************

def chooseVar():

    return mrv()

    # for v in info.vars:
    #     if v["value"] == 0:
    #         return v

#*****************************************************************************************************

def isConsistent_magnetic(var, d):
    var["value"] = d
    updateGameMap()
    # print("=++++++++++++++=")
    # printGameMapUpdate()
    # print("=++++++++++++++=")
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not((i == 0 and j == 0) or i*j != 0):
                wherei = var["h1"][0] + i
                wherej = var["h1"][1] + j

                if wherei < info.m and wherej < info.n:
                    h1t = info.gameMapUpdate[var["h1"][0]][var["h1"][1]]
                    h2t = info.gameMapUpdate[wherei][wherej]
                    if h1t == h2t and (h1t != 0 and h2t != 0):
                        # print("=++++++++++++++=")
                        # printGameMapUpdate()
                        # print("=++++++++++++++=")
                        print(-1)
                        var["value"] = 0
                        updateGameMap()
                        return False
                
                wherei = var["h2"][0] + i
                wherej = var["h2"][1] + j

                if wherei < info.m and wherej < info.n:
                    # print("=++++++++++++++=")
                    # printGameMapUpdate()
                    # print("=++++++++++++++=")
                    h1t = info.gameMapUpdate[var["h2"][0]][var["h2"][1]]
                    h2t = info.gameMapUpdate[wherei][wherej]
                    if h1t == h2t and (h1t != 0 and h2t != 0):
                        print(-2)
                        var["value"] = 0
                        updateGameMap()
                        return False
    var["value"] = 0
    updateGameMap()

    return True

#*****************************************************************************************************

def isConsistent(var, d):
    var["value"] = d
    updateGameMap()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not((i == 0 and j == 0) or i*j != 0):
                wherei = var["h1"][0] + i
                wherej = var["h1"][1] + j

                if wherei < info.m and wherej < info.n:

                    h1t = info.gameMapUpdate[var["h1"][0]][var["h1"][1]]
                    h2t = info.gameMapUpdate[wherei][wherej]
                    if h1t == h2t and (h1t != 0 and h2t != 0):
                        print(-1)
                        var["value"] = 0
                        updateGameMap()
                        return False
                
                wherei = var["h2"][0] + i
                wherej = var["h2"][1] + j

                if wherei < info.m and wherej < info.n:

                    h1t = info.gameMapUpdate[var["h2"][0]][var["h2"][1]]
                    h2t = info.gameMapUpdate[wherei][wherej]
                    if h1t == h2t and (h1t != 0 and h2t != 0):
                        print(-2)
                        var["value"] = 0
                        updateGameMap()
                        return False

    posColCount = 0
    negColCount = 0
    posColCount_h = 0
    negColCount_h = 0

    posRowCount = 0
    negRowCount = 0
    posRowCount_v = 0
    negRowCount_v = 0
    
    # h1 column
    for i in range(info.m):
        if info.gameMapUpdate[i][var["h1"][1]] == +1:
            posColCount += 1

        if info.gameMapUpdate[i][var["h1"][1]] == -1:
            negColCount += 1
    
    if posColCount > info.posColumns[var["h1"][1]] or negColCount > info.negColumns[var["h1"][1]]:
        print(-3)
        var["value"] = 0
        updateGameMap()
        return False

    # ------------------------------------------------

    # h1 row
    for j in range(info.n):
        if info.gameMapUpdate[var["h1"][0]][j] == +1:
            posRowCount += 1
        
        if info.gameMapUpdate[var["h1"][0]][j] == -1:
            negRowCount += 1

    if posRowCount > info.posRows[var["h1"][0]] or negRowCount > info.negRows[var["h1"][0]]:
        print(-4)
        var["value"] = 0
        updateGameMap()
        return False

    # ------------------------------------------------

    # if horizontal we check 'h2's column aswell
    if var["dir"] == info.HomeDir.HORIZONTAL:
        for i in range(info.m):
            if info.gameMapUpdate[i][var["h2"][1]] == +1:
                posColCount_h += 1

            if info.gameMapUpdate[i][var["h2"][1]] == -1:
                negColCount_h += 1
        
        if posColCount_h > info.posColumns[var["h2"][1]] or negColCount_h > info.negColumns[var["h2"][1]]:
            print(-5)
            var["value"] = 0
            updateGameMap()
            return False

    # ------------------------------------------------

    # if vertical we check 'h2's row aswell
    if var["dir"] == info.HomeDir.VERTICAL:
        for j in range(info.n):
            if info.gameMapUpdate[var["h2"][0]][j] == +1:
                posRowCount_v += 1
            
            if info.gameMapUpdate[var["h2"][0]][j] == -1:
                negRowCount_v += 1

        if posRowCount_v > info.posRows[var["h2"][0]] or negRowCount_v > info.negRows[var["h2"][0]]:
            print(-6)
            var["value"] = 0
            updateGameMap()
            return False

    # -------------------------------------------------

    # if none of situations above happened, It means that everything constraint is stasfied

    var["value"] = 0
    updateGameMap()
    return True

#*****************************************************************************************************

def backingUpGame():
    for v in info.vars:
        if v["value"] == 0:
            v["domain"] = [[0, 1], [1, 0], 'e']
            # v["dSize"] = 3

    for v in info.vars:
        if v["value"] != 0:
            forwardChecking_var(v)

#*****************************************************************************************************

def getNeighbors(var):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1 , 2):
            if (i == 0 and j == 0) or (i * j != 0): continue

            im = var["h1"][0] + i
            jm = var["h1"][1] + j

            if im < info.m and jm < info.n and im >= 0 and jm >= 0:
                vNeigbor = findVarByPosition(im, jm)
                repeated = False
                for v in neighbors:
                    if v["cnt"] == vNeigbor["cnt"]:
                        repeated = True
                        break
                if not repeated and vNeigbor["cnt"] != var["cnt"]:
                    neighbors.append(vNeigbor)

            im = var["h2"][0] + i
            jm = var["h2"][1] + j

            if im < info.m and jm < info.n and im >= 0 and jm >= 0:
                repeated = False
                vNeigbor = findVarByPosition(im, jm)
                for v in neighbors:
                    if v["cnt"] == vNeigbor["cnt"]:
                        repeated = True
                        break
                if not repeated and vNeigbor["cnt"] != var["cnt"]:
                    neighbors.append(vNeigbor)

    return neighbors


#*****************************************************************************************************

def findVarByPosition(i, j):
    for v in info.vars:
        if (v["h1"][0] == i and v["h1"][1] == j) or (v["h2"][0] == i and v["h2"][1] == j):
            return v

        # if v["h2"][0] == i and v["h2"][1] == j:
        #     return v, 'h2'

#*****************************************************************************************************

def calDSize(var):
    dSize = 3
    if var["domain"][0] == 0:
        dSize -= 1
    if var["domain"][1] == 0:
        dSize -= 1
    if var["domain"][2] == 0:
        dSize -= 1
    return dSize

#*****************************************************************************************************

def forwardChecking():
    for v in info.vars:
        if type(v["value"]) is list:
            forwardChecking_var(v)

#*****************************************************************************************************

arcQueue = []

def ac3(var):
    while len(var) != 0:
        x_i, x_j = arcQueue.pop()
        if revise(x_i, x_j):
            if len(x_i["domain"]) == 0: return False
            x_i_neighbors = getNeighbors(x_i)
            for x_k in x_i_neighbors:
                if x_k["cnt"] == x_j["cnt"]: continue
                arcQueue.append((x_i, x_j))
    return True

#*****************************************************************************************************

def revise(x_i, x_j):
    revised = False
    for i in range(len(x_i["domain"])):
        noVal = True
        for dj in x_j["domain"]:
            x_i["value"] = x_i["domain"][i]
            updateGameMap()
            if isConsistent(x_j, dj):
                noVal = False
                break
            x_i["value"] = 0
            updateGameMap()
        if noVal:
            x_i["domain"][i] = 0
            revised = True
    return revised

#*****************************************************************************************************

def forwardChecking_var(var):
    print("<<<<<<>>>>>>", var["cnt"])
    if type(var["value"]) is list:
        return True
        neighbors = getNeighbors(var)
        for i in range(len(neighbors)):

            if not isConsistent_magnetic(neighbors[i], [1, 0]):
                print(neighbors[i]["cnt"] ,"-", neighbors[i]["domain"][1])
                neighbors[i]["domain"][1] = 0

            if not isConsistent_magnetic(neighbors[i], [0, 1]):
                print(neighbors[i]["cnt"], "-", neighbors[i]["domain"][0])
                neighbors[i]["domain"][0] = 0
            # print("M----")
            # printLimited()
            # print("M----")
    
    
    # printMap()
    # printLimited()
    print("<<<<<<>>>>>>", var["cnt"])

    for v in info.vars:
        if calDSize(v) == 0:
            # print("<<<<<<I'M FAILING>>>>>>", v["cnt"], var["cnt"])
            # printMap()
            # printStack()
            # print("<<<<<<I'M FAILING>>>>>>", v["cnt"], var["cnt"])
            return False

    return True
                            
#*****************************************************************************************************

def storeDomains():
    lr = []
    for var in info.vars:
        lr.append({"cnt": var["cnt"], "domain": var["domain"].copy()})

    return lr

#*****************************************************************************************************

def regetDomains(stored):
    for i in range(len(stored)):
        info.vars[i]["domain"] = stored[i]["domain"].copy()
        # if stored[i]["domain"][0] == [0, 1]:
        #     info.vars[i]["domain"][0] = [0, 1]
        # else:
        #     info.vars[i]["domain"][0] = 0

        # if stored[i]["domain"][1] == [1, 0]:
        #     info.vars[i]["domain"][1] = [1, 0]
        # else:
        #     info.vars[i]["domain"][1] = 0

        # info.vars[i]["domain"][2] = stored[i]["domain"][2]
        
        # print("STORED DSIZE::::", stored[i]["dSize"])
        

#*****************************************************************************************************

def backTracking():
    if isGoal():
        return True
    varAnalyze = chooseVar()
    if varAnalyze["value"] == -1: return False
    d = varAnalyze["domain"]
    # if varAnalyze == None: return False
    for i in range(3):
        if d[i] == 0: continue
        print(d[i])
        domain = storeDomains()
        if isConsistent(varAnalyze, d[i]):
            varAnalyze["value"] = d[i]
            varAnalyze["domain"][i] = 0
            updateGameMap()
            fc = forwardChecking_var(varAnalyze)
            printGameMapUpdate()
            if fc:    
                bt = backTracking()
                if bt:
                    return bt
        # varAnalyze["value"] = 0
        varAnalyze["domain"][i] = varAnalyze["value"]
        varAnalyze["value"] = 0
        updateGameMap()
        regetDomains(domain)
    return False

        
        
























finalGameMap = []

def printMap():
    for i in range(info.m):
        finalGameMap.append([])
        for j in range(info.n):
            finalGameMap[i].append('\t*')

    for l in info.vars:
        if type(l["value"]) is list:
            cntStr = str(l["cnt"])
            if l["value"] == [1, 0]:
                finalGameMap[l["h1"][0]][l["h1"][1]] = '\t' + cntStr + '+'
                finalGameMap[l["h2"][0]][l["h2"][1]] = '\t' + cntStr + '-'

            if l["value"] == [0, 1]:
                finalGameMap[l["h1"][0]][l["h1"][1]] = '\t' + cntStr + '-'
                finalGameMap[l["h2"][0]][l["h2"][1]] = '\t' + cntStr + '+'
            
        else:
            if l["value"] == info.HomeType.EMPTY or l["value"] == 0:
                finalGameMap[l["h1"][0]][l["h1"][1]] = '\t' + '*'
                finalGameMap[l["h2"][0]][l["h2"][1]] = '\t' + '*'

    for i in range(info.m):
        for j in range(info.n):
            print(finalGameMap[i][j], end=' ')
        print()

# printMap()

def printGameMapUpdate():
    for i in range(info.m):
        for j in range(info.n):
            print(f"\t{info.gameMapUpdate[i][j]}", end='')
        print()

def printLimited():
    for l in info.vars:
        if calDSize(l) != 3:
            print(l)

def printStack():
    for l in info.vars:
        print(l)
    # print(len(info.vars))