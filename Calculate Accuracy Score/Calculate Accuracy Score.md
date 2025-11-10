# Calculate Accuracy Score

## Problem Statement

Write a Python function to calculate the accuracy score of a model's predictions. The function should take in two 1D numpy arrays: `y_true`, which contains the true labels, and `y_pred`, which contains the predicted labels. It should return the accuracy score as a float.

## Input
* `y_true`: A 1D numpy array containing true labels
* `y_pred`: A 1D numpy array containing predicted labels

## Output
* A float representing the accuracy score (ratio of correct predictions)

## Constraints
* Both arrays must have the same length
* Labels are typically binary (0 or 1) but can be any comparable values
* Accuracy is in the range [0, 1]

## Examples

### Example 1:
```
Input:
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])

Output:
0.8333333333333334

Reasoning:
Correct predictions: indices 0, 1, 3, 4, 5 (5 out of 6)
Incorrect predictions: index 2 (predicted 0, actual 1)
Accuracy = 5/6 ≈ 0.833
```

### Example 2:
```
Input:
y_true = np.array([1, 1, 1, 1])
y_pred = np.array([1, 1, 1, 1])

Output:
1.0

Reasoning:
All predictions are correct.
Accuracy = 4/4 = 1.0
```

### Example 3:
```
Input:
y_true = np.array([0, 0, 0, 0])
y_pred = np.array([1, 1, 1, 1])

Output:
0.0

Reasoning:
All predictions are incorrect.
Accuracy = 0/4 = 0.0
```

### Example 4:
```
Input:
y_true = np.array([1, 0, 1, 0, 1, 0, 1, 0])
y_pred = np.array([1, 0, 1, 0, 0, 1, 0, 1])

Output:
0.5

Reasoning:
Half of the predictions are correct.
Accuracy = 4/8 = 0.5
```

## Solution 1: Confusion Matrix Approach

```python
import numpy as np

def accuracy_score(y_true, y_pred):
    TP = np.sum((y_pred == 1) & (y_true == 1))
    TN = np.sum((y_pred == 0) & (y_true == 0))
    FP = np.sum((y_pred == 1) & (y_true == 0))
    FN = np.sum((y_pred == 0) & (y_true == 1))

    return (TP + TN) / (TP + TN + FP + FN)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Four passes through arrays to compute TP, TN, FP, FN
  - Each pass is O(n)
  - Overall: O(n)

- **Space Complexity**: O(1)
  - Only storing scalar values
  - No additional arrays created

## Solution 2: Direct Comparison Approach

```python
import numpy as np

def accuracy_score(y_true, y_pred):
    correct_predictions = np.sum(y_true == y_pred)
    total_samples = len(y_true)
    return correct_predictions / total_samples
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Single pass for element-wise comparison
  - O(n) for sum operation

- **Space Complexity**: O(1)
  - Boolean array created by comparison is temporary
  - Only storing count and length

