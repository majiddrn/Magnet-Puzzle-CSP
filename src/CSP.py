from cmath import inf
import info

def updateGameMap(var, new_val):

    if new_val == 0 or new_val == info.HomeType.EMPTY:

        info.gameMapUpdate[var["h1"][0]][var["h1"][1]] = 0
        info.gameMapUpdate[var["h2"][0]][var["h2"][1]] = 0

    if new_val == [1, 0]:

        info.gameMapUpdate[var["h1"][0]][var["h1"][1]] = +1
        info.gameMapUpdate[var["h2"][0]][var["h2"][1]] = -1
    
    if new_val == [0, 1]:

        info.gameMapUpdate[var["h1"][0]][var["h1"][1]] = -1
        info.gameMapUpdate[var["h2"][0]][var["h2"][1]] = +1

#*****************************************************************************************************
    
def isGoal():
    # updateGameMap()

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

def mrv(depth):
    minVar:map = {"value": -1, "cnt": -1}
    minVarDomain = 10
    unassignedVars = []

    for v in info.vars:
        if v["value"] == 0:
            unassignedVars.append(v)

    for v in unassignedVars:
        if calDSize(v) < minVarDomain and v["value"] == 0:
            minVarDomain = calDSize(v)
            minVar = v

    return minVar

#*****************************************************************************************************

def chooseVar(depth):

    var_mrv = mrv(depth)

    return var_mrv

#*****************************************************************************************************

def isConsistent_magnetic(var, d):
    var["value"] = d
    updateGameMap(var, d)
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
                        # print(-1)
                        var["value"] = 0
                        updateGameMap(var, 0)
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
                        # print(-2)
                        var["value"] = 0
                        updateGameMap(var, 0)
                        return False
    var["value"] = 0
    updateGameMap(var, 0)

    return True

#*****************************************************************************************************

def isConsistent(var, d):
    var["value"] = d
    updateGameMap(var, d)
    
    # print("--------")
    # print("I'm", var)
    # printGameMapUpdate()
    # print("--------")

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not((i == 0 and j == 0) or i * j != 0):
                wherei = var["h1"][0] + i
                wherej = var["h1"][1] + j

                if wherei < info.m and wherej < info.n and wherej >= 0 and wherej >=0:

                    h1t = info.gameMapUpdate[var["h1"][0]][var["h1"][1]]
                    h2t = info.gameMapUpdate[wherei][wherej]
                    # print(h1t * h2t, "i:", wherei, "j:", wherej)
                    if h1t * h2t > 0:
                        # print(-1)
                        var["value"] = 0
                        updateGameMap(var, 0)
                        return False
                
                wherei = var["h2"][0] + i
                wherej = var["h2"][1] + j

                if wherei < info.m and wherej < info.n and wherej >= 0 and wherej >=0:

                    h1t = info.gameMapUpdate[var["h2"][0]][var["h2"][1]]
                    h2t = info.gameMapUpdate[wherei][wherej]
                    # if h1t == h2t and (h1t != 0 and h2t != 0):
                    # print(h1t * h2t, "i:", wherei, "j:", wherej)
                    if h1t * h2t > 0:
                        # print(-2)
                        var["value"] = 0
                        updateGameMap(var, 0)
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
        # print(-3)
        var["value"] = 0
        updateGameMap(var, 0)
        return False

    # ------------------------------------------------

    # h1 row
    for j in range(info.n):
        if info.gameMapUpdate[var["h1"][0]][j] == +1:
            posRowCount += 1
        
        if info.gameMapUpdate[var["h1"][0]][j] == -1:
            negRowCount += 1

    if posRowCount > info.posRows[var["h1"][0]] or negRowCount > info.negRows[var["h1"][0]]:
        # print(-4)
        var["value"] = 0
        updateGameMap(var, 0)
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
            # print(-5)
            var["value"] = 0
            updateGameMap(var, 0)
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
            # print(-6)
            var["value"] = 0
            updateGameMap(var, 0)
            return False

    # -------------------------------------------------

    # if none of situations above happened, It means that everything constraint is stasfied

    var["value"] = 0
    updateGameMap(var, 0)
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
                    vNeigbor, dir = findVarByPosition(im, jm)
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
                vNeigbor, dir = findVarByPosition(im, jm)
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
        if (v["h1"][0] == i and v["h1"][1] == j):
            return v, 'h1'

        if v["h2"][0] == i and v["h2"][1] == j:
            return v, 'h2'

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
    cluster = [n for n in getNeighbors(var) if n["value"] == 0 ]
    # cluster.append(var)
    arcQueue = [(v_1, v_2) for v_1 in cluster for v_2 in cluster if v_1["cnt"] != v_2["cnt"] ]

    # print(arcQueue)

    while len(arcQueue) != 0:
        x_i, x_j = arcQueue.pop()
        if revise(x_i, x_j):
            if len(x_i["domain"]) == 0: return False
            x_i_neighbors = [n for n in cluster if n["value"] == 0 ]
            for x_k in x_i_neighbors:
                # if x_k["cnt"] == x_i["cnt"]: continue
                arcQueue.append((x_k, x_i))
    return True

