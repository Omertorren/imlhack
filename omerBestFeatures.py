from data.getData import *
from bagOfWords import bagOfWords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

words = bagOfWords(200).getAllWords()
vec = CountVectorizer()
tvec = TfidfTransformer(use_idf=False)
x = vec.fit_transform(words)
tvec.fit(x)
max = max(list(x.indices))

def myBag(s):
    t = vec.transform(s.split(" "))
    a = tvec.transform(t)
    return a