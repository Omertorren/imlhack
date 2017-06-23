import dill as pickle
import time
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import *
from sklearn.externals import joblib



class modelGever():
    def __init__(self):
        self.mdl = pickle.load(open("fmdl.pkl","rb"))
        pipename = "pipe.mdl"
        filename = "model.mdl"
        self.pipe = joblib.load(pipename)
        self.svr = joblib.load(filename)

    def evaluate(self,sent):
        p = self.pipe.transform(sent)
        predict = self.svr.predict([p])
        return predict
