m:int
n:int

gameMap:list

vars = []
varsStatic = []

posRows:list
negRows:list

posColumns:list
negColumns:list

gameMapUpdate:list

class HomeDir(enumerate):
    VERTICAL = "v"
    HORIZONTAL = "h"

class HomeType(enumerate):
    POSITIVE = "p"
    NEGETIVE = "n"
    EMPTY = "e"
    NOT_ASSIGNED = "na"