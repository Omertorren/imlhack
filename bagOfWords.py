import os
import re
import numpy as np
import nltk
from nltk.stem import *
import pickle

# magic numbers
HAARETZ = 0
ISRAEL_HAYOM = 1


def cleanse_raw(data):
    """
    cleaning all irrelevant characters from data but for small letter.
    :param data: python list (CHANGES THE GIVEN DATA)
    :return: the data cleansed.
    """
    for i in range(len(data)):
        letters_only = re.sub("[^a-zA-Z]", " ", data[i])
        lower_case = letters_only.lower()
        data[i] = lower_case
    return data


def get_words(sentences):
    """
    split each sentence into words, and returns merged list
    of all words from all sentences, with duplicates.
    :param sentences: python list
    :return: python list of words (with duplicates)
    """
    words = []
    for sentence in sentences:
        words.extend(sentence.split())
    return words


def ignore_irrelevant_words(words):
    return [w for w in words if not w in stopwords.words("english")]


def normalize_words(words):
    normalized = []
    stemmer = SnowballStemmer("english")
    for word in words:
        normalize.append(stemmer.stem(word))
    return normalized


def prepare_data():
    with open("haaretz.csv", 'r') as file:
        all_data_raw = file.readlines()
        all_data_raw = cleanse_raw(all_data_raw)
        all_words = get_words(all_data_raw)
        haaretz = np.array(all_data_raw)
        haaretz = np.vstack((haaretz, np.zeros(haaretz.shape[0]) + HAARETZ))
        haaretz = haaretz.transpose()
    return haaretz
    # todo read from israel_hayom


def load_stopwords(path):
    with open(path, 'rb') as handle:
        b = pickle.load(handle)
    return b


def one_time_init():
    # nltk.download()
    from nltk.corpus import stopwords
    with open('stopwords.pickle', 'wb') as handle:
        pickle.dump(stopwords.words("english"),
                    handle, protocol=pickle.HIGHEST_PROTOCOL)



if __name__ == "__main__":
    # print("hello bag of words , lets do this IML!!!!!!!")
    print(load_stopwords('stopwords.pickle'))
    print()
    print(get_words(cleanse_raw(['aa aa aa!'])))
    train = prepare_data()



    # OLD CODE:   todo delete
    # import pandas as pd
    # train = pd.read_csv("haaretz.csv")
    # train["news"] = HAARETZ
    # print(train.shape)
    # print(train.columns.values)
    # print(train[0][1])
