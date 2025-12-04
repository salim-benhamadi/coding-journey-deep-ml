import numpy as np

# Comprehensive metrics calculation solution
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    y_true = np.array(actual)
    y_pred = np.array(predicted)

    TP = np.sum((y_true == 1) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    
    confusion_matrix = [[TP, FN], [FP, TN]]
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    recall = TP / (TP + FN)
    precision = TP / (TP + FP)
    specificity = TN / (TN + FP)
    negative_predictive_value = TN / (TN + FN)
    f1_score = (2 * recall * precision) / (recall + precision)
    
    return (confusion_matrix, 
            round(accuracy, 3), 
            round(f1_score, 3), 
            round(specificity, 3), 
            round(negative_predictive_value, 3))

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(n), for converting lists to numpy arrays