from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator

from sklearn.decomposition import FastICA

class Classifier(BaseEstimator):
    def __init__(self):
        self.n_components = 10
        self.clf = Pipeline([
            ('fica', FastICA(n_components=self.n_components)),
            ('clf', SVC(C = 100, gamma = 8, probability = True))
        ])

    def fit(self, X, y):
        self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)

    def predict_proba(self, X):
        return self.clf.predict_proba(X)

