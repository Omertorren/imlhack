import dill as pickle
from sklearn.externals import joblib

_digits_to_ints_d = {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def _title_normalizer(s):
  normalized = []
  for w in s.split(' '):
    word = w.lower()
    if word in _digits_to_ints_d:
      normalized.append(str(_digits_to_ints_d[word]))
    else:
      normalized.append(w)
  return ' '.join(normalized)


class modelGever():
    def __init__(self):
        # self.mdl = pickle.load(open("fmdl.pkl","rb"))
        pipename = "pipe.mdl"
        filename = "model.mdl"
        # self.wrds = self.mdl()
        self.pipe = joblib.load(pipename)
        self.svr = joblib.load(filename)

    def evaluate(self,sent):
        p = self.pipe.transform([_title_normalizer(sent)])
        predict = self.svr.predict(p)
        # k = True in list(map(lambda x:sent in x, self.wrds))
        return predict
