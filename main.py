from data.getData import *
from bagOfWords import *
from simplifiedBag import *
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from omerBestFeatures import *
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier, ExtraTreeRegressor
import numpy as np
from sklearn.pipeline import Pipeline
bg = bagOfWords(1000)
foos = [bg.generate_maj_features, bg.generate_word_len_avg_feature, sentence_len_feature, myBag]
foos = [myBag]
initFoos = [j_init]
models = ["SVCSpecial","SVC", "LinearSVC", "LinearSVR","NuSCR","NuSVC", "TreeRegress","TreeClass","ExTreeClass","ExTreeRegress"]
algos = [
        MultinomialNB()
         # svm.SVC(gamma=0.01,C=10,kernel='poly'),
         # svm.SVC(),
         # svm.LinearSVC(),
         # svm.NuSVC(),
         # DecisionTreeRegressor(random_state=0),
         # DecisionTreeClassifier(random_state=0),
         # ExtraTreeClassifier(random_state=0),
         # ExtraTreeRegressor(random_state=0)
]

def getElems():
    tr,te,val = getTrainingData()
    tr = [sentToFeat(x) for x in tr[0]], tr[1]
    te = [sentToFeat(x) for x in te[0]], te[1]
    val = [sentToFeat(x) for x in val[0]], val[1]
    return tr, te, val


def sentToFeat(sent):
    for foo in foos:
        x = foo(sent)
    return x

def modelSelection():
    tr,te,val = getElems()
    print("##### Vectors Created ######")
    x,y = tr
    xx,yy = te
    xxx,yyy = val
    i = 1
    for algo in algos:
        print ("##### Running model number %s we are on %s ######"%(i, models[i-1]))
        clf = algo.fit(x,y)
        pred = algo.predict(xx)
        scores = sum([0 if circ(pred[i]) == yy[i] else 1 for i in range(len(pred))]) / len(pred)
        print("Score for test data%s"%scores)

        pred = algo.predict(xxx)
        scores = sum([0 if circ(pred[i]) == yyy[i] else 1 for i in range(len(pred))]) / len(pred)
        print("Score for test data%s" % scores)
        i+=1

def init():
    for foo in initFoos:
        foo()
    print("##### INIT Completed ######")

# circ = lambda x:1 if x>0.5 else 0
# init()
# modelSelection()

