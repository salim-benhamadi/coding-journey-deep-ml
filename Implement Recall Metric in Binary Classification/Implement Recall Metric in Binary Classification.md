# Implement Recall Metric in Binary Classification

## Problem Statement

Your task is to implement the recall metric in a binary classification setting. Recall is a performance measure that evaluates how effectively a machine learning model identifies positive instances from all the actual positive cases in a dataset.

You need to write a function `recall(y_true, y_pred)` that calculates the recall metric. The function should accept two inputs:

* `y_true`: A list of true binary labels (0 or 1) for the dataset
* `y_pred`: A list of predicted binary labels (0 or 1) from the model

Your function should return the recall value rounded to three decimal places. If the denominator (TP + FN) is zero, the recall should be 0.0 to avoid division by zero.

## Input
* `y_true`: A numpy array of true binary labels (0 or 1)
* `y_pred`: A numpy array of predicted binary labels (0 or 1)

## Output
* A float representing the recall score, rounded to 3 decimal places

## Constraints
* Both arrays must have the same length
* Labels are binary (0 or 1)
* Return 0.0 if there are no positive cases in y_true

## Examples

### Example 1:
```
Input:
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

Output:
0.75

Reasoning:
TP = 3 (indices 0, 2, 5: predicted 1, actual 1)
FN = 1 (index 3: predicted 0, actual 1)
Recall = TP / (TP + FN) = 3 / (3 + 1) = 0.75
The model correctly identified 3 out of 4 positive instances.
```

### Example 2:
```
Input:
y_true = np.array([1, 1, 1, 1])
y_pred = np.array([1, 1, 1, 1])

Output:
1.0

Reasoning:
TP = 4, FN = 0
Recall = 4 / 4 = 1.0
Perfect recall - all positive cases identified.
```

### Example 3:
```
Input:
y_true = np.array([1, 1, 1, 1])
y_pred = np.array([0, 0, 0, 0])

Output:
0.0

Reasoning:
TP = 0, FN = 4
Recall = 0 / 4 = 0.0
Model missed all positive cases.
```

### Example 4:
```
Input:
y_true = np.array([0, 0, 0, 0])
y_pred = np.array([1, 1, 0, 0])

Output:
0.0

Reasoning:
No positive cases in y_true (TP + FN = 0)
Return 0.0 to avoid division by zero.
```

## Solution: Confusion Matrix Approach

```python
import numpy as np

def recall(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    
    if TP + FN == 0:
        return 0.0
    
    return round(TP / (TP + FN), 3)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Two passes through arrays to compute TP and FN
  - Each comparison and logical operation is O(1)

- **Space Complexity**: O(1)
  - Only storing scalar values for TP and FN
  - No additional data structures needed