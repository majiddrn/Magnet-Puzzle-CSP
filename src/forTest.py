import CSP
import info

l = []

var = {"cnt": 1, "h1": [1, 2], "h2": [2, 2], "dir": info.HomeDir.VERTICAL
                            , "domain": [[0, 1], [1, 0], info.HomeType.EMPTY], "dSize": 3,"value": 0}

print(CSP.checkHomeType(2, 2, [], var))