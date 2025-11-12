# Generate a Confusion Matrix for Binary Classification

## Problem Statement

Your task is to implement the function `confusion_matrix(data)` that generates a confusion matrix for a binary classification problem. The confusion matrix provides a summary of the prediction results on a classification problem, allowing you to visualize how many data points were correctly or incorrectly labeled.

## Input
* `data`: A list of lists, where each inner list represents a pair `[y_true, y_pred]` for one observation. `y_true` is the actual label, and `y_pred` is the predicted label

## Output
* A 2×2 confusion matrix represented as a list of lists: `[[TP, FN], [FP, TN]]`

## Constraints
* Labels are binary (0 or 1)
* Input list is not empty
* Each inner list contains exactly two elements

## Examples

### Example 1:
```
Input:
data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]

Output:
[[1, 1], [2, 1]]

Reasoning:
Parsing the data:
- [1, 1]: True=1, Pred=1 → TP
- [1, 0]: True=1, Pred=0 → FN
- [0, 1]: True=0, Pred=1 → FP
- [0, 0]: True=0, Pred=0 → TN
- [0, 1]: True=0, Pred=1 → FP

TP = 1, FN = 1, FP = 2, TN = 1
Matrix: [[1, 1], [2, 1]]
```

### Example 2:
```
Input:
data = [[1, 1], [1, 1], [0, 0], [0, 0]]

Output:
[[2, 0], [0, 2]]

Reasoning:
All predictions are correct.
TP = 2, FN = 0, FP = 0, TN = 2
Matrix: [[2, 0], [0, 2]]
```

### Example 3:
```
Input:
data = [[1, 0], [1, 0], [0, 1], [0, 1]]

Output:
[[0, 2], [2, 0]]

Reasoning:
All predictions are incorrect.
TP = 0, FN = 2, FP = 2, TN = 0
Matrix: [[0, 2], [2, 0]]
```

### Example 4:
```
Input:
data = [[1, 1], [0, 0]]

Output:
[[1, 0], [0, 1]]

Reasoning:
Perfect binary classification with one positive and one negative case.
TP = 1, FN = 0, FP = 0, TN = 1
Matrix: [[1, 0], [0, 1]]
```

## Solution: Array Manipulation Approach

```python
import numpy as np

def confusion_matrix(data):
    y_true, y_pred = np.array(data)[:, 0], np.array(data)[:, 1]
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    return [[TP, FN], [FP, TN]]
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Converting to numpy array and slicing: O(n)
  - Four passes through arrays to compute TP, FN, FP, TN: O(n)
  - Overall: O(n)

- **Space Complexity**: O(n)
  - Storing y_true and y_pred arrays: O(n)
  - Output matrix is constant size: O(1)