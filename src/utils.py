import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import label_binarize

def compute_macro_auc(y_true, y_pred_proba, classes):
    """
    Computes Macro-averaged ROC-AUC score for multi-class predictions.
    BirdCLEF official evaluation metric.
    """
    y_true_bin = label_binarize(y_true, classes=classes)
    return roc_auc_score(y_true_bin, y_pred_proba, multi_class='ovr', average='macro')

def print_metrics_summary(score, metric_name="Macro ROC-AUC"):
    """
    Utility printer for evaluation metrics.
    """
    print(f"Validation {metric_name} Score: {score:.4f}")
