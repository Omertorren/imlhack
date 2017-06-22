from sklearn.linear_model import SGDClassifier
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
from sklearn.model_selection import GridSearchCV


pipe = Pipeline([('vect', CountVectorizer(stop_words="english", analyzer="word", max_features=5000)),
                      ('tfidf', TfidfTransformer()),
                      ])
svr = GridSearchCV(MultinomialNB(class_prior=None, fit_prior=True), cv=5,
                   param_grid={"alpha": [0.2,0.5,1.0]})


a,b,c = getTrainingData()
x = pipe.fit_transform(a[0],a[1])
svr.fit(x,a[1])
print(svr.best_estimator_, svr.best_params_)
predicted = svr.predict(pipe.transform(b[0]))
print(np.mean(predicted == b[1]))
predicted = svr.predict(pipe.transform(c[0]))
print(np.mean(predicted == c[1]))