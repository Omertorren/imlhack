# #  TODO need to download
# import nltk
# nltk.download()

#
from data.getData import *
from  bagOfWords import *
from nltk.stem import *
import sys


#

def sentence_into_list_of_words(sentece, stemmer):
    lst = sentece.split(" ")
    # todo remove shit words.
    for i in range(len(lst)):
        lst[i] = stemmer.stem(lst[i])
    return lst


def counter_for_dictionary(lst, val, dictionary):
    for sentence in lst:
        temp = sentence_into_list_of_words(sentence, stemmer)
        for wrd in temp:
            if wrd not in dictionary:
                dictionary[wrd] = val
            else:
                dictionary[wrd] += val


def normalize_weights(weight):
    max = -sys.maxsize
    temp = 0
    for key in weight:
        temp = abs(weight[key])
        if temp > max:
            max = temp
    for key in weight:
        weight[key] = weight[key] / max
        weight[key] = (weight[key] + 1) / 2


def compute_sum(sentence, dictionary):
    nsentence = cleanse_raw([sentence])
    nsentence = normalize_words(ignore_irrelevant_words(get_words(nsentence)))
    sum = 0
    for wrd in nsentence:
        if wrd in dictionary:
            # print(dictionary[wrd])
            # sum += (dictionary[wrd] + 1) / 2
            sum = dictionary[wrd]
    return [sum]


def compute_length(sentence):
    nsentence = cleanse_raw([sentence])
    nsentence = normalize_words(ignore_irrelevant_words(get_words(nsentence)))
    return len(sentence)


if __name__ == '__main__':
    stemmer = SnowballStemmer("english")
    word_list = getWord()
    word_list = normalize_words(ignore_irrelevant_words(word_list))

    weight = dict()
    for word in word_list:
        weight[word] = 0

    haaretz_list, israel_hayom_list = getData()
    # cleaning out bad words.
    haaretz_list = ignore_irrelevant_words(cleanse_raw(haaretz_list))
    israel_hayom_list = ignore_irrelevant_words(cleanse_raw(israel_hayom_list))

    # gathering validation
    h_validate = haaretz_list[int((len(haaretz_list) / 10) * 8):]
    i_validate = israel_hayom_list[int((len(israel_hayom_list) / 10) * 8):]
    # train set
    h_train = haaretz_list[:int((len(haaretz_list) / 10) * 8)]
    i_train = israel_hayom_list[:int((len(israel_hayom_list) / 10) * 8)]

    # starting with 1 for haaretz today.
    counter_for_dictionary(i_train, 1, weight)
    counter_for_dictionary(h_train, -1, weight)
    normalize_weights(weight)

    h_count = 0
    h_half = 0
    h_wrong = 0
    for i in h_validate:
        val = compute_sum(i, weight)[0]
        if val < 0.5:
            h_count += 1
        elif val == 0.5:
            h_half += 1
        elif val > 0.5:
            h_wrong += 1

    i_count = 0
    i_half = 0
    i_wrong = 0
    for j in i_validate:
        val = compute_sum(j, weight)[0]
        if val > 0.5:
            i_count += 1
        elif val == 0.5:
            i_half += 1
        elif val < 0.5:
            i_wrong += 1

    for j in i_validate:

    print("rights  |overallsize |wrongs|   non-dicidable")
    print(i_count, "   ", len(i_validate), "         ", i_wrong, "    ", i_half)
    print(h_count, "   ", len(h_validate), "         ", h_wrong, "    ", h_half)
