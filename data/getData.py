def getData():
    haaretz = open("haaretz.csv", "r").read().split("\n")
    israelHayom = open("israelhayom.csv","r").read().split("\n")
    return haaretz, israelHayom