#*****************************************************************************************************

def revise(x_i, x_j):
    # revised = False
    for i in range(len(x_i["domain"])):
        noVal = True
        for dj in x_j["domain"]:
            x_i["value"] = x_i["domain"][i]
            updateGameMap(x_i, x_i["domain"][i])
            if isConsistent(x_j, dj):
                noVal = False
                break
            x_i["value"] = 0
            updateGameMap(x_i, 0)
        if noVal:
            x_i["domain"][i] = 0
            return True
            # revised = True
    # return revised

#*****************************************************************************************************

def forwardChecking_magnetic(var):

    goingToChange = []
    count = 0
    neighbors = [v for v in getNeighbors(var) if v["value"] == 0]
    
    if type(var["value"]) is list:
        
        for i in range(len(neighbors)):

            for val_index in range(3):
                if neighbors[i]["domain"][val_index] == 0:
                    continue

                if not isConsistent(neighbors[i], neighbors[i]["domain"][val_index]):
                    neighbors[i]["domain"][val_index] = 0
                    count += 1

            if all(val == 0 for val in neighbors[i]["domain"]):

                return False, []

    return True, goingToChange

#*****************************************************************************************************

def forwardChecking_homesCount(var_assigned):
    neigbors = [v for v in getNeighbors(var_assigned) if v["value"] == 0]

    for var in neigbors:
        h1_i = var["h1"][0]
        h1_j = var["h1"][1]

        h2_i = var["h2"][0]
        h2_j = var["h2"][1]

        for ind in range(2):
            if var["domain"][ind] == 0: continue

            if var["dir"] == info.HomeDir.HORIZONTAL:
                posCountRow = 0
                negCountRow = 0
                
                posCountCol_h1 = 0
                posCountCol_h2 = 0

                negCountCol_h1 = 0
                negCountCol_h2 = 0

                for i in range(info.m):
                    #positives:
                    if info.gameMapUpdate[i][h1_j] == +1:
                        posCountCol_h1 += 1
                    if info.gameMapUpdate[i][h2_j] == +1:
                        posCountCol_h2 += 1
                    
                    #negetives:
                    if info.gameMapUpdate[i][h1_j] == -1:
                        negCountCol_h1 += 1
                    if info.gameMapUpdate[i][h2_j] == -1:
                        negCountCol_h2 += 1

                for j in range(info.n):
                    if info.gameMapUpdate[h1_i][j] == +1:
                        posCountRow += 1
                    if info.gameMapUpdate[h1_i][j] == -1:
                        negCountRow += 1

                if var["domain"][ind] == [1, 0]:
                    posCountCol_h1 += 1
                    negCountCol_h2 += 1
                
                if var["domain"][ind] == [0, 1]:
                    negCountCol_h1 += 1
                    posCountCol_h2 += 1

                posCountRow += 1
                negCountRow += 1

                if posCountRow > info.posRows[h1_i] or negCountRow > info.negRows[h1_i]:
                    var["domain"][ind] = 0
                
                if posCountCol_h1 > info.posColumns[h1_j] or negCountCol_h1 > info.negColumns[h1_j]:
                    var["domain"][ind] = 0

                if posCountCol_h2 > info.posColumns[h2_j] or negCountCol_h2 > info.negColumns[h2_j]:
                    var["domain"][ind] = 0
        
        if var["dir"] == info.HomeDir.VERTICAL:
                posCountCol = 0
                negCountCol = 0
                
                posCountRow_h1 = 0
                posCountRow_h2 = 0

                negCountRow_h1 = 0
                negCountRow_h2 = 0

                for j in range(info.n):
                    #positives:
                    if info.gameMapUpdate[h1_i][j] > 0:
                        posCountRow_h1 += 1
                    if info.gameMapUpdate[h2_i][j] > 0:
                        posCountRow_h2 += 1
                    
                    #negetives:
                    if info.gameMapUpdate[h1_i][j] < 0:
                        negCountRow_h1 += 1
                    if info.gameMapUpdate[h2_i][j] < 0:
                        negCountRow_h2 += 1

                for i in range(info.m):
                    #positives:
                    if info.gameMapUpdate[i][h1_j] > 0:
                        posCountCol += 1
                    if info.gameMapUpdate[i][h1_j] < 0:
                        negCountCol += 1

                if var["domain"][ind] == [1, 0]:
                    posCountRow_h1 += 1
                    negCountRow_h2 += 1
                
                if var["domain"][ind] == [0, 1]:
                    negCountRow_h1 += 1
                    posCountRow_h2 += 1

                if posCountCol + 1 > info.posColumns[h1_j] or negCountCol + 1 > info.negColumns[h1_j]:
                    var["domain"][ind] = 0

                if posCountRow_h1 > info.posRows[h1_i] or negCountRow_h1 > info.negRows[h1_i]:
                    var["domain"][ind] = 0

                if posCountRow_h2 > info.posRows[h2_i] or negCountRow_h2 > info.negRows[h2_i]:
                    var["domain"][ind] = 0

        if all(val == 0 for val in var["domain"]):
            return False
    
    return True

