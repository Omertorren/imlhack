from data.getData import *
from bagOfWords import *
from simplifiedBag import *
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier, ExtraTreeRegressor
bg = bagOfWords(1000)
foos = [bg.generate_maj_features, bg.generate_word_len_avg_feature, sentence_len_feature]
initFoos = [j_init]
models = ["SVCSpecial","SVC", "LinearSVC", "LinearSVR","NuSCR","NuSVC", "TreeRegress","TreeClass","ExTreeClass","ExTreeRegress"]
algos = [
        # svm.SVC(probability=True, random_state=0),
         # svm.SVC(),
         # svm.LinearSVC(),
         # svm.NuSVC(),
         DecisionTreeRegressor(random_state=0),
         DecisionTreeClassifier(random_state=0),
         ExtraTreeClassifier(random_state=0),
         ExtraTreeRegressor(random_state=0)]

def getElems():
    tr,te,val = getTrainingData()
    tr = [sentToFeat(x) for x in tr[0]], tr[1]
    te = [sentToFeat(x) for x in te[0]], te[1]
    val = [sentToFeat(x) for x in val[0]], val[1]
    return tr, te, val


def sentToFeat(sent):
    x = []
    for foo in foos:
        x += foo(sent)
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
        algo.fit(x,y)
        pred = algo.predict(te[0])
        scores = sum([0 if circ(pred[i]) == y[i] else 1 for i in range(len(pred))]) / len(pred)
        print(scores)
        i+=1

def init():
    for foo in initFoos:
        foo()
    print("##### INIT Completed ######")

circ = lambda x:1 if x>0.5 else 0
init()
modelSelection()
