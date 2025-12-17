# Linear Regression Using Normal Equation

## Problem Statement

Write a Python function that performs linear regression using the normal equation. The function should take a matrix X (features) and a vector y (target) as input, and return the coefficients of the linear regression model. Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

## Input
* `X`: A list of lists representing the feature matrix (m samples × n features)
* `y`: A list of floats representing the target values

## Output
* A list of floats representing the coefficients (theta values), rounded to 4 decimal places

## Constraints
* X should include a column of ones for the intercept term
* The number of samples must equal the length of y
* X^T * X must be invertible

## Examples

### Example 1:
```
Input:
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]

Output:
[0.0, 1.0]

Reasoning:
The linear model is y = 0.0 + 1.0*x, perfectly fitting the input data.
First column of X is all 1s (intercept term).
The model: y = 0.0 * 1 + 1.0 * x
```

### Example 2:
```
Input:
X = [[1, 1], [1, 2], [1, 3], [1, 4]]
y = [2, 4, 6, 8]

Output:
[0.0, 2.0]

Reasoning:
The linear model is y = 0.0 + 2.0*x.
Perfect fit: y = 2x
```

### Example 3:
```
Input:
X = [[1, 0], [1, 1], [1, 2]]
y = [1, 3, 5]

Output:
[1.0, 2.0]

Reasoning:
The linear model is y = 1.0 + 2.0*x.
```

### Example 4:
```
Input:
X = [[1, 2, 3], [1, 4, 5], [1, 6, 7]]
y = [10, 20, 30]

Output:
[theta0, theta1, theta2]

Reasoning:
Multiple linear regression with 2 features plus intercept.
```

## Solution: Normal Equation Approach

```python
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)
    
    # Normal equation: theta = (X^T * X)^(-1) * X^T * y
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    
    # Round to 4 decimal places
    theta = np.round(theta, 4)
    
    return theta.tolist()
```

### Complexity Analysis

- **Time Complexity**: O(n² × m + n³), where n is the number of features and m is the number of samples
  - Computing X^T × X: O(n² × m)
  - Matrix inversion: O(n³)
  - Matrix multiplication X^T × y: O(n × m)
  - Overall dominated by: O(n² × m + n³)

- **Space Complexity**: O(n²)
  - Storing X^T × X matrix: O(n²)
  - Other intermediate calculations: O(n × m) or less