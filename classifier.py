"""
===================================================
     Introduction to Machine Learning (67577)
             IML HACKATHON, June 2017

            **  Headline Classifier  **

Author(s):  Omer Shacham, Neriya Ochana, Jonathan Weiss, Ron Urbach

===================================================
"""
import finalPy

HAARETZ = 0
ISRAEL_HAYOM = 1


class Classifier(object):
    """
    Recieves a list of m unclassified headlines, and predicts for each one which
     newspaper published it.
    :param X: A list of length m containing the headlines' texts (strings)
    :return: y_hat - a binary vector of length m
    """

    def classify(self, X):
        y_hat = []
        predictor = finalPy.modelGever()
        for headline in X:
            y.append(predictor.evaluate(headline)[0])
        return y_hat
