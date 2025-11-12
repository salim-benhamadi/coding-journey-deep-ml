# Implement Precision Metric

## Problem Statement

Write a Python function `precision` that calculates the precision metric given two numpy arrays: `y_true` and `y_pred`. The `y_true` array contains the true binary labels, and the `y_pred` array contains the predicted binary labels. Precision is defined as the ratio of true positives to the sum of true positives and false positives.

## Input
* `y_true`: A numpy array of true binary labels (0 or 1)
* `y_pred`: A numpy array of predicted binary labels (0 or 1)

## Output
* A float representing the precision score, rounded to 3 decimal places

## Constraints
* Both arrays must have the same length
* Labels are binary (0 or 1)
* Return 0.0 if there are no positive predictions (TP + FP = 0)

## Examples

### Example 1:
```
Input:
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

Output:
1.0

Reasoning:
TP = 3 (indices 0, 2, 5: predicted 1, actual 1)
FP = 0 (no cases where predicted 1, actual 0)
Precision = TP / (TP + FP) = 3 / (3 + 0) = 1.0
All positive predictions were correct.
```

### Example 2:
```
Input:
y_true = np.array([1, 1, 0, 0])
y_pred = np.array([1, 0, 1, 0])

Output:
0.5

Reasoning:
TP = 1 (index 0: predicted 1, actual 1)
FP = 1 (index 2: predicted 1, actual 0)
Precision = 1 / (1 + 1) = 0.5
Half of positive predictions were correct.
```

### Example 3:
```
Input:
y_true = np.array([1, 1, 1, 1])
y_pred = np.array([0, 0, 0, 0])

Output:
0.0

Reasoning:
TP = 0, FP = 0 (no positive predictions)
Return 0.0 to avoid division by zero.
```

### Example 4:
```
Input:
y_true = np.array([0, 0, 0, 0])
y_pred = np.array([1, 1, 1, 1])

Output:
0.0

Reasoning:
TP = 0, FP = 4
Precision = 0 / 4 = 0.0
All positive predictions were incorrect.
```

## Solution: Confusion Matrix Approach

```python
import numpy as np

def precision(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    
    if TP + FP == 0:
        return 0.0
    
    return round(TP / (TP + FP), 3)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Two passes through arrays to compute TP and FP
  - Each comparison and logical operation is O(1)

- **Space Complexity**: O(1)
  - Only storing scalar values for TP and FP
  - No additional data structures needed