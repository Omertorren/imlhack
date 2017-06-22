import os
import re
import numpy as np

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
        letters_only = re.sub("[^a-zA-Z]", "", data[i])
        lower_case = letters_only.lower()
        data[i] = lower_case
    return data


def prepare_data():
    with open("haaretz.csv", 'r') as file:
        all_data_raw = file.readlines()
        cleanse_raw(all_data_raw)
        haaretz = np.array(all_data_raw)
        haaretz = np.vstack((haaretz, np.zeros(haaretz.shape[0]) + HAARETZ))
        haaretz = haaretz.transpose()
    return haaretz
    # todo read from israel_hayom


if __name__ == "__main__":
    print("hello bag of words , lets do this IML!!!!!!!")
    train = prepare_data()



    # OLD CODE:   todo delete
    # import pandas as pd
    # train = pd.read_csv("haaretz.csv")
    # train["news"] = HAARETZ
    # print(train.shape)
    # print(train.columns.values)
    # print(train[0][1])
