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
varsCount:int

varsStack = []

class HomeDir(enumerate):
    VERTICAL = "v"
    HORIZONTAL = "h"

class HomeType(enumerate):
    POSITIVE = "p"
    NEGETIVE = "n"
    EMPTY = "e"
