import info

def checkHomeType(im, jm, l, var):

    # for var in l:
        # print(var)

    if var["value"] == info.HomeType.EMPTY:
        return info.HomeType.EMPTY
    
    if var["value"] == 0:
        return info.HomeType.NOT_ASSIGNED
    
    if type(var["value"]) is list:
        if var["h1"] == [im, jm]: 
            if var["value"] == [1, 0]:
                return info.HomeType.POSITIVE
            else:
                return info.HomeType.NEGETIVE

        if var["h2"] == [im, jm]:
            if var["value"] == [0, 1]:
                return info.HomeType.POSITIVE
            else:
                return info.HomeType.NEGETIVE

    # if var["h1"][0] == im and var["h1"][1] == jm:
    #     if var["value"] == 0:
    #         return info.HomeType.NOT_ASSIGNED

    #     if var["value"] == info.HomeType.EMPTY:
    #         return var["value"]
        
    #     if type(var["value"]) is list:
    #         if var["value"] == [1, 0]:
    #             return info.HomeType.POSITIVE
    #         if var["value"] == [0, 1]:
    #             return info.HomeType.NEGETIVE
    
    # if var["h2"][0] == im and var["h2"][1] == jm:
    #     if var["value"] == 0:
    #         return info.HomeType.NOT_ASSIGNED

    #     if var["value"] == info.HomeType.EMPTY:
    #         return var["value"]
            
    #     if type(var["value"]) is list:
    #         if var["value"] == [0, 1]:
    #             return info.HomeType.POSITIVE
    #         if var["value"] == [1, 0]:
    #             return info.HomeType.NEGETIVE
    
    return info.HomeType.EMPTY

def checkHome2(i1, j1):
    if i1 != info.m - 1:
        if info.gameMap[i1][j1] == info.gameMap[i1 + 1][j1]:
            return [i1 + 1, j1]
    
    if j1 != info.n - 1:
        if info.gameMap[i1][j1] == info.gameMap[i1][j1 + 1]:
            return [i1, j1 + 1]

