"""
Bag of words features extractions for IML hackathon.
Please attach stopwords.pickle with this file.
"""

import re
import numpy as np
import nltk
from nltk.stem import *
import pickle
import data.getData

# magic numbers
HAARETZ = 0
ISRAEL_HAYOM = 1


def one_time_init():
    """
    shouldnt be ran, just for our use in gathering data, and
     for the checkers to see how we aquired it.
    """
    nltk.download()
    from nltk.corpus import stopwords
    with open('stopwords.pickle', 'wb') as handle:
        pickle.dump(stopwords.words("english"),
                    handle, protocol=pickle.HIGHEST_PROTOCOL)


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
    """
    ignores the words that are irrelevant such as a, or , and, the..
    :param words: python list
    :return: python list of relevant words
    """
    ignore_us = load_stopwords("stopwords.pickle")
    return [w for w in words if not w in ignore_us]


def normalize_words(words):
    """
    stem the words into normalized form
    :param words: python list
    :return: python list of normalized words
    """
    normalized = []
    stemmer = SnowballStemmer("english")
    for word in words:
        normalized.append(stemmer.stem(word))
    return normalized


def prepare_data(path):
    with open(path, 'r') as file:
        # massaging words
        all_data_raw = file.readlines()
        all_data_raw = all_data_raw[:len(all_data_raw)*0.8]
        all_data_raw = cleanse_raw(all_data_raw)
        all_words = get_words(all_data_raw)
        all_words = ignore_irrelevant_words(all_words)
        all_words = normalize_words(all_words)
        return all_words
        # add taging:   //not needed...
        # haaretz = np.array(all_words)
        # haaretz = np.vstack((haaretz, np.zeros(haaretz.shape[0]) + HAARETZ))
        # haaretz = haaretz.transpose()


def preprocess():
    eng_dictionary = data.getData.getWord()
    haaretz = prepare_data('data/haaretz.csv')
    israel= prepare_data('data/israelhayom.csv')



def load_stopwords(path):
    """
    loads the stopwords that can be ignored.
    :param path:  usually "stopwords.pickle"
    :return:
    """
    with open(path, 'rb') as handle:
        b = pickle.load(handle)
    return b


if __name__ == "__main__":
    # print("hello bag of words , lets do this IML!!!!!!!")
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
