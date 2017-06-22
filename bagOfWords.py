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
import operator

# magic numbers
HAARETZ = 0
ISRAEL_HAYOM = 1


class bagOfWords:
    def __init__(self):
        haaretz = self.prepare_data('data/haaretz.csv', False)
        israel = self.prepare_data('data/israelhayom.csv', False)
        majors = self.find_majors(300, haaretz, israel)
        haaretz_avg, israel_avg = self.find_average_word_length()

    def generate_maj_features(self, sentence):
        features_vec = np.zeros(len(self.majors))
        table = {}
        for i in range(len(self.majors)):
            table[majors] = i
        for word in sentence.split():
            if word in majors:
                features_vec[table[word]] += 1
        max_w = np.max(features_vec)
        if max_w != 0:
            features_vec /= max_w
        return list(features_vec)

    def generate_word_len_avg_feature(self, sentence):
        avg = 0
        count = 0
        for word in sentence:
            avg += len(word)
            count += 1
        if count != 0:
            avg /= count
        return list(avg)

    def cleanse_raw(self, data):
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

    def get_words(self, sentences):
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

    def ignore_irrelevant_words(self, words):
        """
        ignores the words that are irrelevant such as a, or , and, the..
        :param words: python list
        :return: python list of relevant words
        """
        ignore_us = self.load_stopwords("stopwords.pickle")
        return [w for w in words if not w in ignore_us]

    def normalize_words(self, words):
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

    def prepare_data(self, path, stem):
        with open(path, 'r') as file:
            # massaging words
            all_data_raw = file.readlines()
            all_data_raw = all_data_raw[:int(np.floor(len(all_data_raw) * 0.8))]
            all_data_raw = self.cleanse_raw(all_data_raw)
            all_words = self.get_words(all_data_raw)
            all_words = self.ignore_irrelevant_words(all_words)
            if (stem):
                all_words = self.normalize_words(all_words)
            return all_words
            # add taging:   //not needed...
            # haaretz = np.array(all_words)
            # haaretz = np.vstack((haaretz, np.zeros(haaretz.shape[0]) + HAARETZ))
            # haaretz = haaretz.transpose()

    def find_majors(self, n, haaretz, israel_hayom):
        table = {}
        for word in haaretz:
            if word in table:
                table[word] += 1
            else:
                table[word] = 1
        for word in israel_hayom:
            if word in table:
                table[word] += 1
            else:
                table[word] = 1
        sorted_maj = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
        sorted_maj = sorted_maj[:n]
        majors = [w[0] for w in sorted_maj]
        return majors

    def find_average_word_length(self, haaretz, israel_hayom):
        avg_haaretz = 0
        count = 0
        for word in haaretz:
            avg_haaretz += len(word)
            count += 1
        if count != 0:
            avg_haaretz /= count
        avg_israel = 0
        count = 0
        for word in israel_hayom:
            avg_israel += len(word)
            count += 1
        if count != 0:
            avg_israel /= count
        return avg_haaretz, avg_israel

    def load_stopwords(self, path):
        """
        loads the stopwords that can be ignored.
        :param path:  usually "stopwords.pickle"
        :return:
        """
        with open(path, 'rb') as handle:
            b = pickle.load(handle)
        return b


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


if __name__ == "__main__":
    # print("hello bag of words , lets do this IML!!!!!!!")
    print()
    print(get_words(cleanse_raw(['aa aa aa!'])))
    haaretz = prepare_data('data/haaretz.csv', False)
    israel = prepare_data('data/israelhayom.csv', False)
    majors = find_majors(300, haaretz, israel)




    # OLD CODE:   todo delete
    # import pandas as pd
    # train = pd.read_csv("haaretz.csv")
    # train["news"] = HAARETZ
    # print(train.shape)
    # print(train.columns.values)
    # print(train[0][1])
