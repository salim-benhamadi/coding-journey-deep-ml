# Calculate Performance Metrics for a Classification Model

## Problem Statement

In this task, you are required to implement a function `performance_metrics(actual, predicted)` that computes various performance metrics for a binary classification problem. These metrics include:

* Confusion Matrix
* Accuracy
* F1 Score
* Specificity
* Negative Predictive Value

The function should take in two lists:
* `actual`: The actual class labels (1 for positive, 0 for negative)
* `predicted`: The predicted class labels from the model

## Input
* `actual`: A list of integers (0 or 1) representing true labels
* `predicted`: A list of integers (0 or 1) representing predicted labels

## Output
A tuple containing:
1. `confusion_matrix`: A 2x2 matrix as `[[TP, FN], [FP, TN]]`
2. `accuracy`: A float (rounded to 3 decimals)
3. `f1_score`: A float (rounded to 3 decimals)
4. `specificity`: A float (rounded to 3 decimals)
5. `negative_predictive_value`: A float (rounded to 3 decimals)

## Constraints
* All elements in the `actual` and `predicted` lists must be either 0 or 1
* Both lists must have the same length

## Examples

### Example 1:
```
Input:
actual = [1, 0, 1, 0, 1]
predicted = [1, 0, 0, 1, 1]

Output:
([[2, 1], [1, 1]], 0.6, 0.667, 0.5, 0.5)

Reasoning:
Index 0: actual=1, pred=1 → TP
Index 1: actual=0, pred=0 → TN
Index 2: actual=1, pred=0 → FN
Index 3: actual=0, pred=1 → FP
Index 4: actual=1, pred=1 → TP

TP=2, TN=1, FP=1, FN=1
Confusion Matrix: [[2, 1], [1, 1]]
Accuracy = (2+1)/(2+1+1+1) = 3/5 = 0.6
Precision = 2/(2+1) = 2/3 ≈ 0.667
Recall = 2/(2+1) = 2/3 ≈ 0.667
F1 = 2*0.667*0.667/(0.667+0.667) ≈ 0.667
Specificity = 1/(1+1) = 0.5
NPV = 1/(1+1) = 0.5
```

### Example 2:
```
Input:
actual = [1, 1, 1, 1]
predicted = [1, 1, 1, 1]

Output:
([[4, 0], [0, 0]], 1.0, 1.0, nan, nan)

Reasoning:
Perfect predictions on all positive cases.
TP=4, TN=0, FP=0, FN=0
Note: Specificity and NPV are undefined (division by zero) when TN=0
```

### Example 3:
```
Input:
actual = [0, 0, 0, 0]
predicted = [0, 0, 0, 0]

Output:
([[0, 0], [0, 4]], 1.0, nan, 1.0, 1.0)

Reasoning:
Perfect predictions on all negative cases.
TP=0, TN=4, FP=0, FN=0
Note: F1 is undefined when TP=0
```

## Solution: Comprehensive Metrics Calculation Approach

```python
import numpy as np

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
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Converting lists to arrays: O(n)
  - Computing TP, TN, FP, FN: O(n) each
  - Computing metrics: O(1) each
  - Overall: O(n)

- **Space Complexity**: O(n)
  - Storing numpy arrays: O(n)
  - All other variables are scalars: O(1)
  - Overall: O(n)