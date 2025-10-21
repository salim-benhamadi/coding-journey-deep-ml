# Implement ReLU Activation Function

## Problem Statement

Write a Python function `relu` that implements the Rectified Linear Unit (ReLU) activation function. The function should take a single float as input and return the value after applying the ReLU function. The ReLU function returns the input if it's greater than 0, otherwise, it returns 0.

## Input
* `z`: A float representing the input value

## Output
* A float representing the ReLU activation output

## Constraints
* Input can be any real number
* Output is always non-negative (≥ 0)

## Examples

### Example 1:
```
Input:
relu(0)

Output:
0

Reasoning:
ReLU(0) = max(0, 0) = 0
```

### Example 2:
```
Input:
relu(1)

Output:
1

Reasoning:
ReLU(1) = max(0, 1) = 1 (positive value is returned as-is)
```

### Example 3:
```
Input:
relu(-1)

Output:
0

Reasoning:
ReLU(-1) = max(0, -1) = 0 (negative values become 0)
```

### Example 4:
```
Input:
relu(5.5)

Output:
5.5

Reasoning:
ReLU(5.5) = max(0, 5.5) = 5.5
```

### Example 5:
```
Input:
relu(-100)

Output:
0

Reasoning:
All negative values are mapped to 0.
```

## Solution : Max Function Approach

```python
def relu(z: float) -> float:
    return max(0, z)
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - Single comparison operation
  - Constant time regardless of input value

- **Space Complexity**: O(1)
  - No additional data structures
  - Only returns the comparison result
