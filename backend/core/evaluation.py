from typing import Dict, Any
from sklearn.metrics import (
    accuracy_score,
    recall_score,
    precision_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
import numpy as np

class EvaluationEngine:
    @staticmethod
    def compute_specificity(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """TN / (TN + FP)"""
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
        if (tn + fp) == 0:
            return 0.0
        return tn / (tn + fp)
        
    @staticmethod
    def evaluate(y_true: np.ndarray, y_pred: np.ndarray, y_pred_proba: np.ndarray = None) -> Dict[str, Any]:
        """
        Calculates required experiment metrics.
        Assumes binary classification where Positive Class = 1.
        """
        metrics = {}
        metrics["accuracy"] = float(accuracy_score(y_true, y_pred))
        metrics["sensitivity"] = float(recall_score(y_true, y_pred, pos_label=1))
        metrics["specificity"] = float(EvaluationEngine.compute_specificity(y_true, y_pred))
        metrics["precision"] = float(precision_score(y_true, y_pred, pos_label=1, zero_division=0))
        metrics["f1"] = float(f1_score(y_true, y_pred, pos_label=1))
        
        if y_pred_proba is not None:
            # Handle binary case where predict_proba returns shape (n_samples, 2)
            if y_pred_proba.ndim == 2 and y_pred_proba.shape[1] == 2:
                y_prob_pos = y_pred_proba[:, 1]
            else:
                y_prob_pos = y_pred_proba
            metrics["roc_auc"] = float(roc_auc_score(y_true, y_prob_pos))
        else:
            metrics["roc_auc"] = None
            
        cm = confusion_matrix(y_true, y_pred).ravel()
        # cm is [tn, fp, fn, tp]
        metrics["confusion_matrix"] = {
            "tn": int(cm[0]),
            "fp": int(cm[1]),
            "fn": int(cm[2]),
            "tp": int(cm[3])
        }
        
        return metrics
