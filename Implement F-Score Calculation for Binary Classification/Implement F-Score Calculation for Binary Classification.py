import numpy as np

# Confusion matrix solution
def f_score(y_true, y_pred, beta):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    
    if TP + FN == 0 or TP + FP == 0:
        return 0.0
    
    recall = TP / (TP + FN)
    precision = TP / (TP + FP)
    
    if recall + beta**2 * precision == 0:
        return 0.0
    
    f_score_value = ((1 + beta**2) * recall * precision) / (recall + beta**2 * precision)
    
    return round(f_score_value, 3)

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(1), only using constant extra space