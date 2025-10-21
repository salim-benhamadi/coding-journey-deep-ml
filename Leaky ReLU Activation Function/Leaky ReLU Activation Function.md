# Leaky ReLU Activation Function

## Problem Statement

Write a Python function `leaky_relu` that implements the Leaky Rectified Linear Unit (Leaky ReLU) activation function. The function should take a float `z` as input and an optional float `alpha`, with a default value of 0.01, as the slope for negative inputs. The function should return the value after applying the Leaky ReLU function.

## Input
* `z`: A float representing the input value
* `alpha`: A float representing the slope for negative inputs (default: 0.01)

## Output
* A float representing the Leaky ReLU activation output

## Constraints
* Input `z` can be any real number
* `alpha` is typically a small positive value (e.g., 0.01)
* Output preserves sign information (can be negative)

## Examples

### Example 1:
```
Input:
leaky_relu(0)

Output:
0

Reasoning:
For z = 0, the output is 0.
```

### Example 2:
```
Input:
leaky_relu(1)

Output:
1

Reasoning:
For z = 1 (positive), the output is z = 1.
```

### Example 3:
```
Input:
leaky_relu(-1)

Output:
-0.01

Reasoning:
For z = -1 with default alpha = 0.01, the output is 0.01 × (-1) = -0.01.
```

### Example 4:
```
Input:
leaky_relu(-2, alpha=0.1)

Output:
-0.2

Reasoning:
For z = -2 with alpha = 0.1, the output is 0.1 × (-2) = -0.2.
```

### Example 5:
```
Input:
leaky_relu(5.5, alpha=0.05)

Output:
5.5

Reasoning:
Positive values are returned as-is regardless of alpha.
```

## Solution : Ternary Operator Approach

```python
def leaky_relu(z: float, alpha: float = 0.01) -> float:
    return z if z > 0 else alpha * z
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - Single comparison and conditional return

- **Space Complexity**: O(1)
  - No additional data structures

