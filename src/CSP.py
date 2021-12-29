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

def checkConstraint(im, jm, home):
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
    
    homeType = checkHomeType(im, jm)

    if homeType == info.HomeType.POSITIVE:
        if posCountColumn > info.posColumns[jm] or posCountRow > info.posRows[im]:
            return False

    if homeType == info.HomeType.NEGETIVE:
        if negCountColumn > info.negColumns[jm] or negCountRow > info.negRows[im]:
            return False
    
    return True

