# Binary Classification with Logistic Regression

## Problem Statement

Implement the prediction function for binary classification using Logistic Regression. Your task is to compute class probabilities using the sigmoid function and return binary predictions based on a threshold of 0.5.

## Input
* `X`: A numpy array of shape (m, n) containing feature vectors
* `weights`: A numpy array of shape (n,) containing model weights
* `bias`: A float representing the bias term

## Output
* A numpy array of shape (m,) containing binary predictions (0 or 1)

## Constraints
* X and weights dimensions must be compatible for matrix multiplication
* Predictions are 1 if probability ≥ 0.5, otherwise 0
* Output values are strictly 0 or 1

## Examples

### Example 1:
```
Input:
X = np.array([[1, 1], [2, 2], [-1, -1], [-2, -2]])
weights = np.array([1, 1])
bias = 0

Output:
[1 1 0 0]

Reasoning:
Linear outputs: [1*1 + 1*1 + 0, 2*1 + 2*1 + 0, -1*1 + -1*1 + 0, -2*1 + -2*1 + 0]
              = [2, 4, -2, -4]
Probabilities: [σ(2), σ(4), σ(-2), σ(-4)]
             ≈ [0.88, 0.98, 0.12, 0.02]
Predictions: [1, 1, 0, 0] (threshold = 0.5)
```

### Example 2:
```
Input:
X = np.array([[0, 0], [1, 0], [0, 1]])
weights = np.array([0.5, 0.5])
bias = -0.5

Output:
[0 0 0]

Reasoning:
Linear outputs: [0, 0, 0]
Probabilities: [0.5, 0.5, 0.5]
Since all are exactly 0.5, and threshold is >= 0.5, all predict to 1.
Wait, let me recalculate:
z = [0*0.5 + 0*0.5 - 0.5, 1*0.5 + 0*0.5 - 0.5, 0*0.5 + 1*0.5 - 0.5]
  = [-0.5, 0, 0]
σ(-0.5) ≈ 0.38, σ(0) = 0.5, σ(0) = 0.5
Predictions: [0, 1, 1]
```

### Example 3:
```
Input:
X = np.array([[5, 5], [-5, -5]])
weights = np.array([1, 1])
bias = 0

Output:
[1 0]

Reasoning:
Linear outputs: [10, -10]
Probabilities: [σ(10) ≈ 0.9999, σ(-10) ≈ 0.0001]
Predictions: [1, 0]
```

### Example 4:
```
Input:
X = np.array([[0]])
weights = np.array([2])
bias = -1

Output:
[0]

Reasoning:
Linear output: 0*2 - 1 = -1
Probability: σ(-1) ≈ 0.27
Prediction: 0 (< 0.5)
```

## Solution: Vectorized Logistic Regression Approach

```python
import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    linear_output = np.dot(X, weights) + bias
    probabilities = 1 / (1 + np.exp(-linear_output))
    predictions = np.where(probabilities >= 0.5, 1, 0)
    return predictions
```

### Complexity Analysis

- **Time Complexity**: O(m × n), where m is the number of samples and n is the number of features
  - Matrix multiplication (X · weights): O(m × n)
  - Element-wise operations (sigmoid, threshold): O(m)
  - Overall: O(m × n)

- **Space Complexity**: O(m)
  - Storing linear outputs: O(m)
  - Storing probabilities: O(m)
  - Storing predictions: O(m)
  - Overall: O(m)