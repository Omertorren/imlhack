# #  TODO need to download
# import nltk
# nltk.download()

#
from data.getData import *
from  bagOfWords import *
from nltk.stem import *
import sys

weights = {}
mids = 0


def sentence_into_list_of_words(sentece, stemmer):
    lst = sentece.split(" ")
    # todo remove shit words.
    for i in range(len(lst)):
        lst[i] = stemmer.stem(lst[i])
    return lst


def counter_for_dictionary(lst, val, stemmer):
    for sentence in lst:
        temp = sentence_into_list_of_words(sentence, stemmer)
        for wrd in temp:
            if wrd not in weights:
                weights[wrd] = val
            else:
                weights[wrd] += val


def normalize_weights():
    max = -sys.maxsize
    temp = 0
    for key in weights:
        temp = abs(weights[key])
        if temp > max:
            max = temp
    for key in weights:
        weights[key] = weights[key] / max
        weights[key] = (weights[key] + 1) / 2


def sentence_sum_feature(sentence):
    nsentence = cleanse_raw([sentence])
    nsentence = normalize_words((get_words(nsentence)))
    sum = 0
    for wrd in nsentence:
        if wrd in weights:
            sum += weights[wrd]
    return [sum]


def _get_length(sentence):
    nsentence = cleanse_raw([sentence])
    nsentence = normalize_words((get_words(nsentence)))
    return len(sentence)


def avarage_length(data1, data2):
    len1 = 0
    len2 = 0
    for sentence in data1:
        len1 += len(normalize_words(get_words(cleanse_raw([sentence]))))
    len1 = len1 / len(data1)

    for sentence in data2:
        len2 += len(normalize_words(get_words(cleanse_raw([sentence]))))
    len2 = len2 / len(data2)
    return len1, len2


def j_init():
    stemmer = SnowballStemmer("english")
    word_list = getWord()
    word_list = normalize_words((word_list))

    weight = dict()
    for word in word_list:
        weight[word] = 0

    haaretz_list, israel_hayom_list = getData()
    print(len(haaretz_list), len(israel_hayom_list))
    # cleaning out bad words.
    haaretz_list = (cleanse_raw(haaretz_list))
    israel_hayom_list = (cleanse_raw(israel_hayom_list))

    # gathering validation
    h_validate = haaretz_list[int((len(haaretz_list) / 10) * 8):]
    i_validate = israel_hayom_list[int((len(israel_hayom_list) / 10) * 8):]
    # train set
    h_train = haaretz_list[:int((len(haaretz_list) / 10) * 8)]
    i_train = israel_hayom_list[:int((len(israel_hayom_list) / 10) * 8)]

    # starting with 1 for haaretz today.
    counter_for_dictionary(i_train, 1, stemmer)
    counter_for_dictionary(h_train, -1, stemmer)
    normalize_weights()
    ilen, hlen = avarage_length(i_train, h_train)
    mids = (ilen + hlen) / 2
#######
    h_count = 0
    h_half = 0
    h_wrong = 0
    for i in h_validate:
        val = sentence_sum_feature(i)[0]
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
        val = sentence_sum_feature(j)[0]
        if val > 0.5:
            i_count += 1
        elif val == 0.5:
            i_half += 1
        elif val < 0.5:
            i_wrong += 1

    print("rights  |overallsize |wrongs|   non-dicidable")
    print(i_count, "   ", len(i_validate), "         ", i_wrong, "    ", i_half)
    print(h_count, "   ", len(h_validate), "         ", h_wrong, "    ", h_half)
    return weight, mids


def sentence_len_feature(sentence):
    sentence = cleanse_raw([sentence])
    sentence = normalize_words(get_words(sentence))
    sent_len = len(sentence)
    if sent_len > mids:
        return [0]
    elif sent_len < mids:
        return [1]
    else:
        return [0]

        # stemmer = SnowballStemmer("english")
        # word_list = getWord()
        # word_list = normalize_words((word_list))
        #
        # weight = dict()
        # for word in word_list:
        #     weight[word] = 0
        #
        # haaretz_list, israel_hayom_list = getData()
        # print(len(haaretz_list), len(israel_hayom_list))
        # # cleaning out bad words.
        # haaretz_list = (cleanse_raw(haaretz_list))
        # israel_hayom_list = (cleanse_raw(israel_hayom_list))
        #
        # # gathering validation
        # h_validate = haaretz_list[int((len(haaretz_list) / 10) * 8):]
        # i_validate = israel_hayom_list[int((len(israel_hayom_list) / 10) * 8):]
        # # train set
        # h_train = haaretz_list[:int((len(haaretz_list) / 10) * 8)]
        # i_train = israel_hayom_list[:int((len(israel_hayom_list) / 10) * 8)]
        #
        # # starting with 1 for haaretz today.
        # counter_for_dictionary(i_train, 1, weight)
        # counter_for_dictionary(h_train, -1, weight)
        # normalize_weights(weight)
        #
        # h_count = 0
        # h_half = 0
        # h_wrong = 0
        # for i in h_validate:
        #     val = compute_sum(i, weight)[0]
        #     if val < 0.5:
        #         h_count += 1
        #     elif val == 0.5:
        #         h_half += 1
        #     elif val > 0.5:
        #         h_wrong += 1
        #
        # i_count = 0
        # i_half = 0
        # i_wrong = 0
        # for j in i_validate:
        #     val = compute_sum(j, weight)[0]
        #     if val > 0.5:
        #         i_count += 1
        #     elif val == 0.5:
        #         i_half += 1
        #     elif val < 0.5:
        #         i_wrong += 1


if __name__ == '__main__':
    j_init()

# for j in i_validate:
#
# print("rights  |overallsize |wrongs|   non-dicidable")
# print(i_count, "   ", len(i_validate), "         ", i_wrong, "    ", i_half)
# print(h_count, "   ", len(h_validate), "         ", h_wrong, "    ", h_half)

###### avg length  :
# for j in i_train:
#     print()
