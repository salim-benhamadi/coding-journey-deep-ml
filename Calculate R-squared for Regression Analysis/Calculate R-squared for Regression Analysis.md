# Calculate R-squared for Regression Analysis

## Problem Statement

R-squared, also known as the coefficient of determination, is a measure that indicates how well the independent variables explain the variability of the dependent variable in a regression model.

Your Task: To implement the function `r_squared(y_true, y_pred)` that calculates the R-squared value, given arrays of true values `y_true` and predicted values `y_pred`.

## Input
* `y_true`: A numpy array of actual values
* `y_pred`: A numpy array of predicted values

## Output
* A float representing the R-squared value, rounded to 3 decimal places

## Constraints
* Both arrays must have the same length
* Arrays should contain numerical values
* R-squared typically ranges from 0 to 1, but can be negative for poor models

## Examples

### Example 1:
```
Input:
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])

Output:
0.989

Reasoning:
Mean of y_true = 3.0
SSR (residual sum of squares) = (1-1.1)² + (2-2.1)² + (3-2.9)² + (4-4.2)² + (5-4.8)²
                               = 0.01 + 0.01 + 0.01 + 0.04 + 0.04 = 0.11
SST (total sum of squares) = (1-3)² + (2-3)² + (3-3)² + (4-3)² + (5-3)²
                           = 4 + 1 + 0 + 1 + 4 = 10
R² = 1 - (0.11/10) = 1 - 0.011 = 0.989
```

### Example 2:
```
Input:
y_true = np.array([10, 20, 30, 40, 50])
y_pred = np.array([10, 20, 30, 40, 50])

Output:
1.0

Reasoning:
Perfect predictions, SSR = 0
R² = 1 - 0 = 1.0
```

### Example 3:
```
Input:
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([3, 3, 3, 3, 3])

Output:
0.0

Reasoning:
Predictions are always the mean of y_true.
This is equivalent to a baseline model.
R² = 0.0
```

### Example 4:
```
Input:
y_true = np.array([1, 2, 3])
y_pred = np.array([5, 6, 7])

Output:
-3.0

Reasoning:
Very poor predictions (worse than baseline).
Negative R² indicates model performs worse than simply predicting the mean.
```

## Solution: Variance Decomposition Approach

```python
import numpy as np

def r_squared(y_true, y_pred):
    y_mean = np.mean(y_true)
    SSR = np.sum((y_true - y_pred)**2)
    SST = np.sum((y_true - y_mean)**2)
    return round(1 - (SSR / SST), 3)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of samples
  - Computing mean: O(n)
  - Computing SSR: O(n)
  - Computing SST: O(n)
  - Overall: O(n)

- **Space Complexity**: O(1)
  - Only storing scalar values (mean, SSR, SST)
  - Temporary arrays created by NumPy operations are not counted
  - Overall: O(1)