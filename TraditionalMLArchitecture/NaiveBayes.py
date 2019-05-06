from TraditionalMLArchitecture.MLModel import MLModel
from sklearn.naive_bayes import GaussianNB


class NaiveBayes(MLModel):
    def __init__(self, x_train, y_train, x_test, y_test):
        super().__init__()
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.model = GaussianNB()

    def train_predict(self):
        self.model.fit(self.x_train, self.y_train)
        y_pred = self.model.predict_proba(self.x_test)  # predict_proba
        return y_pred[:,1]

    def cross_validation(self, params=None):
        pass