def checkMagneticMatch(vars, var):
    print("dawdawd", var["value"])
    # if im != 0:
    #     if checkHomeType(im - 1, jm, l) == checkHomeType(im, jm, l):
    #         return False

    # if im != info.m - 1:
    #     if checkHomeType(im + 1, jm, l) == checkHomeType(im, jm, l):
    #         return False

    # if jm != 0:
    #     if checkHomeType(im, jm - 1, l) == checkHomeType(im, jm, l):
    #         return False
    
    # if jm != info.n - 1:
    #     if checkHomeType(im, jm + 1, l) == checkHomeType(im, jm, l):
    #         return False

    varh1i = var["h1"][0]
    varh1j = var["h1"][1]
    varh2i = var["h2"][0]
    varh2j = var["h2"][1]

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == -1 and j == -1: continue
            if var["dir"] == info.HomeDir.HORIZONTAL:
                if i == 1 and j == -1: continue
            if var["dir"] == info.HomeDir.VERTICAL:
                if i == -1 and j == 1: continue

            if varh1i + i < 0 or varh1j + j < 0: continue
            if varh1i + i >= info.m or varh1j + j >= info.n: continue

            if var["dir"] == info.HomeDir.HORIZONTAL:
                # print("h")
                if (i == -1 and j == 0) or (i == 0 and j == -1) or (i == 1 and j == 0):
                    print("h-h1")
                    anotherVar = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                    if checkHomeType(varh1i + i, varh1j + j, vars, anotherVar) is checkHomeType(varh1i, varh1j, vars, var):
                        # printStack()
                        print(False)
                        return False
                
                if (i == -1 and j == 1) or (i == 1 and j == 1):
                    print("h-h2")
                    anotherVar = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                    if checkHomeType(varh1i + i, varh1j + j, vars, anotherVar) is checkHomeType(varh2i, varh2j, vars, var):
                        # printStack()
                        print(False)
                        return False

            if var["dir"] == info.HomeDir.VERTICAL:
                # print("v")
                if (i == -1 and j == 0) or (i == 0 and j == 1) or (i == 0 and j == -1):
                    print("v-h1")
                    anotherVar = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                    if checkHomeType(varh1i + i, varh1j + j, vars, anotherVar) == checkHomeType(varh1i, varh1j, vars, var):
                        # printStack()
                        print(False)
                        return False
                
                if (i == 1 and j == 1) or (i == 1 and j == -1):
                    print("v-h2")
                    anotherVar = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                    if checkHomeType(varh1i + i, varh1j + j, vars, anotherVar) == checkHomeType(varh2i, varh2j, vars, var):
                        # printStack()
                        print(False)
                        return False


            # if (i == -1 and j == 0) or (i == 0 and j == -1):        # in this situation, only h1 effects
            #     varLimitted = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
            #     if varLimitted["h1"][0] == varh1i + i and varLimitted["h1"][1] == varh1j + j:
            #         if var["value"] == [1, 0]:
            #             return False
            #         if var["value"] == [0, 1]:
            #             return False
                
            #     if varLimitted["h2"][0] == varh1i + i and varLimitted["h2"][1] == varh1j + j:
            #         if var["value"] == [1, 0]:
            #             return False
            #         if var["value"] == [0, 1]:
            #             return False
            # else:
            #     varLimitted = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
            #     if varLimitted["h1"][0] == varh1i + i and varLimitted["h1"][1] == varh1j + j:
            #         if var["value"] == [1, 0]:
            #             return False
            #         if var["value"] == [0, 1]:
            #             return False
                
            #     if varLimitted["h2"][0] == varh1i + i and varLimitted["h2"][1] == varh1j + j:
            #         if var["value"] == [1, 0]:
            #             return False
            #         if var["value"] == [0, 1]:
            #             return False
    # printStack()

    if var["dir"] == info.HomeDir.HORIZONTAL:
        if varh2j + 1 < info.n:
            anotherVar = findSpeceficVar_xy(vars, varh2i, varh2j + 1)
            type1 = checkHomeType(varh2i, varh2j + 1, vars, anotherVar)
            type2 = checkHomeType(varh2i, varh2j, vars, var)
            print(type1, type2)
            if type1 == type2:
                print(False)
                return False

    if var["dir"] == info.HomeDir.VERTICAL:
        if varh2i + 1 < info.m:
            anotherVar = findSpeceficVar_xy(vars, varh1i + 1, varh1j)
            type1 = checkHomeType(varh2i + 1, varh2j, vars, anotherVar)
            type2 = checkHomeType(varh2i, varh2j, vars, var)
            print(type1, type2)
            if type1 == type2:
               return False

    return True

def checkConstraint(var, l, d):
    im = var["h1"][0]
    jm = var["h1"][1]

    var["value"] = d

    home1 = [im, jm]
    home2 = checkHome2(i1=im, j1=jm)

    posCountColumn = 0
    negCountColumn = 0

    posCountRow = 0
    negCountRow = 0

    for i in range(info.m):
        if checkHomeType(i, jm, l, var) == info.HomeType.POSITIVE:
            posCountRow += 1

        if checkHomeType(i, jm, l, var) == info.HomeType.NEGETIVE:
            negCountRow += 1
    
    for j in range(info.n):
        if checkHomeType(im, j, l, var) == info.HomeType.POSITIVE:
            posCountColumn += 1
        
        if checkHomeType(im, j, l, var) == info.HomeType.NEGETIVE:
            negCountColumn += 1

    var["value"] = 0

    if posCountColumn > info.posColumns[jm] or posCountRow > info.posRows[im]:
        # printStack()
        return False
        
    if negCountColumn > info.negColumns[jm] or negCountRow > info.negRows[im]:
        # printStack()
        return False 

    # print(home1)
    # print(home2)

    var["value"] = d

    if not checkMagneticMatch(l, var):# or not checkMagneticMatch(home2[0], home2[1], l, var):
        # printStack()
        var["value"] = 0
        return False
    
    var["value"] = 0
    # printStack()
    return True

def assignmentComplete():
    cnt = 0
    allAssigned = True
    top:list
    
    top = list(info.vars)

    i:int

    for var in info.vars:
        if type(var["value"]) is int:
            if var["value"] == 0:
                allAssigned = False

    for i in range(len(top)):
        if type(top[i]["value"]) is list:
            cnt += 1

    # print(cnt, sum(info.posRows))

    return allAssigned

    if cnt == sum(info.posRows) and allAssigned:
        return True
    else:
        return False

