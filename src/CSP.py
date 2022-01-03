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

def chooseVar():
    for v in info.vars:
        if v["value"] == 0:
            return v

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


def backTracking():
    if isGoal():
        return True
    varAnalyze = chooseVar()
    if varAnalyze == None: return False
    for d in varAnalyze["domain"]:
        print(d)
        if isConsistent(varAnalyze, d):
            varAnalyze["value"] = d
            updateGameMap()
            bt = backTracking()
            if bt:
                return bt
        varAnalyze["value"] = 0
        updateGameMap()
    return False