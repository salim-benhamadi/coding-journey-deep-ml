# Single Neuron

## Problem Statement

Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, handling multidimensional input features. The function should take a list of feature vectors (each vector representing multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and bias as input. It should return the predicted probabilities after sigmoid activation and the mean squared error between the predicted probabilities and the true labels, both rounded to four decimal places.

## Input
* `features`: A list of lists, where each inner list represents features for one sample
* `labels`: A list of integers (0 or 1) representing true binary labels
* `weights`: A list of floats, one weight for each feature
* `bias`: A float representing the bias term

## Output
* A tuple containing:
  - List of floats: predicted probabilities (rounded to 4 decimal places)
  - Float: mean squared error (rounded to 4 decimal places)

## Constraints
* Number of features per sample must match the number of weights
* Labels must be binary (0 or 1)
* All inputs are valid numerical values

## Examples

### Example 1:
```
Input:
features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1

Output:
([0.4626, 0.4134, 0.6682], 0.3349)

Reasoning:
Sample 1: z = 0.7*0.5 + (-0.4)*1.0 + (-0.1) = -0.15, σ(-0.15) ≈ 0.4626
Sample 2: z = 0.7*(-1.5) + (-0.4)*(-2.0) + (-0.1) = -0.35, σ(-0.35) ≈ 0.4134
Sample 3: z = 0.7*2.0 + (-0.4)*1.5 + (-0.1) = 0.7, σ(0.7) ≈ 0.6682
MSE = mean([(0-0.4626)², (1-0.4134)², (0-0.6682)²]) ≈ 0.3349
```

### Example 2:
```
Input:
features = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
labels = [0, 1]
weights = [0.1, 0.2, 0.3]
bias = 0.5

Output:
([0.7858, 0.9820], 0.3088)

Reasoning:
Sample 1: z = 0.1*1.0 + 0.2*2.0 + 0.3*3.0 + 0.5 = 1.4, σ(1.4) ≈ 0.7858
Sample 2: z = 0.1*4.0 + 0.2*5.0 + 0.3*6.0 + 0.5 = 3.7, σ(3.7) ≈ 0.9820
MSE = mean([(0-0.7858)², (1-0.9820)²]) ≈ 0.3088
```

### Example 3:
```
Input:
features = [[0.0, 0.0]]
labels = [0]
weights = [1.0, 1.0]
bias = 0.0

Output:
([0.5000], 0.2500)

Reasoning:
z = 0.0*1.0 + 0.0*1.0 + 0.0 = 0.0, σ(0.0) = 0.5
MSE = (0 - 0.5)² = 0.25
```

## Solution: Vectorized NumPy Approach

```python
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    # Convert inputs to numpy arrays
    y_true = np.array(labels)
    W = np.array(weights)
    X = np.array(features)
    
    # Compute linear combination: z = w·x + b
    z = np.dot(X, W) + bias
    
    # Apply sigmoid activation: σ(z) = 1 / (1 + e^(-z))
    y_pred = round(1 / (1 + np.exp(-z)) 4).tolist()
    
    # Compute mean squared error
    mse = round(np.mean((y_true - y_pred) ** 2) 4).tolist()

    return y_pred, mse
```

### Complexity Analysis

- **Time Complexity**: O(m × n), where m is the number of samples and n is the number of features
  - Matrix multiplication (features × weights): O(m × n)
  - Sigmoid computation: O(m)
  - MSE calculation: O(m)
  - Overall: O(m × n)

- **Space Complexity**: O(m)
  - Storing predictions array: O(m)
  - Intermediate calculations: O(m)
  - Input arrays: O(m × n) but not counted as auxiliary space
