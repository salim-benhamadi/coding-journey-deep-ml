# Calculate 2x2 Matrix Inverse

## Problem Statement

Write a Python function that calculates the inverse of a 2x2 matrix. Return `None` if the matrix is not invertible.

## Input
* `matrix`: A 2x2 list of floats representing the input matrix

## Output
* A 2x2 list of floats representing the inverse matrix, or `None` if not invertible

## Constraints
* Input is always a 2x2 matrix
* Matrix is not invertible if determinant is zero

## Examples

### Example 1:
```
Input:
matrix = [[4, 7], [2, 6]]

Output:
[[0.6, -0.7], [-0.2, 0.4]]

Reasoning:
The inverse of a 2x2 matrix [[a, b], [c, d]] is given by (1/(ad-bc)) * [[d, -b], [-c, a]], 
provided ad-bc is not zero.
```

### Example 2:
```
Input:
matrix = [[1, 2], [2, 4]]

Output:
None

Reasoning:
Determinant = (1*4) - (2*2) = 0, so the matrix is not invertible.
```

## Solution 1: NumPy Approach

```python
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    import numpy as np 
    matrix_array = np.array(matrix)
    determinant = np.linalg.det(matrix_array)
    if determinant:
        return np.linalg.inv(matrix_array).tolist()
    return None
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - Operations on 2x2 matrix are constant time
  - NumPy's determinant and inverse calculations are optimized

- **Space Complexity**: O(1)
  - Constant additional space for 2x2 operations

## Solution 2: Manual Calculation Approach

```python
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if determinant:
        inv_det = 1/determinant
        return [[inv_det*matrix[1][1], -inv_det*matrix[0][1]],
                [-inv_det*matrix[1][0], inv_det*matrix[0][0]]]
    return None
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - Fixed number of arithmetic operations regardless of input
  - Direct formula application for 2x2 matrix inverse

- **Space Complexity**: O(1)
  - Only stores determinant and creates result matrix
  - No additional data structures needed

### Mathematical Formula

For a 2x2 matrix:
```
[[a, b], [c, d]]
```
The inverse is:
```
(1/(ad-bc)) * [[d, -b], [-c, a]]
```
where `ad-bc` is the determinant.