# Sigmoid Activation Function Understanding

## Problem Statement

Write a Python function that computes the output of the sigmoid activation function given an input value z. The function should return the output rounded to four decimal places.

## Input
* `z`: A float representing the input value

## Output
* A float representing the sigmoid activation output, rounded to 4 decimal places

## Constraints
* Input can be any real number
* Output is always in the range (0, 1)

## Examples

### Example 1:
```
Input:
z = 0

Output:
0.5

Reasoning:
The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)). 
For z = 0, exp(-0) = 1, hence the output is 1 / (1 + 1) = 0.5.
```

### Example 2:
```
Input:
z = 2

Output:
0.8808

Reasoning:
σ(2) = 1 / (1 + exp(-2)) = 1 / (1 + 0.1353) ≈ 0.8808
```

### Example 3:
```
Input:
z = -2

Output:
0.1192

Reasoning:
σ(-2) = 1 / (1 + exp(2)) = 1 / (1 + 7.3891) ≈ 0.1192
```

### Example 4:
```
Input:
z = 10

Output:
0.9999

Reasoning:
For large positive values, sigmoid approaches 1.
σ(10) = 1 / (1 + exp(-10)) ≈ 0.9999
```

### Example 5:
```
Input:
z = -10

Output:
0.0000

Reasoning:
For large negative values, sigmoid approaches 0.
σ(-10) = 1 / (1 + exp(10)) ≈ 0.0000 (rounded)
```

## Solution: Mathematical Formula Approach

```python
import math

def sigmoid(z: float) -> float:
    output = 1 / (1 + math.exp(-z))
    return round(output, 4)
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - Exponential calculation is constant time
  - Arithmetic operations are constant time

- **Space Complexity**: O(1)
  - Only using constant extra space for the result
  - No additional data structures needed

