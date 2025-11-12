# Calculate Mean Absolute Error (MAE)

## Problem Statement

Implement a function to calculate the Mean Absolute Error (MAE) between two arrays of actual and predicted values. The MAE is a metric used to measure the average magnitude of errors in a set of predictions without considering their direction.

## Input
* `y_true`: A numpy array of actual values
* `y_pred`: A numpy array of predicted values

## Output
* A float representing the MAE, rounded to 3 decimal places

## Constraints
* Both arrays must have the same length
* Arrays can contain any real numbers (positive, negative, or zero)
* MAE is always non-negative

## Examples

### Example 1:
```
Input:
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

Output:
0.5

Reasoning:
Absolute errors: |3-2.5|, |-0.5-0.0|, |2-2|, |7-8|
              = |0.5|, |-0.5|, |0|, |-1|
              = 0.5, 0.5, 0, 1
MAE = (0.5 + 0.5 + 0 + 1) / 4 = 2.0 / 4 = 0.5
```

### Example 2:
```
Input:
y_true = np.array([1.0, 2.0, 3.0])
y_pred = np.array([1.0, 2.0, 3.0])

Output:
0.0

Reasoning:
Perfect predictions, all errors are 0.
MAE = (0 + 0 + 0) / 3 = 0.0
```

### Example 3:
```
Input:
y_true = np.array([10, 20, 30])
y_pred = np.array([15, 25, 35])

Output:
5.0

Reasoning:
All predictions are off by 5.
MAE = (5 + 5 + 5) / 3 = 15 / 3 = 5.0
```

### Example 4:
```
Input:
y_true = np.array([100])
y_pred = np.array([50])

Output:
50.0

Reasoning:
Single prediction with error of 50.
MAE = 50 / 1 = 50.0
```

## Solution: Vectorized NumPy Approach

```python
import numpy as np

def mae(y_true, y_pred):
    mae_result = np.mean(np.abs(y_true - y_pred))
    return round(mae_result, 3)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Element-wise subtraction: O(n)
  - Absolute value computation: O(n)
  - Mean calculation: O(n)
  - Overall: O(n)

- **Space Complexity**: O(n)
  - Temporary array for differences: O(n)
  - Temporary array for absolute values: O(n)
  - Overall: O(n)