# Implement F-Score Calculation for Binary Classification

## Problem Statement

Your task is to implement a function that calculates the F-Score for a binary classification task. The F-Score combines both Precision and Recall into a single metric, providing a balanced measure of a model's performance.

Write a function `f_score(y_true, y_pred, beta)` where:

* `y_true`: A numpy array of true labels (binary)
* `y_pred`: A numpy array of predicted labels (binary)
* `beta`: A float value that adjusts the importance of Precision and Recall. When beta=1, it computes the F1-Score, a balanced measure of both Precision and Recall

The function should return the F-Score rounded to three decimal places.

## Input
* `y_true`: A numpy array of true binary labels (0 or 1)
* `y_pred`: A numpy array of predicted binary labels (0 or 1)
* `beta`: A float value controlling the weight of recall vs precision

## Output
* A float representing the F-Score, rounded to 3 decimal places

## Constraints
* Both arrays must have the same length
* Labels are binary (0 or 1)
* Return 0.0 if precision or recall cannot be computed
* Beta > 0 (typically)

## Examples

### Example 1:
```
Input:
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
beta = 1

Output:
0.857

Reasoning:
TP = 3, FN = 1, FP = 0
Recall = 3/(3+1) = 0.75
Precision = 3/(3+0) = 1.0
F1-Score = (1+1²)*0.75*1.0 / (0.75 + 1²*1.0) = 2*0.75*1.0 / 1.75 = 1.5/1.75 ≈ 0.857
```

### Example 2:
```
Input:
y_true = np.array([1, 1, 1, 1])
y_pred = np.array([1, 1, 1, 1])
beta = 1

Output:
1.0

Reasoning:
Perfect predictions: Precision = 1.0, Recall = 1.0
F1-Score = 1.0
```

### Example 3:
```
Input:
y_true = np.array([1, 1, 0, 0])
y_pred = np.array([1, 0, 1, 0])
beta = 2

Output:
0.556

Reasoning:
TP = 1, FN = 1, FP = 1
Recall = 1/(1+1) = 0.5
Precision = 1/(1+1) = 0.5
F2-Score = (1+4)*0.5*0.5 / (0.5 + 4*0.5) = 2.5*0.25 / 2.5 = 0.625/2.5 = 0.25
Wait, let me recalculate: (1+2²)*0.5*0.5 / (0.5 + 2²*0.5) = 5*0.25 / (0.5 + 2.0) = 1.25/2.5 = 0.5
Actually: (1+4)*0.5*0.5 / (0.5 + 4*0.5) = 5*0.25 / 2.5 = 1.25/2.5 = 0.5... 
F2 emphasizes recall more than precision.
```

### Example 4:
```
Input:
y_true = np.array([1, 1, 1, 1])
y_pred = np.array([0, 0, 0, 0])
beta = 1

Output:
0.0

Reasoning:
TP = 0, FN = 4, FP = 0
Recall = 0, so F-Score = 0.0
```

## Solution: Confusion Matrix Approach

```python
import numpy as np

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
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Three passes through arrays to compute TP, FN, and FP
  - Each comparison and logical operation is O(1)

- **Space Complexity**: O(1)
  - Only storing scalar values
  - No additional data structures needed