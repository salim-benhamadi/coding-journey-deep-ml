import numpy as np

# Confusion matrix solution
def accuracy_score(y_true, y_pred):
    TP = np.sum((y_pred == 1) & (y_true == 1))
    TN = np.sum((y_pred == 0) & (y_true == 0))
    FP = np.sum((y_pred == 1) & (y_true == 0))
    FN = np.sum((y_pred == 0) & (y_true == 1))

    return (TP + TN) / (TP + TN + FP + FN)

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(1), only using constant extra space


# Direct comparison solution
def accuracy_score(y_true, y_pred):
    correct_predictions = np.sum(y_true == y_pred)
    total_samples = len(y_true)
    return correct_predictions / total_samples

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(1), only using constant extra space