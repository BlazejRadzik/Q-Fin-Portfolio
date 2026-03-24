import joblib
from sklearn.linear_model import LogisticRegression


class ProbabilityOfDefaultModel:
    def __init__(self, c_parameter: float = 0.1):
        self.model = LogisticRegression(C=c_parameter, penalty="l2", solver="lbfgs")

    def fit(self, X, y):
        self.model.fit(X, y)
        joblib.dump(self, "pd_model_v1.pkl")

    def predict_pd(self, X_input):
        return self.model.predict_proba(X_input)[:, 1]
