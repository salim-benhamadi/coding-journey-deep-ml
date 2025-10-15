# Linear Regression Using Gradient Descent

## Problem Statement

Write a Python function that performs linear regression using gradient descent. The function should take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array. Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.

## Input
* `X`: A NumPy array of shape (m, n) containing features with a column of ones for the intercept
* `y`: A NumPy array of shape (m,) containing target values
* `alpha`: A float representing the learning rate (α > 0)
* `iterations`: An integer representing the number of gradient descent iterations

## Output
* A NumPy array of shape (n, 1) containing the learned coefficients, rounded to 4 decimal places

## Constraints
* `X` should include a column of ones for the intercept term
* Learning rate should be positive and appropriately sized to ensure convergence
* Number of iterations should be sufficient for convergence

## Examples

### Example 1:
```
Input:
X = np.array([[1, 1], [1, 2], [1, 3]]), 
y = np.array([1, 2, 3]), 
alpha = 0.01, 
iterations = 1000

Output:
np.array([[0.1107], [0.9513]])

Reasoning:
The linear model is y ≈ 0.1107 + 0.9513*x, which approximates y = 0 + 1*x after gradient descent optimization.
```

### Example 2:
```
Input:
X = np.array([[1, 0], [1, 1], [1, 2], [1, 3]]),
y = np.array([2, 3, 4, 5]),
alpha = 0.01,
iterations = 1000

Output:
np.array([[2.0000], [1.0000]])

Reasoning:
The model learns y = 2.0 + 1.0*x, a perfect fit for the linear data.
```

### Example 3:
```
Input:
X = np.array([[1, 2, 3], [1, 4, 5], [1, 6, 7]]),
y = np.array([10, 20, 30]),
alpha = 0.001,
iterations = 5000

Output:
Approximately [[intercept], [coef1], [coef2]]

Reasoning:
Multiple feature linear regression with two predictors plus intercept.
```

## Solution: Gradient Descent Approach

```python
import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    n, m = X.shape
    theta = np.zeros((m, 1))

    def predict(X, theta):
        return np.dot(X, theta)

    def update_weights(X, y, theta, alpha):
        predictions = predict(X, theta)
        error = predictions - y.reshape(-1, 1)  
        gradient = (1 / n) * np.dot(X.T, error)  
        theta -= alpha * gradient
        return theta
    
    for _iteration_ in range(iterations):
        theta = update_weights(X, y, theta, alpha)

    return np.round(theta, 4)
```

### Complexity Analysis

- **Time Complexity**: O(iterations × m × n²), where m is number of samples and n is number of features
  - Each iteration performs:
    - Matrix multiplication X·θ: O(m × n)
    - Compute error: O(m)
    - Matrix multiplication X^T·error: O(n × m)
    - Gradient descent update: O(n)
  - Overall per iteration: O(m × n)
  - Total: O(iterations × m × n)

- **Space Complexity**: O(n)
  - Storing theta coefficients: O(n)
  - Temporary arrays for predictions and gradients: O(m) and O(n)
  - Dominated by O(max(m, n))
