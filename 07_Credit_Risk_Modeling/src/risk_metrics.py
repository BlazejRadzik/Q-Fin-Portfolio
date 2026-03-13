from sklearn.metrics import roc_auc_score

class RiskValidator:
    """Calculates banking-specific validation metrics."""
    @staticmethod
    def calculate_gini(y_true, y_probs) -> float:
        """Standard Gini Coefficient for scorecard performance: 2*AUC - 1"""
        auc = roc_auc_score(y_true, y_probs)
        return 2 * auc - 1