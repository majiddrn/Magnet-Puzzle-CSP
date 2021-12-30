import info

# def addPos(im, jm):
#     info.posHomes.add([im, jm])

# def addNeg(im, jm):
#     info.negHomes.add([im, jm])

def checkHomeType(im, jm, l):
    # if [im, jm] in info.posHomes:
    #     return info.HomeType.POSITIVE
    # if [im, jm] in info.negHomes:
    #     return info.HomeType.NEGETIVE
    # return info.HomeType.EMPTY

    for var in l:
        # print(var)
        if var["h1"][0] == im and var["h1"][1] == jm:
            if var["value"] == 0:
                return info.HomeType.NOT_ASSIGNED
            
            if type(var["value"]) is list:
                if var["value"][0] == 1:
                    return info.HomeType.POSITIVE
                if var["value"][0] == 0:
                    return info.HomeType.NEGETIVE
        
        if var["h2"][0] == im and var["h2"][1] == jm:
            if var["value"] == 0:
                return info.HomeType.NOT_ASSIGNED

            if type(var["value"]) is list:
                if var["value"][1] == 1:
                    return info.HomeType.POSITIVE
                if var["value"][1] == 0:
                    return info.HomeType.NEGETIVE
    
    return info.HomeType.EMPTY

def checkHome2(i1, j1):
    if i1 != info.m - 1:
        if info.gameMap[i1][j1] == info.gameMap[i1 + 1][j1]:
            return [i1 + 1, j1]
    
    if j1 != info.n - 1:
        if info.gameMap[i1][j1] == info.gameMap[i1][j1 + 1]:
            return [i1, j1 + 1]

def checkMagneticMatch(im, jm, l):
    if im != 0:
        if checkHomeType(im - 1, jm, l) == checkHomeType(im, jm, l):
            return False

    if im != info.m - 1:
        if checkHomeType(im + 1, jm, l) == checkHomeType(im, jm, l):
            return False

    if jm != 0:
        if checkHomeType(im, jm - 1, l) == checkHomeType(im, jm, l):
            return False
    
    if jm != info.n - 1:
        if checkHomeType(im, jm + 1, l) == checkHomeType(im, jm, l):
            return False

    return True

def checkConstraint(im, jm, l):
    home1 = [im, jm]
    home2 = checkHome2(i1=im, j1=jm)

    posCountColumn = 0
    negCountColumn = 0

    posCountRow = 0
    negCountRow = 0

    for i in range(info.m):
        if checkHomeType(i, jm, l) == info.HomeType.POSITIVE:
            posCountColumn += 1

        if checkHomeType(i, jm, l) == info.HomeType.NEGETIVE:
            negCountColumn += 1
    
    for j in range(info.n):
        if checkHomeType(im, j, l) == info.HomeType.POSITIVE:
            posCountRow += 1
        
        if checkHomeType(im, j, l) == info.HomeType.NEGETIVE:
            negCountRow += 1

    if posCountColumn > info.posColumns[jm] or posCountRow > info.posRows[im]:
        return False
        
    if negCountColumn > info.negColumns[jm] or negCountRow > info.negRows[im]:
        return False 

    # print(home1)
    # print(home2)

    if not checkMagneticMatch(home1[0], home1[1], l) or not checkMagneticMatch(home2[0], home2[1], l):
        return False

    return True

def assignmentComplete():
    cnt = 0
    top:list

    top = list(info.varsStack[-1])

    i:int

    for i in range(len(top)):
        if type(top[i]["value"]) is list:
            cnt += 1

    # print(cnt, sum(info.posRows))

    if cnt == sum(info.posRows):
        return True
    else:
        return False

def chooseVar_MRV():
    minVar = 0
    minDCount = 10

    for var in info.varsStack[-1]:
        cntDomains = 3
        if var["value"] == 0:
            for d in var["domain"]:
                if d == 0:
                    cntDomains -= 1

            if cntDomains < minDCount:
                minDCount = cntDomains
                minVar = var

    # print(minVar["cnt"], minDCount)

    return minVar

def findSpeceficVar(listSent, cnt):
    for l in listSent:
        if l["cnt"] == cnt:
            return l

def findSpeceficVar_xy(listSent, im, jm):
    for l in listSent:
        if (l["h1"][0] == im and l["h1"][1] == jm) or (l["h2"][0] == im and l["h2"][1] == jm):
            return l

def forwardChecking(var, cnt, vars):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == -1 and j == -1: continue
            if var["dir"] == info.HomeDir.HORIZONTAL:
                if i == 1 and j == -1: continue
            if var["dir"] == info.HomeDir.VERTICAL:
                if i == -1 and j == 1: continue

            varh1i = var["h1"][0]
            varh1j = var["h1"][1]
            varh2i = var["h2"][0]
            varh2j = var["h2"][1]

            if varh1i + i < 0 or varh1j + j < 0: continue
            if varh1j + i > info.m or varh1j + j > info.n: continue

            if (i == -1 and j == 0) or (i == 0 and j == -1):        # in this situation, only h1 effects
                varLimitted = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                if varLimitted["h1"][0] == varh1i + i and varLimitted["h1"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][1] = 0
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][0] = 0
                
                if varLimitted["h2"][0] == varh1i + i and varLimitted["h2"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][0] = 0
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][1] = 0
            else:
                varLimitted = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                if varLimitted["h1"][0] == varh1i + i and varLimitted["h1"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][0] = 0
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][1] = 0
                
                if varLimitted["h2"][0] == varh1i + i and varLimitted["h2"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][1] = 0
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][0] = 0


            # varLimitted = findSpeceficVar_xy(vars, i + , j)
    for l in vars:
        if l["domain"][0] == 0 and l["domain"][1] == 0 and l["domain"][2] == 0:
            return False
    
    return True
        
def deleteFromDomain(var, v):
    for i in range(len(var["domain"])):
        if var["domain"][i] == v:
            var["domain"][i] = 0

def backTracking():
    if assignmentComplete():
        return True
    
    varAnalyze = chooseVar_MRV()
    for d in varAnalyze["domain"]:
        if d == 0: continue

        if type(d) is list:
            dNew = d.copy()
        else:
            dNew = d

        # print (len(info.varsStack))
        newVars = info.varsStack[-1][:]
        varChainging = findSpeceficVar(newVars, varAnalyze["cnt"])
        varChainging["value"] = dNew
        # deleteFromDomain(varChainging, dNew)
        # print(varChainging)
        if checkConstraint(varChainging["h1"][0], varChainging["h1"][1], newVars):
            # printStack()
            infrences = forwardChecking(varChainging , varChainging["cnt"], newVars)
            # print(infrences)
            info.varsStack.append(newVars)
            # print(info.varsStack[-1])
            if infrences:
                # print("HERE")
                resultBt = backTracking()
                if resultBt:
                    return resultBt
        if len(info.varsStack) != 1:
            info.varsStack.pop()
    return False

















def printStack():
    for l in info.varsStack[-1]:
        print(l)
    print(len(info.varsStack))