import numpy as np

# Array manipulation solution
def confusion_matrix(data):
    y_true, y_pred = np.array(data)[:, 0], np.array(data)[:, 1]
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    return [[TP, FN], [FP, TN]]

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(n), for storing y_true and y_pred arrays