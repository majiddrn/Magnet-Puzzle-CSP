m:int
n:int

posRows:list
negRows:list

posColumns:list
negColumns:list

gameMap:list

posHomes:set
negHomes:set

varsStatic = []
vars = []

varsStack = []

class HomeType(enumerate):
    POSITIVE = 1
    NEGETIVE = -1
    EMPTY = 0
