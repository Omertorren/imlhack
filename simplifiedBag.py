#  TODO need to download
# import nltk
# nltk.download()
#
from nltk.corpus import words


# todo delete.
def get_data():
    return [], []


def cleanse_raw(lst):
    return []

word_list = words.words()
dictionary = dict(words.words())
for word in word_list:
    dictionary[word] = 0

haaretz_list, israel_list = get_data()
for sentence in haaretz_list
