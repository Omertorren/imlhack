def getData():
    haaretz = open("data/haaretz.csv", "r").read().split("\n")
    israelHayom = open("data/israelhayom.csv", "r").read().split("\n")
    # israelHayom=[] # todo remove
    return haaretz, israelHayom


def getWord():
    return open("data/a.txt", "r").read().split(',')
