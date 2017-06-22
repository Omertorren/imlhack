from data.getData import *
from bagOfWords import *
from sklearn.model_selection import cross_val_score
from sklearn import svm, datasets
bg = bagOfWords()
foos = [bg.generate_maj_features, bg.generate_word_len_avg_feature]
init = []
algos = [svm.SVC(probability=True, random_state=0),
         svm.SVC(),
         svm.LinearSVC(),
         svm.LinearSVR(),
         svm.NuSVR(),
         svm.NuSVC()]

def getElems():
    tr,te,val = getTrainingData()
    tr = [sentToFeat(x) for x in tr[0]], tr[1]
    te = [sentToFeat(x) for x in te[0]], te[1]
    val = [sentToFeat(x) for x in val[0]], val[1]
    return tr, te, val


def sentToFeat(sent):
    x = []
    print(sent)
    for foo in foos:
        x += foo(sent)
    return x

def modelSelection():
    tr,te,val = getElems()
    x,y = tr
    xx,yy = te
    xxx,yyy = val
    for algo in algos:
        algo.fit(x,y)
        cross_val_score(algo,xx,yy,scoring="accuracy")


modelSelection()