#*****************************************************************************************************

def forwardChecking_var(var):
    res_magnetic = forwardChecking_magnetic(var)

    return res_magnetic, []
                            
#*****************************************************************************************************

def lcv(var):
    neighbors = [n for n in getNeighbors(var) if n["value"] == 0]
    newDomain = []

    for d in var["domain"]:
        if d == 0: continue

        c_count = 0

        var["value"] = d
        updateGameMap(var, d)

        for neighbor in neighbors:
            if not isConsistent_magnetic(neighbor, [0, 1]):
                c_count += 1
            
            if not isConsistent_magnetic(neighbor, [1, 0]):
                c_count += 1
        
        var["value"] = 0
        updateGameMap(var, 0)

        newDomain.append({"val": d, "c_count": c_count})
    
    # print("--------")

    # print(newDomain)
    newDomain = sorted(newDomain, key=lambda x: x["c_count"], reverse=True)

    # print(newDomain)
    # print("------")

    domainReturn = []

    for l in newDomain:
        domainReturn.append(l["val"])

    return domainReturn

        
#*****************************************************************************************************

def storeDomains(listToStore):
    lr = []
    for var in listToStore:
        lr.append({"cnt": var["cnt"], "domain": var["domain"].copy(), "value": var["value"]})

    return lr

#*****************************************************************************************************

def regetDomains(stored):
    for i in range(len(stored)):    
        for j in range(len(info.vars)):
            if info.vars[j]["cnt"] == stored[i]["cnt"]:
                info.vars[j]["domain"] = stored[i]["domain"].copy()
        

#*****************************************************************************************************
    

def backTracking(depth=0):
    if isGoal():
        return True
    
    var = chooseVar(depth)

    if var["value"] == -1: return False

    # print(var["cnt"])

    domain = lcv(var)
    # domain = var["domain"]

    for i in range(len(domain)):
        # if var["domain"][i] == 0: continue
        # if domain == 0: continue

        value = domain[i]

        if isConsistent(var, value):
            # print("++++++:", value)
            var["value"] = value
            # var["domain"][i] = 0
            if domain[i] == [0, 1]:
                var["domain"][0] = 0
            if domain[i] == [1, 0]:
                var["domain"][1] = 0
            if domain[i] == info.HomeType.EMPTY:
                var["domain"][2] =0
            updateGameMap(var, value)

            # print(var["cnt"], var["value"], depth)

            saved_domains = storeDomains([n for n in getNeighbors(var) if n["value"] == 0])

            ac3_ret = ac3(var)

            # fc, c_list = forwardChecking_var(var)            

            # if fc:
                # bt = backTracking(depth + 1)
                # if bt:
                    # return bt
        
            if ac3_ret:
                bt = backTracking(depth + 1)
                if bt:
                    return bt

            regetDomains(saved_domains)
            var["value"] = 0
            # var["domain"][i] = value
            if domain[i] == [0, 1]:
                var["domain"][0] = value
            if domain[i] == [1, 0]:
                var["domain"][1] = value
            if domain[i] == info.HomeType.EMPTY:
                var["domain"][2] = value
            updateGameMap(var, 0)



    

        
        
























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
        print(l)

def printStack():
    for l in info.vars:
        print(l)
    # print(len(info.vars))