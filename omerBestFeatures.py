from data.getData import *
from bagOfWords import bagOfWords
from sklearn.feature_extraction.text import CountVectorizer

words = bagOfWords(200).getAllWords()
vec = CountVectorizer()
x = vec.fit_transform(words)
max = max(list(x.indices))

def myBag(s):
    a = list([x/max for x in vec.transform([s]).indices])
    return a