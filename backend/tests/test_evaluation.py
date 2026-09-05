import numpy as np
from backend.core.evaluation import EvaluationEngine

def test_evaluation_metrics_mathematics():
    # 0 = Benign (Negative), 1 = Malignant (Positive)
    # Let's create a deterministic array
    # y_true: 5 Benign, 5 Malignant
    y_true = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    
    # y_pred: 
    # True Negatives (TN): 4
    # False Positives (FP): 1 (Benign predicted as Malignant)
    # False Negatives (FN): 2 (Malignant predicted as Benign)
    # True Positives (TP): 3
    y_pred = np.array([0, 0, 0, 0, 1, 0, 0, 1, 1, 1])
    
    # Probabilities for ROC-AUC
    # We assign high probability to 1s
    y_pred_proba = np.array([0.1, 0.2, 0.3, 0.4, 0.6, 0.4, 0.3, 0.7, 0.8, 0.9])
    
    metrics = EvaluationEngine.evaluate(y_true, y_pred, y_pred_proba)
    
    cm = metrics["confusion_matrix"]
    assert cm["tn"] == 4
    assert cm["fp"] == 1
    assert cm["fn"] == 2
    assert cm["tp"] == 3
    
    # Specificity = TN / (TN + FP) = 4 / 5 = 0.8
    assert np.isclose(metrics["specificity"], 0.8)
    
    # Sensitivity (Recall) = TP / (TP + FN) = 3 / 5 = 0.6
    assert np.isclose(metrics["sensitivity"], 0.6)
    
    # Accuracy = (TP + TN) / Total = 7 / 10 = 0.7
    assert np.isclose(metrics["accuracy"], 0.7)
    
    # Precision = TP / (TP + FP) = 3 / 4 = 0.75
    assert np.isclose(metrics["precision"], 0.75)
    
    # F1 = 2 * (Precision * Sensitivity) / (Precision + Sensitivity)
    # 2 * (0.75 * 0.6) / (1.35) = 0.9 / 1.35 = 0.6666...
    assert np.isclose(metrics["f1"], 0.6666666666666666)
    
    print("Metrics verified successfully!")
