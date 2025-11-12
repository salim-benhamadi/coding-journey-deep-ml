import numpy as np

# Confusion matrix solution
def precision(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    
    if TP + FP == 0:
        return 0.0
    
    return round(TP / (TP + FP), 3)

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(1), only using constant extra space