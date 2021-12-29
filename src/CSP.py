import info

def addPos(im, jm):
    info.posHomes.add([im, jm])

def addNeg(im, jm):
    info.negHomes.add([im, jm])

def checkHomeType(im, jm):
    if [im, jm] in info.posHomes:
        return info.HomeType.POSITIVE
    if [im, jm] in info.negHomes:
        return info.HomeType.NEGETIVE
    return info.HomeType.EMPTY

def checkHome2(i1, j1):
    if i1 != info.m - 1:
        if info.gameMap[i1, j1] == info.gameMap[i1 + 1, j1]:
            return [i1 + 1, j1]
    
    if j1 != info.n - 1:
        if info.gameMap[i1, j1] == info.gameMap[i1, j1 + 1]:
            return [i1, j1 + 1]

def checkMagneticMatch(im, jm):
    if im != 0:
        if checkHomeType(im - 1, jm) == checkHomeType(im, jm):
            return False

    if im != info.m - 1:
        if checkHomeType(im + 1, jm) == checkHomeType(im, jm):
            return False

    if jm != 0:
        if checkHomeType(im, jm - 1) == checkHomeType(im, jm):
            return False
    
    if jm != info.n - 1:
        if checkHomeType(im, jm + 1) == checkHomeType(im, jm):
            return False

    return True

def checkConstraint(im, jm):
    home1 = [im, jm]
    home2 = checkHome2(i1=im, j1=jm)

    posCountColumn = 0
    negCountColumn = 0

    posCountRow = 0
    negCountRow = 0

    for i in range(info.m):
        if checkHomeType(i, jm) == info.HomeType.POSITIVE:
            posCountColumn += 1

        if checkHomeType(i, jm) == info.HomeType.NEGETIVE:
            negCountColumn += 1
    
    for j in range(info.n):
        if checkHomeType(im, j) == info.HomeType.POSITIVE:
            posCountRow += 1
        
        if checkHomeType(im, j) == info.HomeType.NEGETIVE:
            negCountRow += 1

    if posCountColumn > info.posColumns[jm] or posCountRow > info.posRows[im]:
        return False
        
    if negCountColumn > info.negColumns[jm] or negCountRow > info.negRows[im]:
        return False 

    if not checkMagneticMatch(home1[0], home1[1]) or not checkMagneticMatch(home2[0], home2[1]):
        return False

    return True

def assignmentComplete():
    cnt = 0

    for var in info.vars:
        if len(var["value"]) == 2:
            cnt += 1

    if cnt == sum(info.posRows):
        return True
    else:
        return False

# def chooseVar():


def backTracking():
    if assignmentComplete():
        return True
    
    # varAnalyze = chooseVar()
