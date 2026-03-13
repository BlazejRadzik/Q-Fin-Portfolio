from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

class ProbabilityOfDefaultModel:
    """
    Institutional engine for estimating Probability of Default (PD) 
    using Regularized Logistic Regression.
    """
    def __init__(self, c_parameter: float = 0.1):
        self.model = LogisticRegression(C=c_parameter, penalty='l2', solver='lbfgs')

    def fit_model(self, X, y):
        """Trains the model on historical default data."""
        self.model.fit(X, y)
        joblib.dump(self.model, 'pd_model_v1.pkl')

    def estimate_pd(self, X_input) -> np.ndarray:
        """Returns the estimated probability of default [0, 1]."""
        return self.model.predict_proba(X_input)[:, 1]