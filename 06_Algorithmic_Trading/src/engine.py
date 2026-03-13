from sklearn.linear_model import LogisticRegression
import joblib

class ProbabilityOfDefaultModel:
    """Institutional-grade PD Model using Regularized Logistic Regression."""
    def __init__(self, c_parameter: float = 0.1):
        self.model = LogisticRegression(C=c_parameter, penalty='l2', solver='lbfgs')

    def fit(self, X, y):
        self.model.fit(X, y)
        joblib.dump(self, 'pd_model_v1.pkl')

    def predict_pd(self, X_input) -> float:
        """Returns the Probability of Default (PD) as a decimal."""
        # Index [1] for the positive class (Default)
        return self.model.predict_proba(X_input)[:, 1]