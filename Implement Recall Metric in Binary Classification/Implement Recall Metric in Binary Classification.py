import numpy as np

# Confusion matrix solution
def recall(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    
    if TP + FN == 0:
        return 0.0
    
    return round(TP / (TP + FN), 3)

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(1), only using constant extra space