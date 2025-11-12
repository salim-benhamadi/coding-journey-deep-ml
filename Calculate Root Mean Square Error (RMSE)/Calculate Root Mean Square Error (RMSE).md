# Calculate Root Mean Square Error (RMSE)

## Problem Statement

In this task, you are required to implement a function `rmse(y_true, y_pred)` that calculates the Root Mean Square Error (RMSE) between the actual values and the predicted values. RMSE is a commonly used metric for evaluating the accuracy of regression models, providing insight into the standard deviation of residuals.

Your Task:
Implement the function `rmse(y_true, y_pred)` to:
- Calculate the RMSE between the arrays `y_true` and `y_pred`
- Return the RMSE value rounded to three decimal places

The RMSE is defined as:

```
RMSE = √[(1/n) Σ(y_true,i - y_pred,i)²]
```

Where:
- n is the number of observations
- y_true,i and y_pred,i are the actual and predicted values for the i-th observation

## Input
* `y_true`: A numpy array of actual values
* `y_pred`: A numpy array of predicted values

## Output
* A float representing the RMSE, rounded to 3 decimal places

## Constraints
* Both arrays must have the same length
* Arrays can contain any real numbers
* RMSE is always non-negative

## Examples

### Example 1:
```
Input:
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

Output:
0.612

Reasoning:
Squared errors: (3-2.5)², (-0.5-0.0)², (2-2)², (7-8)²
              = 0.5², 0.5², 0², 1²
              = 0.25, 0.25, 0, 1
MSE = (0.25 + 0.25 + 0 + 1) / 4 = 1.5 / 4 = 0.375
RMSE = √0.375 ≈ 0.612
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
RMSE = √0 = 0.0
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
Squared errors: 25, 25, 25
MSE = 75 / 3 = 25
RMSE = √25 = 5.0
```

### Example 4:
```
Input:
y_true = np.array([100, 200])
y_pred = np.array([110, 190])

Output:
10.0

Reasoning:
Errors: 10, -10
Squared errors: 100, 100
MSE = 200 / 2 = 100
RMSE = √100 = 10.0
```

## Solution: Vectorized NumPy Approach

```python
import numpy as np

def rmse(y_true, y_pred):
    rmse_result = np.sqrt(np.mean((y_true - y_pred)**2))
    return round(rmse_result, 3)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Element-wise subtraction: O(n)
  - Squaring: O(n)
  - Mean calculation: O(n)
  - Square root: O(1)
  - Overall: O(n)

- **Space Complexity**: O(n)
  - Temporary array for differences: O(n)
  - Temporary array for squared differences: O(n)
  - Overall: O(n)