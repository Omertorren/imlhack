from sklearn.linear_model import SGDClassifier
from data.getData import *
from bagOfWords import *
from simplifiedBag import *
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from omerBestFeatures import *
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import *

pipe = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      ])
svr = GridSearchCV(SGDClassifier(),
                   param_grid={"alpha":[0.0001],
                               "loss":["log"],
                               "penalty":["l2"]})

from sklearn.externals import joblib
# save the classifier

a,b,c = getTrainingData()
# x = pipe.fit_transform(a[0],a[1])
# svr.fit(x,a[1])
pipename = "pipe.mdl"
filename = "model.mdl"
pipe = joblib.load(pipename)
svr = joblib.load(filename)
predicted = svr.predict(pipe.transform(b[0]))
predicted[predicted > 0.5] = 1
predicted[predicted <= 0.5] = 0
print(np.mean(predicted == b[1]))
predicted = svr.predict(pipe.transform(c[0]))
predicted[predicted > 0.5] = 1
predicted[predicted <= 0.5] = 0
print(np.mean(predicted == c[1]))
strt = "Terrorist kills 13-year-old in her bedroom in Kiryat Arba"
k = pipe.transform([strt])
print(svr.predict(k))
# joblib.dump(pipe,pipename,compress=9)
# joblib.dump(svr,filename,compress=9)