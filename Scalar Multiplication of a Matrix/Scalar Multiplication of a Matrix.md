# Scalar Multiplication of a Matrix

## Problem Statement

Write a Python function that multiplies a matrix by a scalar and returns the result.

## Input
* `matrix`: A 2D list of integers or floats representing the input matrix
* `scalar`: An integer or float representing the scalar value to multiply with

## Output
* A 2D list representing the matrix after scalar multiplication

## Constraints
* Matrix can be of any valid dimensions
* Scalar can be any numeric value (int or float)

## Examples

### Example 1:
```
Input:
matrix = [[1, 2], [3, 4]], scalar = 2

Output:
[[2, 4], [6, 8]]

Reasoning:
Each element of the matrix is multiplied by the scalar.
```

### Example 2:
```
Input:
matrix = [[1, 2, 3], [4, 5, 6]], scalar = 0.5

Output:
[[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

Reasoning:
Each element is multiplied by 0.5.
```

## Solution 1: NumPy Approach

```python
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    import numpy as np
    return (np.array(matrix) * scalar).tolist()
```

### Complexity Analysis

- **Time Complexity**: O(m × n), where m and n are the dimensions of the matrix
  - NumPy performs element-wise multiplication efficiently
  - Converting to/from numpy array processes all elements

- **Space Complexity**: O(m × n)
  - Additional space for numpy array and result list

## Solution 2: Loop Approach

```python
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] *= scalar
    return result
```

### Complexity Analysis

- **Time Complexity**: O(m × n), where m and n are the dimensions of the matrix
  - Nested loops iterate through all matrix elements once
  - Each multiplication operation is O(1)

- **Space Complexity**: O(m × n)
  - Additional space needed for the result matrix copy