def chooseVar_MRV():
    minVar:dict = {"value": -1}
    minDCount = 10

    # for var in info.vars:
    #     if type(var["value"]) is int:
    #         if var["value"] == 0:
    #             cntDomains = 3
    #             for d in var["domain"]:
    #                 if d == 0:
    #                     cntDomains -= 1

    #             if cntDomains < minDCount:
    #                 minDCount = cntDomains
    #                 minVar = var
    for l in info.vars:
        if l["value"] == 0:
            print(l["value"])
            return l

    # for var in info.vars:
    #     if var["value"] != 0:
    #         print(var["value"])
    #         continue
    #     if var["dSize"] < minDCount:
    #         minDCount = var["dSize"]
    #         minVar = var 

    # print(minVar)
    # print(minVar, minDCount)

    # return minVar

def findSpeceficVar(listSent, cnt):
    for l in listSent:
        if l["cnt"] == cnt:
            return l

def findSpeceficVar_xy(listSent, im, jm):
    for l in listSent:
        if (l["h1"][0] == im and l["h1"][1] == jm) or (l["h2"][0] == im and l["h2"][1] == jm):
            return l

def forwardChecking(var, vars):
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
            if varh1i + i >= info.m or varh1j + j >= info.n: continue

            if (i == -1 and j == 0) or (i == 0 and j == -1):        # in this situation, only h1 effects
                varLimitted = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                if varLimitted["h1"][0] == varh1i + i and varLimitted["h1"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][1] = 0
                        varLimitted["dSize"] -= 1
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][0] = 0
                        varLimitted["dSize"] -= 1
                
                if varLimitted["h2"][0] == varh1i + i and varLimitted["h2"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][0] = 0
                        varLimitted["dSize"] -= 1
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][1] = 0
                        varLimitted["dSize"] -= 1
            else:
                varLimitted = findSpeceficVar_xy(vars, varh1i + i, varh1j + j)
                if varLimitted["h1"][0] == varh1i + i and varLimitted["h1"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][0] = 0
                        varLimitted["dSize"] -= 1
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][1] = 0
                        varLimitted["dSize"] -= 1
                
                if varLimitted["h2"][0] == varh1i + i and varLimitted["h2"][1] == varh1j + j:
                    if var["value"] == [1, 0]:
                        varLimitted["domain"][1] = 0
                        varLimitted["dSize"] -= 1
                    if var["value"] == [0, 1]:
                        varLimitted["domain"][0] = 0
                        varLimitted["dSize"] -= 1


            # varLimitted = findSpeceficVar_xy(vars, i + , j)
    for l in vars:
        if l["domain"][2] != 'e':
            if sum(l["domain"]) == 0:
                print("HERE_FALSE")
                return False
    
    return True
        
def deleteFromDomain(var, v):
    for i in range(len(var["domain"])):
        if var["domain"][i] == v:
            var["domain"][i] = 0

def backingUpVars():
    for i in range(len(info.vars)):
        info.vars[i]["dSize"] = 3
        info.vars[i]["domain"] = [[0, 1], [1, 0], info.HomeType.EMPTY]

    # for i in range(len(info.vars)):
    #     forwardChecking(info.vars[i], info.vars)

def backTracking():
    if assignmentComplete():
        return True
    
    varAnalyze = chooseVar_MRV()
    # print(varAnalyze["value"])
    for d in varAnalyze["domain"]:
        if d == 0: continue

        # varAnalyze["value"] = d
        # if not type(varAnalyze["value"]) is int: continue
        # if varAnalyze["value"] == -1: continue
        print(varAnalyze["value"])
        
        if checkConstraint(varAnalyze, info.vars, d):
            # print("here")
            varAnalyze["value"] = d
            # infrences = forwardChecking(varAnalyze, info.vars)
            # print('kuh',infrences)
            # if infrences:
            resultBt = backTracking()
            if resultBt:
                return resultBt
        # varAnalyze["value"] = 0
        backingUpVars()
    return False

















def printStack():
    for l in info.vars:
        print(l)
    # print(len(info.vars))