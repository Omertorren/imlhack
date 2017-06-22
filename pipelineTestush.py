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
pipe = Pipeline([('vect', CountVectorizer(stop_words="english", analyzer="word", max_features=5000)),
                      ('tfidf', TfidfTransformer()),
                      ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-5, n_iter=5, random_state=42))])

pipe = Pipeline([('vect', CountVectorizer(stop_words="english", analyzer="word", max_features=5000)),
                      ('tfidf', TfidfTransformer()),
                      ('clf', MultinomialNB())])

a,b,c = getTrainingData()
_ = pipe.fit(a[0],a[1])
predicted = pipe.predict(b[0])
print(np.mean(predicted == b[1]))
predicted = pipe.predict(c[0])
print(np.mean(predicted == c[1]))