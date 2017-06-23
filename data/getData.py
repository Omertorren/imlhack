def getData():
    haaretz = open("data/haaretzfinal.csv", "r").read().split("\n")
    israelHayom = open("data/israelhayom.csv","r").read().split("\n")
    return haaretz, israelHayom

def getNormalData():
    a,b = getData()
    a = [normalSentence(x) for x in a]
    b = [normalSentence(x) for x in b]
    return a,b

from bagOfWords import bagOfWords
def getAllWords():
    return bagOfWords(200).getAllWords()

def getWord():
    return open("data/a.txt", "r").read().split(',')

from bagOfWords import normalize_words
def normalSentence(sent):
    sent = sent.split(" ")
    return " ".join(normalize_words(sent))

import random
from math import floor
def getTrainingData():
    a,b = getData()
    a = [(x,0) for x in a]
    b = [(x,1) for x in b]
    allData = a+b
    random.shuffle(allData)
    size = len(allData)
    train,test,validation = floor(size*0.8), floor(size*0.1), floor(size*0.1)
    train_x, train_y = [x[0] for x in allData[0:train]], [x[1] for x in allData[0:train]]
    test_x, test_y = [x[0] for x in allData[train:train+test]], [x[1] for x in allData[train:train+test]]
    validation_x, validation_y = [x[0] for x in allData[train+test:]], [x[1] for x in allData[train+test:]]
    return (train_x, train_y), (test_x, test_y), (validation_x, validation_y)
